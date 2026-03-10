import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import pytz

api_id = 37369639
api_hash = "0cbea3745b46f65f9abea27049246da3"

client = TelegramClient("session", api_id, api_hash)

tz = pytz.timezone("Asia/Tashkent")

async def main():
    while True:
        now = datetime.now(tz).strftime("🕐 %H:%M")
        await client(UpdateProfileRequest(first_name=now))
        await asyncio.sleep(60)

async def start():
    await client.start()
    await main()

asyncio.run(start())
