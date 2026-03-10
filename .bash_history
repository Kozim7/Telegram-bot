pkg update
pkg install python
pkg install git
git clone https://github.com/SpEcHiDe/Telegram-Time-Auto-Name
cd Telegram-Time-Auto-Name
pip install -r requirements.txt
python bot.py
from telethon import TelegramClient, functions
import datetime
import time
import asyncio
# O'zingizning ma'lumotlaringizni kiriting
api_id = 1234567  # O'z API ID'ngiz
api_hash = 'sizning_api_hash_kodingiz'
client = TelegramClient('my_session', api_id, api_hash)
async def main():
with client:
pip install telethon
