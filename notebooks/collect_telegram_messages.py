from telethon.sync import TelegramClient
import json
import os

# Set your credentials
api_id = 12345678   # 🔁 Replace this with your API ID
api_hash = 'abc123yourhash'  # 🔁 Replace this with your API Hash
channel_username = 't.me/lobelia4cosmetics'  # 🔁 Replace with your target channel

# Where to save messages
output_path = "data/raw/telegram_messages/2025-07-09/lobelia4cosmetics.json"

# Start session
with TelegramClient('session_name', api_id, api_hash) as client:
    messages = []
    for message in client.iter_messages(channel_username, limit=200):  # Customize limit
        messages.append({
            "id": message.id,
            "text": message.text,
            "date": str(message.date),
            "sender_id": message.sender_id,
        })

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

print(f"✅ Collected {len(messages)} messages from {channel_username}")
