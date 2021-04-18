import argparse
import os
import random
import threading
import time

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from flask import Flask


params = argparse.ArgumentParser()
params.add_argument('--heroku', action='store_true')
args = params.parse_args()

app = Flask(__name__)


ID, TOKEN = '203807582', \
            '8728ab818c22fe2cbacd1370f2eb67e96ee4be6eac98819ca366b0a1d09be8259f70197206b9b47b0dc7e'
vk_session = VkApi(
    token=TOKEN)
longpoll = VkBotLongPoll(vk_session, ID)
vk = vk_session.get_api()


@app.route("/")
def index():
    return "All works"


def listen():
    for event in longpoll.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Спасибо, что написали нам. Мы обязательно ответим",
                             random_id=random.randint(0, 2 ** 64))
        time.sleep(1)


def background(data):
    for function, arguments in data:
        download_thread = threading.Thread(target=function, name="Downloader", args=arguments)
        download_thread.start()


def main():
    # bot listener on background
    background_functions = [(listen, [])]
    background(background_functions)

    if args.heroku:  # run on heroku service
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:  # run on my pc
        app.run(port=8085, host='127.0.0.1', debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
