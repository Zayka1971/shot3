from handlpiper.question.base_question import BaseQuestion


class AgeFromQuestion(BaseQuestion):
    def question(self):
        return 'Укажите минимальный возраст для знакомства: '

    def is_valid_answer(self, answer, params):
        try:
            answer = int(answer)
            return 13 <= answer <= 100
        except ValueError:
            return False

    def get_param_name(self):
        return 'age_from'