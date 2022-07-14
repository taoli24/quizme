from network import get_categories, get_questions
from question import Question, MultipleChoiceQuestion
from quiz_control import QuizControl
from colorama import Back, Style

if __name__ == '__main__':
    user_choice = 0
    number_questions = 10
    quiz_list = []
    categories = get_categories()

    print('Choose a category from below.\n')

    for key in categories:
        print(f"{key - 8} --- {categories.get(key)}")

    while user_choice not in [key - 8 for key in categories.keys()]:
        try:
            user_choice = int(input('\nYour choice: '))
        except ValueError:
            print('Please enter a valid number for your choice. ')

        if user_choice not in [key - 8 for key in categories.keys()]:
            print('Please choose from available categories.')

    for question in get_questions(number_questions, user_choice + 8):
        new_question = Question(
            question['type'],
            question['question'],
            question['correct_answer'],
            question['incorrect_answers'],
            ['true', 'false']
        ) if question['type'] == 'boolean' \
            else MultipleChoiceQuestion(
            question['type'],
            question['question'],
            question['correct_answer'],
            question['incorrect_answers'],
            ['a', 'b', 'c', 'd']
        )
        quiz_list.append(new_question)

    quiz_controller = QuizControl(quiz_list)

    while quiz_controller.still_has_questions():
        user_answer = None
        question = quiz_controller.next_question()
        while user_answer not in quiz_controller.current_question.acceptable_answers:
            user_answer = input(f'\n{question}\nYour answer: ')

            if user_answer not in quiz_controller.current_question.acceptable_answers:
                print(f'Please answer with {quiz_controller.current_question.acceptable_answers}')
        print(quiz_controller.current_question.answer)
        if quiz_controller.check_answer(user_answer):
            print(f"{Back.GREEN}That is correct.{Style.RESET_ALL}")
        else:
            print(f"{Back.RED}Sorry, that was wrong.{Style.RESET_ALL}")

    print(f'Your score is {quiz_controller.score}/10 with an accuracy of {quiz_controller.score/10*100:.2f}%')
