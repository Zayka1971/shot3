from handler.question.base_question import BaseQuestion


class SexQuestion(BaseQuestion):
    def question(self):
        return 'Введите пол человека, с которым хотите познакомиться (1-м, 2-ж, 0-любой)'

    def is_valid_answer(self, answer, params):
        try:
            answer = int(answer)
            return answer in [1, 2, 0]
        except ValueError:
            return False

    def get_param_name(self):
        return 'sex'