import datetime
import schedule as schedule

ID = '203807582'
TOKEN = '21b426f2c33e1a65bbc8807ab67ff4d282e026b4b79e9d4b1e33f20f7a0072e137f4e77216ce578f6432a'


def if_new_message(vk, message, from_id, event):
    if message == 'Привет':
        answer = 'Ку'
    else:
        answer = 'Пошел в жопу'
    vk.send_message(to_id=from_id, message=answer)


def own_handler(vk, event):
    pass


def scheduler(vk):
    def job():
        message = datetime.datetime.now()
        vk.send_message(to_id=315336001, message=message)
    schedule.every(5).seconds.do(job)
    while True:
        schedule.run_pending()


methods = [if_new_message]
