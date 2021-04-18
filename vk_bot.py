import random
import threading

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class VkGroup:
    def __init__(self, group_id, token):
        # initialization
        self.id = group_id
        self.token = token
        self.vk_session = VkApi(token=self.token)

        # events listener
        listener = threading.Thread(target=self.listen, name="listener", args=[])
        listener.start()

        # scheduler
        scheduler = threading.Thread(target=self.scheduler, name="scheduler", args=[])
        scheduler.start()

    def listen(self):
        longpoll = VkBotLongPoll(self.vk_session, self.id)
        for event in longpoll.listen():
            print(event)
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.own_handler(event)
                self.if_new_message(message=event.obj.message['text'],
                                    from_id=event.obj.message['from_id'],
                                    event=event)

    # client's scheduler
    def scheduler(self):
        pass

    # client's handler
    def own_handler(self, event):
        pass

    # handlers plugs
    def if_new_message(self, message, from_id, event):
        pass

    # methods
    def send_message(self, to_id, message):
        vk = self.vk_session.get_api()
        vk.messages.send(user_id=to_id,
                         message=message,
                         random_id=random.randint(0, 2 ** 64))
