class Pricing(object):
    def __init__(self, numberPerWeek, totalCount, durationInMonth,
                 classTimeInMinutes, plan, price):
        self.numberPerWeek = numberPerWeek
        self.totalCount = totalCount
        self.durationInMonth = durationInMonth
        self.classTimeInMinutes = classTimeInMinutes
        self.plan = plan
        self.price = price
