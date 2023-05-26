from handler.question.base_question import BaseQuestion


class HometownQuestion(BaseQuestion):
    def question(self):
        return 'Город проживания: '

    def is_valid_answer(self, answer, params):
        return True

    def get_param_name(self):
        return 'hometown'