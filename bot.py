from flask import Flask, request
import telebot
import os

app = Flask(__name__)

# Token will come from Render environment variables (we'll add it later)
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Deborah Income Empire Bot ❤️\nFrom Grandma Deborah for real family income ideas.\nTry /ideas for quick hustles!")

@bot.message_handler(commands=['ideas'])
def ideas(message):
    bot.reply_to(message, "Henderson mom ideas to start today:\n1. UGC videos for brands ($100–$800) – billo.co or insense.pro\n2. TaskRabbit gigs (organizing, errands)\n3. Rover dog walking ($25–$40/walk)\n4. Sell digital products on Etsy (Notion templates)\nPick one, do 1 hour/day. You got this! 💪")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def home():
    return "Deborah Income Empire Bot is alive and ready! ❤️"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
  
