from handler.question.base_question import BaseQuestion, QuestionState
from model.user import User
import re

CLIENT_ID = '<CLIENT-ID>'
AUTH_LINK = 'https://oauth.vk.com/authorize?client_id=' + CLIENT_ID + '&display=page&scope=status.offline&response_type=token&v=5.92'


class TokenQuestion(BaseQuestion):
    def __init__(self, user_id, vk_group_client, db_session):
        self.db_session = db_session
        super().__init__(user_id, vk_group_client)

    def question(self):
        return 'Напишите ваш токен. Токен можно получить по этой ссылке: ' + AUTH_LINK

    def is_valid_answer(self, answer, params):
        return re.match('^[a-zA-Z0-9]+$', answer) is not None

    def should_ask(self):
        user = self.db_session.query(User).filter(User.id == self.user_id).first()
        return super().should_ask() and not user.token

    def handle_answer(self, answer, params):
        is_valid = self.is_valid_answer(answer, params)
        if is_valid:
            self.state = QuestionState.FULFILLED
            user = self.get_user()
            user.token = answer
            self.db_session.commit()
        return is_valid

    def get_user(self):
        return self.db_session.query(User).filter(User.id == self.user_id).first()