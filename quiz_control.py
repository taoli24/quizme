from html import unescape


class QuizControl:
    def __init__(self, q_list: list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = unescape(self.current_question.text)
        if self.current_question.type == 'boolean':
            q_text = f"Q.{self.question_number}: {q_text} (true/false):"
        else:
            q_text = f"Q.{self.question_number}: {q_text} (choose one):\n"
            for key in self.current_question.answer_list:
                q_text += f'{key}. {unescape(self.current_question.answer_list[key])}\n'

        return q_text

    def check_answer(self, user_answer):
        user_answer = user_answer if self.current_question.type == 'boolean' else self.current_question.answer_list.get(user_answer)
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
