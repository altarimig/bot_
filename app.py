from flask import Flask, request, json
from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAJqrGBZBIDkBAEgb5I4FOVDoRRpeSSHOSaisXyn9QGCmx2H2xTorzDW6P1zAluM1FKsHrZBw2BZB7GT1RTbFWWl8GjLP8n94hgfSoCcv9VuvKCttZC0PF194eTCxekU11zBHGbkzzHkZBjuBVb2ojepDZA6ZAgAixkegZAbuhhLDQZDZD'
GREETINGS = ['hola', 'hola que tal', 'buenas', 'ayuda']

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == '1dHjs0vDZW57nGNBy2gpjmRuAnK_4Tn24zjnDDK2jtJwTJHT8':
            return str(challenge) 
        return '400'
    else:
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            response_text = 'Lo siento, aún sigo aprendiendo tu lenguaje'
            if text_input in GREETINGS:
                response_text = 'Holaaa!!!, en que puedo apoyarte hoy día '
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id, response_text)
        return '200'

if __name__ == "__main__":
    app.run(debug=True)
