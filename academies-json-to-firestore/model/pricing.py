class Pricing(object):
    def __init__(self, numberPerWeek, totalCount, durationInMonth,
                 classTimeInMinutes, plan, price):
        self.numberPerWeek = numberPerWeek
        self.totalCount = totalCount
        self.durationInMonth = durationInMonth
        self.classTimeInMinutes = classTimeInMinutes
        self.plan = plan
        self.price = price

    @staticmethod
    def from_dict(source):
        pricing = Pricing(source[u'numberPerWeek'], source[u'totalCount'],
                          source[u'durationInMonth'],
                          source[u'classTimeInMinutes'], source[u'plan'],
                          source[u'price'])
        return pricing

    def to_dict(self):
        pricing = {
            u'numberPerWeek': self.numberPerWeek,
            u'totalCount': self.totalCount,
            u'durationInMonth': self.durationInMonth,
            u'classTimeInMinutes': self.classTimeInMinutes,
            u'plan': self.plan,
            u'price': self.price
        }
        return pricing

    def __repr__(self):
        return (f'Pricing('
                f'numberPerWeek={self.numberPerWeek}, '
                f'totalCount={self.totalCount}, '
                f'durationInMonth={self.durationInMonth}, '
                f'classTimeInMinutes={self.classTimeInMinutes}, '
                f'plan={self.plan}, '
                f'price={self.price})')
