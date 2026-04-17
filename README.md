<div align="center">

  <img src="assets/banner.gif" alt="Telegram VLC Stream Bot Banner" width="60%">

  <br><br>

  <a href="https://github.com/ytcreatorstudio2001/telegram-vlc-stream-bot">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=35&duration=3000&pause=1000&color=2CA5E0&center=true&vCenter=true&width=700&lines=Telegram+VLC+Stream+Bot;Stream+Movies+Directly;No+Downloads+Required;Fast+Simple+Secure" alt="Typing SVG" />
  </a>

  <br><br>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/VLC-FF8800?style=for-the-badge&logo=videolan&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

  <br>

  <a href="https://github.com/ytcreatorstudio2001/telegram-vlc-stream-bot/stargazers">
    <img src="https://img.shields.io/github/stars/ytcreatorstudio2001/telegram-vlc-stream-bot?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/ytcreatorstudio2001/telegram-vlc-stream-bot/network/members">
    <img src="https://img.shields.io/github/forks/ytcreatorstudio2001/telegram-vlc-stream-bot?style=social" alt="GitHub forks"/>
  </a>
  <a href="https://github.com/ytcreatorstudio2001/telegram-vlc-stream-bot/watchers">
    <img src="https://img.shields.io/github/watchers/ytcreatorstudio2001/telegram-vlc-stream-bot?style=social" alt="GitHub watchers"/>
  </a>

</div>

<br>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2000&pause=500&color=8B5CF6&center=true&vCenter=true&width=800&lines=Stream+your+Telegram+files+instantly;Works+with+VLC+MX+Player+and+more;No+storage+needed+on+your+device;Perfect+for+movies+series+and+music" alt="Subtitle Animation" />
</p>

---

## 🚀 Overview

<div align="center">

**Telegram VLC Stream Bot** is a high-performance bot designed to let you stream media files from Telegram directly to **VLC Media Player** (or any other player) without waiting for downloads to complete. It acts as a bridge, creating a streaming URL that pipes the file content in real-time.

</div>

---

## ✨ Features

<div align="center">

| Feature | Description |
| :--- | :--- |
| 🎬 **Instant Streaming** | Start watching immediately, no waiting for downloads. |
| 📁 **Universal Support** | Works with Videos, Audio, and Documents. |
| ⚡ **High Speed** | Optimized for fast buffering and low latency. |
| 🖥️ **Multi-Platform** | Compatible with PC, Android, iOS, and TV. |
| ⛔ **No Limits** | Supports large files (2GB+) with ease. |
| 🔐 **Secure** | Safe interaction with Telegram API. |
| ☁️ **Easy Deploy** | Ready for Koyeb, Heroku, and VPS. |
| 👮‍♂️ **Admin Panel** | Built-in dashboard to manage users & settings. |
| 🗄️ **Database** | MongoDB support for persistent user data. |

</div>

---

## 🎯 How It Works

<div align="center">

```mermaid
graph LR
    A[� Telegram Cloud] -->|File Stream| B(🤖 Bot Server / FastAPI)
    B -->|HTTP Stream| C[🎥 VLC Player / User]
    D[👤 User Command] -->|Request| B
    style A fill:#2CA5E0,stroke:#1a8ac7,stroke-width:2px,color:#fff
    style B fill:#009688,stroke:#00796b,stroke-width:2px,color:#fff
    style C fill:#FF8800,stroke:#e67700,stroke-width:2px,color:#fff
    style D fill:#8B5CF6,stroke:#7c3aed,stroke-width:2px,color:#fff
```

</div>

---

## �🛠️ Deployment

### 🚀 One-Click Deploy (Koyeb)

<div align="center">
  <a href="https://app.koyeb.com/deploy?type=git&repository=github.com/akhil-tg/telegram-vlc-stream-bot&branch=master&name=telegram-vlc-bot">
    <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" width="200"/>
  </a>
</div>

<br>

### 🔑 Environment Variables

