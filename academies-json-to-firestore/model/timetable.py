from model.clazz import Clazz


class Timetable(object):
    def __init__(self, timetableName, classes):
        self.timetableName = timetableName
        self.classes = [Clazz(**clazz) for clazz in classes]

    @staticmethod
    def from_dict(source):
        timetable = Timetable(source[u'timetableName'], source[u'classes'])
        return timetable

    def to_dict(self):
        timetable = {
            u'timetableName': self.timetableName,
            u'classes': [clazz.to_dict() for clazz in self.classes]
        }
        return timetable

    def __repr__(self):
        return (f'Timetable('
                f'timetableName={self.timetableName}, '
                f'classes={self.classes})')
