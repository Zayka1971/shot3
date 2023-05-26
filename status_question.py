from handler.question.base_question import BaseQuestion


class StatusQuestion(BaseQuestion):
    def question(self):
        return 'Выберите семейное положение человека, с которым хотите познакомиться (1-не женат(незамужем),' \
               '2-встречается, 3-помолвлен(а), 4-женат(замужем), 5-все сложно,' \
               ' 6-в поисках, 7-в любви): '

    def is_valid_answer(self, answer, params):
        try:
            answer = int(answer)
            return 1 <= answer <= 7
        except ValueError:
            return False

    def get_param_name(self):
        return 'status'