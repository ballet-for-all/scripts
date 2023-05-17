from model.teacher import Teacher
from model.sns import Sns
from model.pricing import Pricing
from model.location import Location
from model.timetable import Timetable


class Academy(object):
    def __init__(self, name, address, phone, sns, coupon, images, teachers,
                 timetables, pricing, pricingDescription):
        self.name = name
        self.address = address
        self.phone = phone
        self.sns = Sns(**sns)
        self.coupon = coupon
        self.images = images
        self.teachers = [Teacher(**teacher) for teacher in teachers]
        self.timetables = [Timetable(**timetable) for timetable in timetables]
        self.pricing = [Pricing(**price) for price in pricing]
        self.pricingDescription = pricingDescription

    @staticmethod
    def from_dict(source):
        academy = Academy(source[u'name'], source[u'address'],
                          source[u'phone'], source[u'sns'], source[u'coupon'],
                          source[u'images'], source[u'teachers'],
                          source[u'timetables'], source[u'pricing'],
                          source[u'pricingDescription'])
        if u'location' in source:
            academy.setLocation(source[u'location'])
        return academy

    def to_dict(self):
        academy = {
            u'name': self.name,
            u'address': self.address,
            u'phone': self.phone,
            u'sns': self.sns.to_dict(),
            u'coupon': self.coupon,
            u'images': self.images,
            u'teachers': [teacher.to_dict() for teacher in self.teachers],
            u'timetables':
            [timetable.to_dict() for timetable in self.timetables],
            u'pricing': [price.to_dict() for price in self.pricing],
            u'pricingDescription': self.pricingDescription
        }
        if self.location:
            academy[u'location'] = self.location.to_dict()
        return academy

    def setLocation(self, location):
        self.location = Location(**location)

    def __repr__(self):
        result = (f'Academy('
                  f'name={self.name}, '
                  f'address={self.address}, '
                  f'phone={self.phone}, '
                  f'sns={self.sns}, '
                  f'coupon={self.coupon}, '
                  f'images={self.images}, '
                  f'teachers={self.teachers}, '
                  f'timetables={self.timetables}, '
                  f'pricing={self.pricing}, '
                  f'pricingDescription={self.pricingDescription}')
        if hasattr(self, 'location'):
            result += ', location={self.location}'
        return result + ')'
