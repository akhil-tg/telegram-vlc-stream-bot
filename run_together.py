"""
Run bot + FastAPI together - working version
"""
import os
import asyncio
import uvicorn
from pyrogram import Client, filters
from fastapi import FastAPI

# Bot setup with working token
bot = Client(
    "TelegramStreamBot",
    api_id=int(os.environ.get("API_ID", 0)),
    api_hash=os.environ.get("API_HASH", ""),
    bot_token=os.environ.get("BOT_TOKEN", "")
)

# FastAPI setup
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running", "bot": "online"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@bot.on_message(filters.command("start"))
async def start(client, message):
    print(f">>> Got /start from {message.from_user.id}")
    await message.reply("Hello! Bot is working!")

async def run_bot():
    print("Starting bot...")
    await bot.start()
    print("Bot started!")
    await bot.idle()

async def run_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(run_bot(), run_server())

if __name__ == "__main__":
    print("Running bot + server...")
    asyncio.run(main())