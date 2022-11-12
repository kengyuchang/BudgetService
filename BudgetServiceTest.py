import unittest
from unittest.mock import Mock

from BudgetService import BudgetService


class Budget:
    def __init__(self, year_month, amount) -> None:
        super().__init__()
        self.amount = amount
        self.year_month = year_month


class BudgetServiceTest(unittest.TestCase):
    # test1
    #def test_something(self):
        #budget_service = BudgetService()
        # budget_service.get_all = lambda Budget('202212',31)
        # budget_service.get_all = lambda Budget('202212', 31)
        #self.assertEqual(True, True)  # add assertion here

    # test2 非法區間
    def test_illegal_star_end(self):
        budget_service = BudgetService()
        budget_service.get_all = lambda: [Budget("202211",300), Budget("202212", 31)]
        self.assertEqual(budget_service.query('20221231', '20221230'), 0)

    # test3
    def test_OneMonth_end(self):
        budget_service = BudgetService()s
        budget_service.get_all = lambda: [Budget("202211", 300), Budget("202212", 31)]
        self.assertEqual(budget_service.query('20221201', '20221231'), 31)
        print("test3 Ok")


    # test2 20221101~20221102
    #def test_partial_star_end(self):
        #budget_service = BudgetService()
        #budget_service.get_all = lambda: [Budget("202211", 300), Budget("202212", 31)]

if __name__ == '__main__':
    unittest.main()
