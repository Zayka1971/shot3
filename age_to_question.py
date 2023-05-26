from handler.question.base_question import BaseQuestion


class AgeToQuestion(BaseQuestion):
    def question(self):
        return 'Укажите максимальный возраст для знакомства: '

    def is_valid_answer(self, answer, params):
        try:
            answer = int(answer)
            return 13 <= answer <= 100 and int(params['age_from']) <= answer
        except ValueError:
            return False

    def get_param_name(self):
        return 'age_to'