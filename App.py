from flask import Flask, request
import telegram
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    chat_id = data['chat_id']
    message = data['message']
    bot.send_message(chat_id=chat_id, text=message)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
