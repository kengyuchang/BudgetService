import unittest

from BudgetService import BudgetService


class BudgetServiceTest(unittest.TestCase):
    #test1
    def test_something(self):
        budget_service = BudgetService()
        #budget_service.get_all = lambda Budget('202212',31)
        self.assertEqual(True, True)  # add assertion here

    #test2 非法區間

if __name__ == '__main__':
    unittest.main()
