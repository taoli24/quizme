from network import get_categories, get_questions
from question import Question, MultipleChoiceQuestion
from quiz_control import QuizControl
from colorama import Back, Style


def display_category(category_dict: dict) -> None:
    """
    display available categories

    :param category_dict: dict
    :return: None
    """
    print('Choose a category from below.\n')
    for key in category_dict:
        print(f"{key - 8} --- {categories.get(key)}")


def verify_user_choice(category_dict: dict) -> tuple:
    """
    Ask user for input and return user choice if valid choices are made

    :param category_dict: dict
    :return: (number_of_questions, choice): tuple
    """
    choice = 0
    number_of_questions = 0
    while choice not in [key - 8 for key in category_dict.keys()]:
        try:
            choice = int(input('\nChoose one of above categories: '))
        except ValueError:
            print('Please enter a valid number for your choice. ')
            continue
        if choice not in [key - 8 for key in categories.keys()]:
            print('Please choose from available categories.')

    while number_of_questions > 50 or number_of_questions < 10:
        try:
            number_of_questions = int(input('\nHow many questions would you like to do: (10-50) '))
        except ValueError:
            print('Please enter a valid number for your choice. ')
            continue
        if number_of_questions > 50 or number_of_questions < 10:
            print('Please choose between 10 and 50 questions.')

    return number_of_questions, choice + 8


def get_quiz_list(number_of_questions: int, user_choice_of_category: int) -> list:
    """
    Call network.get_questions() and retrieve questions from public api and return a list of
    Question objects.

    :param number_of_questions: int
    :param user_choice_of_category: int
    :return: quiz_list: list
    """
    quiz_list = []
    # create list with question objects
    for question in get_questions(number_of_questions, user_choice_of_category):
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
    return quiz_list


if __name__ == '__main__':
    # retrieve categories from public api
    categories = get_categories()
    # display categories to user
    display_category(categories)
    # verify and get user input
    number_questions, user_choice = verify_user_choice(categories)
    # initialise quiz controller object
    quiz_controller = QuizControl(get_quiz_list(number_questions, user_choice))

    # main logic - run when there is still questions
    while quiz_controller.still_has_questions():
        user_answer = None
        question_text = quiz_controller.next_question()
        while user_answer not in quiz_controller.current_question.acceptable_answers:
            user_answer = input(f'\n{question_text}\nYour answer: ')
            if user_answer not in quiz_controller.current_question.acceptable_answers:
                print(f'Please answer with {quiz_controller.current_question.acceptable_answers}')
        if quiz_controller.check_answer(user_answer):
            print(f"{Back.GREEN}That was correct.{Style.RESET_ALL}\n")
        else:
            print(f"{Back.RED}Sorry, that was wrong.{Style.RESET_ALL}\nThe correct answer is {quiz_controller.current_question.answer}.\n")


    # report score
    print(
        f'Your score is {quiz_controller.score}/{number_questions} with an accuracy of {quiz_controller.score / number_questions * 100:.2f}%')
