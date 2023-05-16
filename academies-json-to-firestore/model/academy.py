from teacher import Teacher
from sns import Sns
from pricing import Pricing
from location import Location
from timetable import Timetable


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

    def setLocation(self, location):
        self.location = Location(**location)
