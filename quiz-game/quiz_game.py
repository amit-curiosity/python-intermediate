from question_data import question_data
from question_model import Question
from quiz_view import QuizView


def process_question_data():
    question_bank: list[Question] = []
    for question in question_data:
        question_text = question['question']
        question_answer = question['correct_answer']
        new_question_object = Question(question_text=question_text, question_answer=question_answer)
        question_bank.append(new_question_object)
    return question_bank
    # print(f'{question["question"]} : {question["correct_answer"]}')
    # print(question_bank)


def quiz_game():
    quiz = QuizView(process_question_data())

    while quiz.still_has_questions():
        quiz.retrieve_next_question()

    # print appropriate message
    print(f'\nYou\'ve completed the quiz.')
    print(f'Your final score is {quiz.score}/{quiz.question_number}')


if __name__ == '__main__':
    quiz_game()
