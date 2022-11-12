import unittest
from datetime import datetime
from decimal import Decimal
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
        self.assertEqual(budget_service.query(datetime.strptime('20221231', "%Y%m%d"), datetime.strptime('20221230', "%Y%m%d")), 0)
        print("test2 Ok")
    # test3 剛好一個整月
    def test_OneMonth_end(self):
        budget_service = BudgetService()
        budget_service.get_all = lambda: [Budget("202211", 300), Budget("202212", 31)]
        #self.assertEqual(budget_service.query('20221201', '20221231'), 31)
        self.assertEqual(
            budget_service.query(datetime.strptime('20221201', "%Y%m%d"), datetime.strptime('20221231', "%Y%m%d")), 31)
        print("test3 Ok")

    # test4 只有一個月，但不足
    def test_OneMonth_end(self):
        budget_service = BudgetService()
        budget_service.get_all = lambda: [Budget("202211", 300), Budget("202212", 31)]
        # self.assertEqual(budget_service.query('20221201', '20221231'), 31)
        self.assertEqual(
            budget_service.query(datetime.strptime('20221230', "%Y%m%d"), datetime.strptime('20221231', "%Y%m%d")),
            2)
        print("test4 Ok")

    # test5
    def test_OneMonth_end(self):
        budget_service = BudgetService()
        budget_service.get_all = lambda: [Budget("202210", 3100),Budget("202211", 300), Budget("202212", 31)]
        # self.assertEqual(budget_service.query('20221201', '20221231'), 31)
        self.assertEqual(
            budget_service.query(datetime.strptime('20221030', "%Y%m%d"), datetime.strptime('20221205', "%Y%m%d")),
            505)
        print("test5 Ok")

    # test6
    def test_OneMonth_end(self):
        budget_service = BudgetService()
        budget_service.get_all = lambda: [Budget("202210", 3100), Budget("202211", 300), Budget("202212", 31)]
        # self.assertEqual(budget_service.query('20221201', '20221231'), 31)
        self.assertEqual(
            budget_service.query(datetime.strptime('20221030', "%Y%m%d"), datetime.strptime('20221129', "%Y%m%d")),
            490)
        print("test6 Ok")

    # test2 20221101~20221102
    #def test_partial_star_end(self):
        #budget_service = BudgetService()
        #budget_service.get_all = lambda: [Budget("202211", 300), Budget("202212", 31)]

if __name__ == '__main__':
    unittest.main()
