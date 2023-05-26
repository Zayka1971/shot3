from handler.base_handler import BaseHandler


class FarewellHandler(BaseHandler):

    def keywords(self):
        return ['Пока', 'Bye']

    def handle_impl(self, _message):
        self.write_msg(f'Грустно видеть, как ты уходишь :(\nПока!')
