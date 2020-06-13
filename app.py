from flask import Flask, request, json
from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAJ4csJ8PXEBANj9voaHgoq8q9FtP7XuXexQgYCkxk1aQecZApXZBQAfIOfAEkkFxdWUmWy7g4eYpW94nK4kQguESOYmzqss2uwCc19M830hLV7hJjy1hZAd6jv34iCAPSHXOZBEbSjfUvjWerZAqUsddv6d0E55lQux2wEklQTZA351P7fKt3'
GREETINGS = ['hola', 'buenas', 'lindo dia']

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'secret':
            return str(challenge) 
        return '400'
    else:
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            response_text = 'piu piu piu'
            if text_input in GREETINGS:
                response_text = 'wenas wenas'
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id, response_text)
        return '200'

if __name__ == "__main__":
    app.run(debug=True)
