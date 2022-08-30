class Question:
    def __init__(self, question_text, question_answer):
        self.question_text = question_text
        self.question_answer = question_answer

    def get_question_text(self):
        return self.question_text

    def get_question_answer(self):
        return self.question_answer

    def set_question(self, question_text, question_answer):
        self.question_text = question_text
        self.question_answer = question_answer


# new_q = Question("What is the capital of India?", "Delhi")
# print(f'{new_q.question_text} : {new_q.question_answer}')
