class Pricing(object):
    __NUMBER_PER_WEEK = u'numberPerWeek'
    __TOTAL_COUNT = u'totalCount'
    __DURATION_IN_MONTH = u'durationInMonth'
    __CLASS_TIME_IN_MINUTES = u'classTimeInMinutes'
    __PLAN = u'plan'
    __ORIGINAL_PRICE = u'originalPrice'
    __SALE_PRICE = u'salePrice'
    __DISCOUNT_PERCENT = u'discountPercent'
    __REQUIRED_KEYS = [
        __DURATION_IN_MONTH, __CLASS_TIME_IN_MINUTES, __PLAN, __ORIGINAL_PRICE,
        __SALE_PRICE, __DISCOUNT_PERCENT
    ]

    def __init__(self, numberPerWeek, totalCount, durationInMonth,
                 classTimeInMinutes, plan, originalPrice, salePrice,
                 discountPercent):
        self.numberPerWeek = numberPerWeek
        self.totalCount = totalCount
        self.durationInMonth = durationInMonth
        self.classTimeInMinutes = classTimeInMinutes
        self.plan = plan
        self.originalPrice = int(str(originalPrice).replace(',', ''))
        self.salePrice = int(str(salePrice).replace(',', ''))
        self.discountPercent = discountPercent

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Pricing.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None

        return Pricing(
            source[Pricing.__NUMBER_PER_WEEK], source[Pricing.__TOTAL_COUNT],
            source[Pricing.__DURATION_IN_MONTH],
            source[Pricing.__CLASS_TIME_IN_MINUTES], source[Pricing.__PLAN],
            source[Pricing.__ORIGINAL_PRICE], source[Pricing.__SALE_PRICE],
            source[Pricing.__DISCOUNT_PERCENT])

    def to_dict(self):
        pricing = {
            Pricing.__NUMBER_PER_WEEK: self.numberPerWeek,
            Pricing.__TOTAL_COUNT: self.totalCount,
            Pricing.__DURATION_IN_MONTH: self.durationInMonth,
            Pricing.__CLASS_TIME_IN_MINUTES: self.classTimeInMinutes,
            Pricing.__PLAN: self.plan,
            Pricing.__ORIGINAL_PRICE: self.originalPrice,
            Pricing.__SALE_PRICE: self.salePrice,
            Pricing.__DISCOUNT_PERCENT: self.discountPercent
        }
        return pricing

    def is_empty(self):
        return (not self.durationInMonth or not self.classTimeInMinutes
                or not self.plan or not self.originalPrice
                or not self.salePrice or not self.discountPercent)

    def __repr__(self):
        return (f'Pricing('
                f'numberPerWeek={self.numberPerWeek}, '
                f'totalCount={self.totalCount}, '
                f'durationInMonth={self.durationInMonth}, '
                f'classTimeInMinutes={self.classTimeInMinutes}, '
                f'plan={self.plan}, '
                f'originalPrice={self.originalPrice}), '
                f'salePrice={self.salePrice}, '
                f'discountPercent={self.discountPercent})')
