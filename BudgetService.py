ffrom datetime import datetime
from dateutil import parser
from dateutil import rrule
from decimal import Decimal
from dateutil.relativedelta import relativedelta
import calendar

def get_all(self):
    pass

class BudgetService:
    def __init__(self) -> None:
        super().__init__()

    def query(self, start, end):
        queryAmount = 0
        budgets = self.get_all()

        if start > end:
            return 0
        # 月份差
        monthRangeDays = self.clsMonth(start,end)

        if monthRangeDays >= 0:
            for i in range(0, monthRangeDays):
                cu_YYYYMMDD = start + relativedelta(months=+i)
                cu_month_start = datetime(cu_YYYYMMDD.year, cu_YYYYMMDD.month, 1)
                cu_month_end = datetime(cu_YYYYMMDD.year, cu_YYYYMMDD.month, calendar.monthrange(cu_YYYYMMDD.year, cu_YYYYMMDD.month)[1])
                if i==0:
                    if self.daydiff(cu_YYYYMMDD,cu_month_start) ==0 :
                        queryAmount+=  self.sameMonthFull(cu_YYYYMMDD, cu_month_end, budgets)
                    else:
                        queryAmount+=  self.sameMonthNotFull(cu_YYYYMMDD, cu_month_end, budgets)
                else:
                    if i<monthRangeDays-1:
                        queryAmount += self.sameMonthFull(cu_month_start, cu_month_end, budgets)
                    if i==monthRangeDays-1:
                        queryAmount += self.sameMonthNotFull(cu_month_start, end, budgets)
        return Decimal(queryAmount)

    def givenYYYYMMDays(self, givenDay):
        return calendar.monthrange(givenDay.year, givenDay.month)[1]

    def daydiff(self, in_start, in_end):
        return (in_end - in_start).days + 1

    def sameMonthFull(self, in_start, in_end, budgets):
        inAmount = 0
        for x in budgets:
            if x.year_month == in_start.strftime("%Y%m"):
                inAmount += x.amount
        return  inAmount

    def sameMonthNotFull(self, in_start, in_end, budgets):
        monthdays=self.givenYYYYMMDays(in_start)
        #diffdays=self.daydiff(end,start)+2
        diffdays=(in_end - in_start).days + 1
        inAmount = 0
        for x in budgets:
            if x.year_month == in_start.strftime("%Y%m"):
                inAmount += x.amount
        return inAmount*diffdays /monthdays

    def clsMonth(self,in_start, in_end):
        cu_month_start = datetime(in_start.year, in_start.month, 1)
        cu_month_end = datetime(in_end.year, in_end.month,
                                calendar.monthrange(in_end.year, in_end.month)[1])
        return rrule.rrule(rrule.MONTHLY, dtstart=cu_month_start, until=cu_month_end).count()

