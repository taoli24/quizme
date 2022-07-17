import unittest
import network


category = {9: 'General Knowledge', 10: 'Entertainment: Books', 11: 'Entertainment: Film', 12: 'Entertainment: Music',
            13: 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television', 15: 'Entertainment: Video Games',
            16: 'Entertainment: Board Games', 17: 'Science & Nature', 18: 'Science: Computers',
            19: 'Science: Mathematics', 20: 'Mythology', 21: 'Sports', 22: 'Geography', 23: 'History', 24: 'Politics',
            25: 'Art', 26: 'Celebrities', 27: 'Animals', 28: 'Vehicles', 29: 'Entertainment: Comics',
            30: 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga',
            32: 'Entertainment: Cartoon & Animations'}


class TestNetworkFunctions(unittest.TestCase):

    def test_get_category(self):
        self.assertEqual(network.get_categories(), category)

    def test_get_questions_number(self):
        self.assertEqual(len(network.get_questions(10, 9)), 10)
        self.assertEqual(len(network.get_questions(50, 9)), 50)

    def test_get_question_category(self):
        self.assertEqual(network.get_questions(10, 18)[0].get('category'), 'Science: Computers')


if __name__ == '__main__':
    unittest.main()
