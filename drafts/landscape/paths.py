#!/usr/bin/env python3
"""Step 4: reorder the year's 26 readings into alternative paths -> paths in data/landscape.json.

Three paths through the same readings:
  - scheduled: the current syllabus order.
  - flow ("relatedness flow"): the shortest walk across the map from the kickoff, ignoring the syllabus order.
  - crossfit: each reading as different as possible from the one before.
Distance is cosine distance between reading-level embeddings (the mean of a reading's passages).
Crossfit keeps the year's arc: the first and last sessions stay fixed, and every reading stays
within WINDOW sessions of its scheduled slot. Flow uses map distance (nearest neighbour plus 2-opt). A seeded simulated annealing over swaps finds
each order; the result is deterministic.
"""
import json, math, random
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
WINDOW = 5
ITER, RESTARTS = 60000, 12

PATHS = {
    "scheduled": ("The planned arc", "This is the syllabus as we planned it. The year starts with agent swarms and moves through how nature, software systems and people send signals. It then rereads classic writing on business planning and ends with how to tend the environment that people and agents work in. Some steps are short, and some jump to a new part of the map on purpose."),
    "flow": ("Relatedness flow", "This path takes the shortest walk across the map. It starts at the kickoff, and each session moves to the nearest reading, so every reading sits next to the one before. It ignores the planned order."),
    "crossfit": ("Crossfit", "Each reading sits as far as possible from the one before, so every session makes the group switch context. Every reading still stays within five sessions of its planned slot, so the year keeps its overall shape."),
}


def cost(order, D):
    return sum(D[order[i], order[i + 1]] for i in range(len(order) - 1))


def anneal(D, sign, seed):
    n = len(D)
    rng = random.Random(seed)
    order = list(range(n))
    cur = sign * cost(order, D)
    best, best_c = order[:], cur
    T0 = 0.05
    for t in range(ITER):
        T = T0 * (1 - t / ITER) + 1e-4
        i, j = sorted(rng.sample(range(1, n - 1), 2))
        # window: each reading must stay within WINDOW of its scheduled slot (its index)
        if abs(order[i] - j) > WINDOW or abs(order[j] - i) > WINDOW:
            continue
        order[i], order[j] = order[j], order[i]
        c = sign * cost(order, D)
        if c <= cur or rng.random() < math.exp((cur - c) / T):
            cur = c
            if c < best_c:
                best, best_c = order[:], c
        else:
            order[i], order[j] = order[j], order[i]
    return best, sign * best_c


def shortest_walk(P, seed):
    """Open path from node 0 visiting all points, minimising map length: nearest neighbour, then 2-opt."""
    n = len(P)
    Dm = np.sqrt(((P[:, None] - P[None]) ** 2).sum(-1))
    rng = random.Random(seed)
    order, left = [0], set(range(1, n))
    while left:
        last = order[-1]
        cand = sorted(left, key=lambda j: Dm[last, j])[:2]
        nxt = cand[0] if seed == 0 or len(cand) == 1 else rng.choice(cand)
        order.append(nxt); left.remove(nxt)
    length = lambda o: sum(Dm[o[i], o[i + 1]] for i in range(n - 1))
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new = order[:i] + order[i:j + 1][::-1] + order[j + 1:]
                if length(new) < length(order) - 1e-9:
                    order, improved = new, True
    return order, length(order)


def main():
    L = json.loads((HERE / "data/landscape.json").read_text())
    R = np.load(HERE / "cache/reading_emb.npy")
    idx = {r["id"]: k for k, r in enumerate(L["readings"])}
    by_id = {r["id"]: r for r in L["readings"]}
    sched = [r for r in sorted((r for r in L["readings"] if r["session"]), key=lambda r: r["session"])]
    E = R[[idx[r["id"]] for r in sched]]
    D = 1 - E @ E.T

    P = np.array([[r["x"], r["y"]] for r in sched])
    results = {"scheduled": list(range(len(sched)))}
    results["flow"] = min((shortest_walk(P, s) for s in range(40)), key=lambda x: x[1])[0]
    results["crossfit"] = max((anneal(D, -1, seed) for seed in range(RESTARTS)), key=lambda x: x[1])[0]
    Dm = np.sqrt(((P[:, None] - P[None]) ** 2).sum(-1))

    out = []
    for key, order in results.items():
        name, why = PATHS[key]
        steps = [float(D[order[i], order[i + 1]]) for i in range(len(order) - 1)]
        out.append({"key": key, "name": name, "why": why, "stops": [sched[k]["id"] for k in order],
                    "mean_step": round(float(np.mean(steps)), 4)})
        maplen = sum(Dm[order[i], order[i + 1]] for i in range(len(order) - 1))
        print(f"{name:18s} meaning step {np.mean(steps):.3f} · map length {maplen:.2f} · longest map hop {max(Dm[order[i], order[i+1]] for i in range(len(order)-1)):.2f}")
    # movement paths: a route from area to area, one stop per movement
    import re
    nu = lambda u: re.sub(r"^https?://(www\.)?", "", (u or "").strip().lower()).rstrip("/")
    nt = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    by_url = {nu(r["url"]): r for r in L["readings"]}
    by_title = {nt(r["title"]): r for r in L["readings"]}
    moves_out = []
    for S in [json.loads((HERE.parent.parent / "tools/themes.json").read_text())]:
        S.update({"key": "syllabus", "name": "The year’s syllabus", "why": S["summary"], "movements": S["themes"]})
        moves = []
        for m in S["movements"]:
            ids, companions = [], []
            for x in m["readings"]:
                r = by_url.get(nu(x["url"])) or by_title.get(nt(x["title"]))
                if not r:
                    print("  missing from map:", x["title"]); continue
                ids.append(r["id"])
                if x.get("companion"):
                    companions.append(r["id"])
            pts = [(by_id[i]["x"], by_id[i]["y"]) for i in ids]
            moves.append({"n": m["n"], "name": m["name"], "blurb": m["blurb"], "stops": ids, "companions": companions,
                          "x": round(float(np.mean([p[0] for p in pts])), 4), "y": round(float(np.mean([p[1] for p in pts])), 4)})
        moves_out.append({"key": S["key"], "name": S["name"], "why": S["why"], "type": "movements", "movements": moves})
        print(f"{S['name']:18s} {len(moves)} movements, {sum(len(m['stops']) for m in moves)} readings")
    L["paths"] = moves_out  # only the recommended syllabus; the article-to-article paths are kept in code for reference
    L["slots"] = [s["date"] for s in json.loads((HERE.parent.parent / "tools/slots.json").read_text())]
    L.pop("dest", None)
    (HERE / "data/landscape.json").write_text(json.dumps(L, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
