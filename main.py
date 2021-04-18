import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


ID, TOKEN = '203807582',\
            '8728ab818c22fe2cbacd1370f2eb67e96ee4be6eac98819ca366b0a1d09be8259f70197206b9b47b0dc7e'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, ID)

    for event in longpoll.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Спасибо, что написали нам. Мы обязательно ответим",
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()