<div align="center">

| Variable | Description | Example |
| :--- | :--- | :--- |
| `API_ID` | Your Telegram API ID | Get from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API Hash | Get from [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Your Bot Token | Get from [@BotFather](https://t.me/BotFather) |
| `URL` | The public URL of your app | `https://your-app.koyeb.app` |
| `ADMINS` | Admin User IDs (space separated) | `123456789 987654321` |
| `DATABASE_URL` | MongoDB Connection String | `mongodb+srv://...` |
| `FORCE_SUB_CHANNEL` | Force Subscribe Channel ID/Username | `@MyChannel` or `-100...` |
| `LOG_CHANNEL` | Channel ID for Logs | `-100xxxxxxx` |

</div>

---

## 🧪 Local Development

<div align="center">

### Run the bot locally for testing or development

</div>

<br>

**1️⃣ Clone the repo:**
```bash
git clone https://github.com/ytcreatorstudio2001/telegram-vlc-stream-bot.git
cd telegram-vlc-stream-bot
```

**2️⃣ Install dependencies:**
```bash
pip install -r requirements.txt
```

**3️⃣ Run the bot:**
```bash
python main.py
```

**4️⃣ Expose locally (Optional):**
```bash
ngrok http 8080
```

---

## 📱 Usage

<div align="center">

### Simple 3-Step Process

</div>

<br>

```
1️⃣ Send any media file to the bot
2️⃣ Get a streaming URL instantly
3️⃣ Open in VLC and enjoy! 🍿
```

<div align="center">

**Supported Players:** VLC, MX Player, Kodi, MPV, and any player supporting HTTP streams

</div>

---

## 👮‍♂️ Admin Panel

<div align="center">

The bot features a powerful admin dashboard to manage your bot easily.

**Command:** `/admin` (Private Chat)

| Feature | Description |
| :--- | :--- |
| 📊 **Stats** | View total user count. |
| 📢 **Broadcast** | Send messages to all users. |
| 🖼️ **Banners** | Manage welcome banners. |
| 🔒 **Force Sub** | Check subscription settings. |
| 🔄 **Control** | Restart bot remotely. |

</div>

---

## 🤝 Contributing

<div align="center">

Contributions are always welcome! Here's how you can help:

<br>

| Type | Description |
| :--- | :--- |
| 🐛 **Bug Reports** | Found a bug? Open an issue! |
| 💡 **Feature Requests** | Have an idea? We'd love to hear it! |
| 🔧 **Pull Requests** | Code contributions are appreciated! |
| 📖 **Documentation** | Help improve our docs! |

</div>

---

## 👨‍💻 Author

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Created+with+love+by+Akhil+TG;Full+Stack+Developer;Open+Source+Enthusiast" alt="Author Animation" />

  <br><br>

  <a href="https://github.com/ytcreatorstudio2001">
    <img src="https://img.shields.io/badge/GitHub-Akhil_TG-181717?style=for-the-badge&logo=github"/>
  </a>
  <a href="https://t.me/akhil_tg">
    <img src="https://img.shields.io/badge/Telegram-Contact_Me-2CA5E0?style=for-the-badge&logo=telegram"/>
  </a>

</div>

---

## ⭐ Support This Project

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=800&color=FFD700&center=true&vCenter=true&repeat=true&width=600&lines=Star+this+repo+if+you+found+it+useful;Happy+Streaming;Enjoy+your+movies" alt="Support Animation" />

  <br><br>

  ### Show your support by giving a ⭐ if this project helped you!

  <br>

  <a href="https://hits.sh/github.com/ytcreatorstudio2001/telegram-vlc-stream-bot/">
    <img src="https://hits.sh/github.com/ytcreatorstudio2001/telegram-vlc-stream-bot.svg?style=for-the-badge&label=Visitors&color=2CA5E0" alt="Hits"/>
  </a>

</div>

---

## 📝 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<br>

Made with ❤️ and ☕

</div>
