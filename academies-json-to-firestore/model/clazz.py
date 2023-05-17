from model.schedule import Schedule


class Clazz(object):
    def __init__(self, className, classTag, schedules):
        self.className = className
        self.classTag = classTag
        self.schedules = [Schedule(**schedule) for schedule in schedules]
