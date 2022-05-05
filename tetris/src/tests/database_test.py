import unittest

from score_database.score_repository import score_repository


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()

    def test_score_saving(self):
        score_repository.save_score("test_user1", 123)
        score_repository.save_score("test_user2", 231)
        score_repository.save_score("test_user3", 230)
        scores = score_repository.find_scores_desc()
        self.assertEqual(scores[0], ("test_user2", 231))
        self.assertEqual(scores[1], ("test_user3", 230))
        self.assertEqual(scores[2], ("test_user1", 123))

    def test_amount_of_scores_retrieved(self):
        score_repository.save_score("test_user1", 123)
        score_repository.save_score("test_user2", 231)
        score_repository.save_score("test_user3", 230)
        score_repository.save_score("test_user4", 230)
        score_repository.save_score("test_user5", 230)
        score_repository.save_score("test_user6", 230)
        score_repository.save_score("test_user7", 230)
        score_repository.save_score("test_user8", 230)
        score_repository.save_score("test_user9", 230)
        score_repository.save_score("test_user10", 230)
        score_repository.save_score("test_user11", 230)
        scores = score_repository.find_scores_desc()
        self.assertEqual(len(scores), 10)
