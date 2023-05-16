from clazz import Clazz


class Timetable(object):
    def __init__(self, timetableName, classes):
        self.timetableName = timetableName
        self.classes = [Clazz(**clazz) for clazz in classes]
