#!/usr/bin/env python3
"""Turn a page body from src/*.html into Markdown for agents, with every link made absolute.

Covers the elements the site uses: headings, paragraphs, lists (including the key/value "rows"
lists and numbered lists that start mid-way), tables, blockquotes, links, emphasis and code.
Images and the in-page contents nav are dropped; the Markdown has its own structure.
"""
from html.parser import HTMLParser
from urllib.parse import urljoin

BLOCK = {"p", "h1", "h2", "h3", "h4", "li", "blockquote", "table", "ul", "ol", "div", "nav", "figure"}


class Node:
    def __init__(self, tag, attrs, parent=None):
        self.tag, self.attrs, self.parent, self.kids = tag, dict(attrs), parent, []

    def cls(self):
        return self.attrs.get("class", "").split()


class Tree(HTMLParser):
    VOID = {"img", "br", "hr", "input", "meta", "link"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {})
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if tag not in self.VOID:
            self.cur = n

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)

    def handle_comment(self, data):
        pass


def to_markdown(body, base):
    t = Tree()
    t.feed(body)

    def inline(n):
        if isinstance(n, str):
            if not n.strip():
                return " " if n else ""
            # keep one space where the source had space next to a tag, so words don't run into links
            return (" " if n[0].isspace() else "") + " ".join(n.split()) + (" " if n[-1].isspace() else "")
        inner = "".join(inline(k) for k in n.kids)
        tag = n.tag
        if tag == "a":
            href = n.attrs.get("href", "")
            text = inner.strip()
            return f"[{text}]({urljoin(base, href)})" if href and not href.startswith("#") else text
        if tag in ("strong", "b"):
            return f"**{inner.strip()}**"
        if tag in ("em", "i", "cite"):
            return f"*{inner.strip()}*"
        if tag == "code":
            return f"`{inner.strip()}`"
        if tag == "br":
            return "  \n"
        if tag in ("img", "button", "input"):
            return ""
        return inner

    def text(n):
        return " ".join(inline(n).split())

    out = []

    def block(n, depth=0):
        if isinstance(n, str):
            if n.strip():
                out.append(" ".join(n.split()) + "\n")
            return
        tag, cls = n.tag, n.cls()
        if tag in ("nav", "img", "figure", "script", "style", "button", "form") or "html-only" in cls:
            return
        if tag in ("h1", "h2", "h3", "h4"):
            out.append("\n" + "#" * int(tag[1]) + " " + text(n) + "\n")
        elif tag == "p":
            line = text(n)
            if "index.md" in n.attrs.get("data-md-skip", "") or ("meta" in cls and "Markdown for agents" in line):
                return   # the page's own pointer to this file
            if line:
                out.append("\n" + (f"*{line}*" if "meta" in cls else line) + "\n")
        elif tag == "blockquote":
            parts = [text(k) for k in n.kids if not isinstance(k, str) and text(k)]
            out.append("\n" + "\n>\n".join("> " + x for x in parts) + "\n")
        elif tag in ("ul", "ol"):
            out.append("\n")
            i = int(n.attrs.get("start", 1))
            for li in (k for k in n.kids if not isinstance(k, str) and k.tag == "li"):
                key = next((k for k in li.kids if not isinstance(k, str) and "k" in k.cls()), None)
                if key is not None:   # a key/value row; lists inside the value stay lists
                    val = next((k for k in li.kids if not isinstance(k, str) and "v" in k.cls()), None)
                    paras, subs = [], []
                    for k in (val.kids if val is not None else []):
                        if isinstance(k, str):
                            if k.strip(): paras.append(" ".join(k.split()))
                        elif k.tag in ("ol", "ul"):
                            j = int(k.attrs.get("start", 1))
                            for sl in (x for x in k.kids if not isinstance(x, str) and x.tag == "li"):
                                subs.append(f"   {j}. " if k.tag == "ol" else "   - ")
                                subs[-1] += text(sl)
                                j += 1
                        else:
                            paras.append(text(k))
                    out.append(f"- **{text(key)}:** {' '.join(p for p in paras if p)}\n" + "".join(x + "\n" for x in subs))
                else:
                    out.append(("  " * depth) + (f"{i}. " if tag == "ol" else "- ") + text(li) + "\n")
                i += 1
        elif tag == "table":
            rows = []
            for tr in walk(n, "tr"):
                rows.append([text(c).replace("|", "\\|") for c in tr.kids if not isinstance(c, str) and c.tag in ("th", "td")])
            if rows:
                head, body = rows[0], rows[1:]
                if not walk(n, "thead"):   # a table without a header row: give it an empty one
                    head, body = [""] * len(rows[0]), rows
                out.append("\n| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n")
                out.extend("| " + " | ".join(r) + " |\n" for r in body)
        else:
            for k in n.kids:
                block(k, depth)

    def walk(n, tag):
        found = []
        for k in n.kids:
            if isinstance(k, str):
                continue
            if k.tag == tag:
                found.append(k)
            found.extend(walk(k, tag))
        return found

    for k in t.root.kids:
        block(k)
    md = "".join(out)
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")
    return md.strip() + "\n"
