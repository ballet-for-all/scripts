from model.schedule import Schedule


class Clazz(object):
    __CLASS_NAME = u'className'
    __CLASS_TAG = u'classTag'
    __SCHEDULES = u'schedules'
    __REQUIRED_KEYS = [__CLASS_NAME, __SCHEDULES]

    def __init__(self, className, classTag, schedules):
        self.className = className
        self.classTag = classTag
        schedules = [Schedule.from_dict(schedule) for schedule in schedules]
        # Remove None or empty element in schedules
        self.schedules = [
            schedule for schedule in schedules
            if schedule != None and not schedule.is_empty()
        ]

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Clazz.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None

        return Clazz(source[Clazz.__CLASS_NAME], source[Clazz.__CLASS_TAG],
                     source[Clazz.__SCHEDULES])

    def to_dict(self):
        clazz = {
            Clazz.__CLASS_NAME: self.className,
            Clazz.__CLASS_TAG: self.classTag,
            Clazz.__SCHEDULES:
            [schedule.to_dict() for schedule in self.schedules]
        }
        return clazz

    def is_empty(self):
        return not self.className or not self.schedules

    def __repr__(self):
        return (f'Clazz('
                f'className={self.className}, '
                f'classTag={self.classTag}, '
                f'schedules={self.schedules})')
