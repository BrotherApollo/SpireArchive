CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS matches (
    id SERIAL PRIMARY KEY,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    difficulty VARCHAR(50) NOT NULL,
    won BOOLEAN NOT NULL,
    floors_cleared INT NOT NULL,
    elites_killed INT NOT NULL,
    gold_gained INT NOT NULL
);

CREATE TABLE IF NOT EXISTS match_players (
    id SERIAL PRIMARY KEY,
    match_id INT NOT NULL REFERENCES matches(id),
    player_id INT NOT NULL REFERENCES players(id),
    character VARCHAR(50) NOT NULL
);

INSTERT INTO players (name) VALUES ('Caleb'), ('Kenji');