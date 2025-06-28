import csv, asyncio, os
from pathlib import Path
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.contacts import ResolveUsernameRequest


API_ID   = 1234578 #int
API_HASH = ""
SESSION  = "tg_session"             # .session file
PHONE    = ""
TWO_FA   = "" #account password

GROUPS = ["Retweet_Like"]

async def grab_group(client, name):
    try:
        ent = (await client(ResolveUsernameRequest(name))).chats[0]
    except ValueError:
        print(f"‼ {name} can not resolve"); return []

    print(f"→ {ent.title} getting members…")
    users = []
    async for u in client.iter_participants(ent, aggressive=True):
        users.append({
            "group": ent.title,
            "id": u.id,
            "username": u.username or "",
            "first_name": u.first_name or "",
            "last_name": u.last_name or "",
            "phone": u.phone or "",
            "is_bot": u.bot,
            "is_verified": u.verified
        })
    return users

# ── MAIN ───────────────────────────────────────────
async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        
        sent = await client.send_code_request(PHONE)
        code = input("SMS/Telegram code: ")
        try:
            
            await client.sign_in(PHONE, code, password=TWO_FA)
        except SessionPasswordNeededError:
            await client.sign_in(password=TWO_FA)

    rows = []
    for g in GROUPS:
        rows += await grab_group(client, g)

    if not rows:
        print("No data scraped."); return
    with Path("members.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"✓ {len(rows)} done! -> members.csv")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
