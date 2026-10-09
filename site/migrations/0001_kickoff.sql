-- The kickoff deck's live layer (site/kickoff.js).
CREATE TABLE votes (            -- reactions (react:s3), "I was there" (there), the slide 4 poll (lesson), themes (theme), paid-work interest (paid)
  poll TEXT NOT NULL,
  option TEXT NOT NULL,
  client TEXT NOT NULL,
  created INTEGER NOT NULL,
  PRIMARY KEY (poll, option, client)
);
CREATE TABLE questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  client TEXT NOT NULL,
  created INTEGER NOT NULL,
  hidden INTEGER NOT NULL DEFAULT 0   -- set to 1 by hand to take a question down
);
CREATE TABLE upvotes (
  qid INTEGER NOT NULL REFERENCES questions(id),
  client TEXT NOT NULL,
  created INTEGER NOT NULL,
  PRIMARY KEY (qid, client)
);
CREATE TABLE entries (          -- intros and paid-work interest: personal data, only ever read through /export
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  kind TEXT NOT NULL,           -- intro | paid
  name TEXT, website TEXT, case_text TEXT, email TEXT, raw TEXT,
  client TEXT NOT NULL,
  created INTEGER NOT NULL
);
