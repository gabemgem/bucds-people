DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS relationship;

CREATE TABLE person (
    name TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    type TEXT NOT NULL,
    pronouns TEXT,
    cohort INTEGER,
    researchtags TEXT,
    researchoverview TEXT,
    affiliations TEXT,
    othertags TEXT
);

CREATE TABLE relationship (
    source TEXT PRIMARY KEY,
    target TEXT NOT NULL,
    type TEXT
);