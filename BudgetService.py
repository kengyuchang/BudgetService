from datetime import datetime



class BudgetService:
    def __init__(self) -> None:
        super().__init__()

    def query(self, star, end):
        budgets = self.get_all()
        dStar = datetime.strptime(star, "%Y%m%d")
        dEnd  = datetime.strptime(end, "%Y%m%d")
        dYearMonth = '{:%Y%m}'.format(dStar)
        days=(dEnd-dStar).days
        a = 0
        for x in budgets:
            if x.year_month==dYearMonth:
                a+=x.amount
        if (dEnd-dStar).days<0:
            return 0
        #if dStar.year==dEnd.year:
            #if dStar.month==dEnd.month:
        if a!=0:
            return a
        return 10

    def cals (self,dayCnt,dayMon,amount):
        return dayCnt/dayMon*amount

    #def addYearMonthChar(self,starday,endday):



    def get_all(self):
        pass
