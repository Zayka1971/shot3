from handler.base_handler import BaseHandler


class GreetingsHandler(BaseHandler):

    def keywords(self):
        return ['Привет', 'Hello', 'VKinder', 'ВКиндер']

    def handle_impl(self, _message):
        self.write_msg(f'Добро пожаловать в VKinder!\n ' \
                   f'Сервис предназначенный для романтических знакомств в соответствии с заданными параметрами ' \
                   f'(возраст, пол, город, семейное положение) и с учётом геолокации.\n' \
                   f'Напишите "Старт" для начала работы')
