from html import unescape
from colorama import Back, Style


class QuizControl:
    def __init__(self, q_list: list):
        self._question_number = 0
        self._score = 0
        self._question_list = q_list
        self._current_question = None

    def still_has_questions(self):
        return self._question_number < len(self._question_list)

    def next_question(self):
        self._current_question = self._question_list[self._question_number]
        self._question_number += 1
        q_text = unescape(self._current_question.text)
        if self._current_question.type == 'boolean':
            q_text = f"{Style.BRIGHT}{Back.CYAN}Q.{self._question_number}: {q_text} (true/false): {Style.RESET_ALL}"
        else:
            q_text = f"{Style.BRIGHT}{Back.CYAN}Q.{self._question_number}: {q_text} (choose one): {Style.RESET_ALL}\n"
            for key in self._current_question.answer_list:
                q_text += f'{key}. {unescape(self._current_question.answer_list[key])}\n'
        return q_text

    def check_answer(self, user_answer):
        user_answer = user_answer if self._current_question.type == 'boolean' else self._current_question.answer_list.get(
            user_answer)
        correct_answer = self._current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self._score += 1
            return True
        else:
            return False

    def report_score(self):
        print(f'Your score is {self._score}/{len(self._question_list)} with an accuracy of {self._score / len(self._question_list) * 100:.2f}%')

    @property
    def current_question(self):
        return self._current_question
