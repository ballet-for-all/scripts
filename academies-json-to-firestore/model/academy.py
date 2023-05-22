from model.teacher import Teacher
from model.sns import Sns
from model.pricing import Pricing
from model.location import Location
from model.timetable import Timetable


class Academy(object):
    __NAME = u'name'
    __ADDRESS = u'address'
    __PHONE = u'phone'
    __SNS = u'sns'
    __COUPON = u'coupon'
    __IMAGES = u'images'
    __TEACHERS = u'teachers'
    __TIMETABLES = u'timetables'
    __PRICING = u'pricing'
    __PRICING_DESCRIPTION = u'pricingDescription'
    __LOCATION = u'location'
    __REQUIRED_KEYS = [
        __NAME, __ADDRESS, __PHONE, __SNS, __COUPON, __IMAGES, __TEACHERS,
        __TIMETABLES
    ]

    def __init__(self, name, address, phone, sns, coupon, images, teachers,
                 timetables, pricing, pricingDescription):
        self.name = name
        self.address = address
        self.phone = [phone_num for phone_num in phone if phone_num != None]
        self.sns = Sns.from_dict(sns)
        self.coupon = coupon
        self.images = [image for image in images if image != None]
        teachers = [Teacher.from_dict(teacher) for teacher in teachers]
        self.teachers = [
            teacher for teacher in teachers
            if teacher != None and not teacher.is_empty()
        ]
        timetables = [
            Timetable.from_dict(timetable) for timetable in timetables
        ]
        self.timetables = [
            timetable for timetable in timetables
            if timetable != None and not timetable.is_empty()
        ]
        pricing = [Pricing.from_dict(price) for price in pricing]
        self.pricing = [
            price for price in pricing
            if price != None and not price.is_empty()
        ]
        self.pricingDescription = pricingDescription

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Academy.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None

        academy = Academy(source[Academy.__NAME], source[Academy.__ADDRESS],
                          source[Academy.__PHONE], source[Academy.__SNS],
                          source[Academy.__COUPON], source[Academy.__IMAGES],
                          source[Academy.__TEACHERS],
                          source[Academy.__TIMETABLES],
                          source[Academy.__PRICING],
                          source[Academy.__PRICING_DESCRIPTION])
        if Academy.__LOCATION in source:
            academy.setLocation(source[Academy.__LOCATION])
        return academy

    def to_dict(self):
        academy = {
            Academy.__NAME:
            self.name,
            Academy.__ADDRESS:
            self.address,
            Academy.__PHONE:
            self.phone,
            Academy.__SNS:
            self.sns.to_dict(),
            Academy.__COUPON:
            self.coupon,
            Academy.__IMAGES:
            self.images,
            Academy.__TEACHERS:
            [teacher.to_dict() for teacher in self.teachers],
            Academy.__TIMETABLES:
            [timetable.to_dict() for timetable in self.timetables],
            Academy.__PRICING: [price.to_dict() for price in self.pricing],
            Academy.__PRICING_DESCRIPTION:
            self.pricingDescription
        }
        if hasattr(self, Academy.__LOCATION):
            academy[Academy.__LOCATION] = self.location.to_dict()
        return academy

    def setLocation(self, location):
        self.location = location

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
        if hasattr(self, Academy.__LOCATION):
            result += ', location={self.location}'
        return result + ')'
