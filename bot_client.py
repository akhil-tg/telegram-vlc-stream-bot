"""
Telegram VLC Stream Bot - Bot Client Module
Copyright (c) 2025 Akhil TG. All Rights Reserved.
"""

from pyrogram import Client
from config import Config
import os
import time
import random

SESSION_DIR = os.getenv("SESSION_DIR", "/app/sessions" if os.path.exists("/app/sessions") else ".")
os.makedirs(SESSION_DIR, exist_ok=True)

session_name = f"StreamBot_{int(time.time())}_{random.randint(1000,9999)}"

class Bot(Client):
    def __init__(self):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins"),
            workdir=SESSION_DIR
        )
        self.boot_status = "Starting..."

    async def start(self):
        await super().start()
        print("Bot Started!")

    async def stop(self, *args):
        try:
            await super().stop()
            print("Bot Stopped!")
        except RuntimeError as e:
            if "attached to a different loop" not in str(e):
                raise

bot = Bot()