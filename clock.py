import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_id = 37369639
api_hash = "0cbea3745b46f65f9abea27049246da3"

client = TelegramClient("session", api_id, api_hash)

async def main():
    while True:
        time = datetime.now().strftime("🕐 %H:%M")
        await client(UpdateProfileRequest(first_name=time))
        await asyncio.sleep(60)

async def start():
    await client.start()
    await main()

asyncio.run(start())
