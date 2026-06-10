# Nexus Music Bot

A Telegram Voice Chat music system featuring a clone deployment mechanism, group management tools, and persistent song queues.

## VPS Deployment Guide / VPS पर डिप्लॉय करने की गाइड

Follow these steps to deploy the bot on your VPS:

### 1. Update System / सिस्टम अपडेट करें
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Dependencies / जरूरी सॉफ्टवेयर डालें
Install Python 3.12, FFmpeg, MongoDB, and Redis.

```bash
# For Python 3.12, you might need the deadsnakes PPA on older Ubuntu versions
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip ffmpeg redis-server -y
```

For MongoDB, follow the official installation guide for your OS (Ubuntu/Debian).

### 3. Clone the Repository / कोड डाउनलोड करें
```bash
git clone https://github.com/your-username/nexus-music-bot.git
cd nexus-music-bot
```

### 4. Create Virtual Environment / वर्चुअल एनवायरनमेंट बनाएं
```bash
python3.12 -m venv venv
source venv/bin/activate
```

### 5. Install Requirements / लाइब्ररीज़ इंस्टॉल करें
```bash
pip install -r requirements.txt
```

### 6. Configuration / कॉन्फ़िगरेशन
Create a `.env` file and fill in the required variables:
```env
BOT_TOKEN=your_bot_token
API_ID=your_api_id
API_HASH=your_api_hash
MONGO_URI=your_mongodb_uri
REDIS_URL=redis://localhost:6379
OWNER_ID=your_id
LOG_CHANNEL=your_log_channel
```

### 7. Setup Cookies / कुकीज़ सेटअप करें
To prevent YouTube throttling and age restrictions, you need a `cookies.txt` file in the root directory.

1. Create the file:
   ```bash
   nano cookies.txt
   ```
2. Paste your YouTube cookies into the file.
3. Save (`Ctrl+O`, `Enter`) and exit (`Ctrl+X`).

**⚠️ SECURITY WARNING:** Never share your `cookies.txt` file or commit it to GitHub. It contains sensitive session tokens for your Google account. This project is configured to ignore `cookies.txt` via `.gitignore`.

### 8. Run the Bot / बॉट चलाएं
Use `tmux` or `screen` to keep the bot running after you close the terminal.

**Using tmux:**
```bash
tmux new -s nexus
source venv/bin/activate
python bot.py
```
Press `Ctrl+B` then `D` to detach. To reattach, use `tmux attach -t nexus`.

---

## Features
- Telegram Voice Chat music system.
- Clone deployment mechanism.
- Group management tools (ban/mute/notes/filters).
- Persistent song queues.
- Uses `ntgcalls` for high performance.
