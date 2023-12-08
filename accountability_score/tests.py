from django.test import TestCase
from .utils import calculate_score

class AccountabilityScoreTestCase(TestCase):

    def test_new_account_score(self):
        # Calculate the score for a new account
        score = calculate_score(
            tasks=0,
            consistency=0.5,
            account_age=0,
            screen_time=0,
            task_retention=0.95
        )

        self.assertEqual(score, 500)

    def test_perfect_account_score(self):
        # Calculate the score for a perfect account
        score = calculate_score(
            tasks=21,
            consistency=1,
            account_age=365,
            screen_time=150000,
            task_retention=1
        )
        
        self.assertEqual(score, 850)

    def test_worst_account_score(self):
        # Calculate the score for the worst possible account
        score = calculate_score(
            tasks=0,
            consistency=0,
            account_age=0,
            screen_time=0,
            task_retention=0
        )
        
        self.assertEqual(score, 300)
