import importlib
import random
import threading

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class VkGroup:
    def __init__(self, client_settings):
        # initialization
        self.id = client_settings.ID
        self.token = client_settings.TOKEN
        self.vk_session = VkApi(token=self.token)

        # adding client's handlers functions
        self.if_new_message = client_settings.if_new_message.__get__(self)

        # events listener
        listener = threading.Thread(target=self.listen, name="listener", args=[])
        listener.start()

        # client's functions scheduler
        scheduler = threading.Thread(target=client_settings.scheduler, name="scheduler", args=[self])
        scheduler.start()

    def listen(self):
        longpoll = VkBotLongPoll(self.vk_session, self.id)
        for event in longpoll.listen():
            print(event)
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.if_new_message(message=event.obj.message['text'],
                                    from_id=event.obj.message['from_id'],
                                    event=event)

    # methods
    def send_message(self, to_id, message):
        vk = self.vk_session.get_api()
        vk.messages.send(user_id=to_id,
                         message=message,
                         random_id=random.randint(0, 2 ** 64))


def main():
    client_settings = importlib.import_module('UserFile')
    vk_group = VkGroup(client_settings)


if __name__ == '__main__':
    main()
