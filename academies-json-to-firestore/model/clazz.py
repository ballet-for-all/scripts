from model.schedule import Schedule


class Clazz(object):
    def __init__(self, className, classTag, schedules):
        self.className = className
        self.classTag = classTag
        self.schedules = [Schedule(**schedule) for schedule in schedules]

    @staticmethod
    def from_dict(source):
        clazz = Clazz(source[u'className'], source[u'classTag'],
                      source[u'schedules'])
        return clazz

    def to_dict(self):
        clazz = {
            u'className': self.className,
            u'classTag': self.classTag,
            u'schedules': [schedule.to_dict() for schedule in self.schedules]
        }
        return clazz

    def __repr__(self):
        return (f'Clazz('
                f'className={self.className}, '
                f'classTag={self.classTag}, '
                f'schedules={self.schedules})')
