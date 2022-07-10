import random


class Question:
    def __init__(self, q_type, q_text, q_answer, q_incorrect, q_acceptable_answers):
        self.type = q_type
        self.text = q_text
        self.answer = q_answer
        self.incorrect = q_incorrect
        self.acceptable_answers = q_acceptable_answers


class MultipleChoiceQuestion(Question):
    def __init__(self, q_type, q_text, q_answer, q_incorrect, q_acceptable_answers):
        super().__init__(q_type, q_text, q_answer, q_incorrect, q_acceptable_answers)
        answers = [*q_incorrect, q_answer]
        random.shuffle(answers)
        self.answer_list = {chr(ind+97): answer for ind, answer in enumerate(answers)}
