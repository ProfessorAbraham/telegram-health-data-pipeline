CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    id BIGINT PRIMARY KEY,
    text TEXT,
    date TIMESTAMP,
    sender_id BIGINT
);
