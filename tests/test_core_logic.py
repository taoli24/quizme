import unittest
from question import Question, MultipleChoiceQuestion
from quiz_control import QuizControl

# Manually initialize a quiz list
quiz_list = [
    MultipleChoiceQuestion(q_type="multiple",
                           q_text="How many Hz does the video standard PAL support?",
                           q_answer="50",
                           q_incorrect=["59", "60", "25"],
                           q_acceptable_answers=['a', 'b', 'c', 'd']),
    Question(q_type="boolean",
             q_text="Ada Lovelace is often considered the first computer programmer.",
             q_answer="True",
             q_incorrect=[
                 "False"
             ],
             q_acceptable_answers=['true', 'false']),
    MultipleChoiceQuestion(q_type="multiple",
                           q_text=".at is the top-level domain for what country?",
                           q_answer="Austria",
                           q_incorrect=["Argentina", "Australia", "Angola"],
                           q_acceptable_answers=['a', 'b', 'c', 'd']),
    MultipleChoiceQuestion(q_type="multiple",
                           q_text="What internet protocol was documented in RFC 1459?",
                           q_answer="IRC",
                           q_incorrect=["HTTP", "HTTPS", "FTP"],
                           q_acceptable_answers=['a', 'b', 'c', 'd']),
    MultipleChoiceQuestion(q_type="multiple",
                           q_text="What amount of bits commonly equals one byte?",
                           q_answer="8",
                           q_incorrect=["1", "2", "64"],
                           q_acceptable_answers=['a', 'b', 'c', 'd']),
]


class TestCoreFunctions(unittest.TestCase):

    def test_still_has_questions(self):
        # Create quiz_controller with known questions and answers
        test_quiz_controller = QuizControl(quiz_list, "Science: Computers")
        # start of the quiz
        self.assertTrue(test_quiz_controller.still_has_questions())
        # questions 1 - 4
        for _ in range(4):
            test_quiz_controller.next_question()
            self.assertTrue(test_quiz_controller.still_has_questions())
        # question 5, still_has_question should return false
        test_quiz_controller.next_question()
        self.assertFalse(test_quiz_controller.still_has_questions())

    def test_check_correct_answers(self):
        # Create quiz_controller with known questions and answers
        test_quiz_controller = QuizControl(quiz_list, "Science: Computers")
        # question1
        for _ in range(5):
            test_quiz_controller.next_question()
            if test_quiz_controller.current_question.type == "boolean":
                self.assertTrue(test_quiz_controller.check_answer(test_quiz_controller.current_question.answer))
            else:
                correct_answer = list(test_quiz_controller.current_question.answer_list.keys())[list(test_quiz_controller.current_question.answer_list.values()).index(test_quiz_controller.current_question.answer)]
                self.assertTrue(test_quiz_controller.check_answer(correct_answer))


if __name__ == '__main__':
    unittest.main()
