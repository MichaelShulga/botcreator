import datetime
import schedule as schedule
from vk_bot import VkGroup

ID = '203807582'
TOKEN = '21b426f2c33e1a65bbc8807ab67ff4d282e026b4b79e9d4b1e33f20f7a0072e137f4e77216ce578f6432a'


class ClientGroup(VkGroup):
    def if_new_message(self, message, from_id, event):
        if message == 'Привет':
            answer = 'Ку'
        else:
            answer = 'Пошел в жопу'
        self.send_message(to_id=from_id, message=answer)

    def own_handler(self, event):
        # https://vk.com/dev/groups_events
        pass

    def scheduler(self):
        def job():
            message = datetime.datetime.now()
            self.send_message(to_id=315336001, message=message)

        schedule.every(5).seconds.do(job)
        while True:
            schedule.run_pending()


def main():
    client_group = ClientGroup(ID, TOKEN)


if __name__ == '__main__':
    main()
