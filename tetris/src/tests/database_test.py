import unittest

from score_database.score_repository import score_repository

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()


    def test_score_saving(self):
        score_repository.save_score("test_user1", 123)
        score_repository.save_score("test_user2", 231)
        scores = score_repository.find_scores_desc()
        self.assertEqual(scores[0], ("test_user1", 123))
        self.assertEqual(scores[1], ("test_user2", 231))