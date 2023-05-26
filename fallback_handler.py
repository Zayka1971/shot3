from handler.base_handler import BaseHandler


class FallbackHandler(BaseHandler):

    def should_handle(self, _message):
        return True

    def handle_impl(self, _message):
        self.write_msg('Не понимаю, о чем вы...')
