CREATE TABLE IF NOT EXISTS players (
    player_id   SERIAL PRIMARY KEY,
    player_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS characters (
    character_id     SERIAL PRIMARY KEY,
    player_id        INTEGER REFERENCES players(player_id),
    character_name   TEXT UNIQUE NOT NULL,
    rank             TEXT,
    level            INTEGER,
    character_class  INTEGER,
    race             TEXT,
    sex              INTEGER,
    last_online_days INTEGER,
    main_alt         TEXT,
    join_date        DATE,
    promo_date       DATE,
    rank_history     TEXT,
    birthday         DATE,
    public_note      TEXT,
    officer_note     TEXT,
    custom_note      TEXT,
    faction          TEXT,
    player_guid      TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS  items (
    sql_item_id    SERIAL PRIMARY KEY,
    item_id        INTEGER UNIQUE NOT NULL,
    item_name      TEXT,
    item_class     TEXT,
    item_sub_class TEXT,
    item_type      TEXT,
    inventory_type TEXT,
    quality        INTEGER,
    item_level     INTEGER
);

CREATE TABLE IF NOT EXISTS raids (
    raid_id  TEXT PRIMARY KEY,
    instance TEXT,
    date     DATE,
    time     TIME
);

CREATE TABLE IF NOT EXISTS raiders (
    raider_id    SERIAL PRIMARY KEY,
    raid_id      TEXT REFERENCES raids(raid_id),
    character_id INTEGER REFERENCES characters(character_id)
);

CREATE TABLE IF NOT EXISTS soft_reserves (
    sr_id        SERIAL PRIMARY KEY,
    raid_id      TEXT REFERENCES raids(raid_id),
    character_id INTEGER REFERENCES characters(character_id),
    item_id      INTEGER REFERENCES items(item_id)
);

CREATE TABLE IF NOT EXISTS loot_records (
    id           SERIAL PRIMARY KEY,
    checksum     TEXT UNIQUE NOT NULL,
    raid_id      TEXT REFERENCES raids(raid_id),
    character_id INTEGER REFERENCES characters(character_id),
    item_id      INTEGER REFERENCES items(item_id),
    is_sr        BOOLEAN,
    is_os        BOOLEAN,
    is_tmb       BOOLEAN,
    received     BOOLEAN,
    awarded_at   TIMESTAMPTZ,
    raw_data     JSONB
);