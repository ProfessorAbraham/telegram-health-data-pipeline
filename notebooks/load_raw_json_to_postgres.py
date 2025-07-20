import json
import psycopg2
from psycopg2.extras import execute_values
import os

# Load database connection info from environment variables (best practice)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "telegram_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_PORT = os.getenv("DB_PORT", 5432)

conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)

cur = conn.cursor()

# Path to JSON file
json_file_path = "data/raw/telegram_messages/2025-07-09/lobelia4cosmetics.json"

with open(json_file_path, "r", encoding="utf-8") as f:
    messages = json.load(f)

insert_query = """
INSERT INTO raw.telegram_messages (id, text, date, sender_id)
VALUES %s
ON CONFLICT (id) DO NOTHING;
"""

records = [(m['id'], m['text'], m['date'], m['sender_id']) for m in messages]

execute_values(cur, insert_query, records)
conn.commit()
cur.close()
conn.close()

print(f"Inserted {len(records)} messages into raw.telegram_messages")
