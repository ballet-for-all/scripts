from model.clazz import Clazz


class Timetable(object):
    __TIMETABLE_NAME = u'timetableName'
    __CLASSES = u'classes'
    __REQUIRED_KEYS = [__CLASSES]

    def __init__(self, timetableName, classes):
        self.timetableName = timetableName
        classes = [Clazz.from_dict(clazz) for clazz in classes]
        # Remove None or empty element in classes
        self.classes = [
            clazz for clazz in classes
            if clazz != None and not clazz.is_empty()
        ]

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Timetable.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None
        return Timetable(source[u'timetableName'], source[u'classes'])

    def to_dict(self):
        timetable = {
            u'timetableName': self.timetableName,
            u'classes': [clazz.to_dict() for clazz in self.classes]
        }
        return timetable

    def is_empty(self):
        return not self.classes

    def __repr__(self):
        return (f'Timetable('
                f'timetableName={self.timetableName}, '
                f'classes={self.classes})')
