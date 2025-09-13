import telebot
import requests

# === CONFIG ===
TELEGRAM_TOKEN = "6544141692:AAEaDh-ega9I4EqqUc6waTrrBoe2GS92vY4"
GITHUB_TOKEN = "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"  # must have repo + workflow permissions
REPO_OWNER = "Pkoka99"
REPO_NAME = "Pkoka99"
WORKFLOW_FILE = "main.yml"  # or workflow_id if you prefer
BRANCH = "main"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# === COMMAND HANDLER ===
@bot.message_handler(commands=["createrdp"])
def run_workflow(message):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "ref": BRANCH,        # branch or tag to run on
        "inputs": {           # optional inputs if workflow requires
            # "param1": "value1"
        }
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 204:
        bot.reply_to(message, "✅ Workflow triggered successfully!")
    else:
        bot.reply_to(
            message,
            f"❌ Failed to trigger workflow.\nStatus: {resp.status_code}\nResponse: {resp.text}"
        )

# === START BOT ===
print("Bot is running...")
bot.infinity_polling()
