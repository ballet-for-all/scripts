class Schedule(object):
    __START_TIME = u'startTime'
    __DURATION_IN_MINUTES = u'durationInMinutes'
    __DAY = u'day'
    __TEACHER_NAME = u'teacherName'
    __REQUIRED_KEYS = [__START_TIME, __DURATION_IN_MINUTES, __DAY]

    def __init__(self, startTime, durationInMinutes, day, teacherName):
        self.startTime = startTime
        self.durationInMinutes = int(durationInMinutes)
        self.day = day
        self.teacherName = teacherName

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Schedule.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None

        return Schedule(source[Schedule.__START_TIME],
                        source[Schedule.__DURATION_IN_MINUTES],
                        source[Schedule.__DAY],
                        source[Schedule.__TEACHER_NAME])

    def to_dict(self):
        schedule = {
            Schedule.__START_TIME: self.startTime,
            Schedule.__DURATION_IN_MINUTES: self.durationInMinutes,
            Schedule.__DAY: self.day,
            Schedule.__TEACHER_NAME: self.teacherName
        }
        return schedule

    def is_empty(self):
        return not self.startTime or not self.durationInMinutes or not self.day

    def __repr__(self):
        return (f'Schedule('
                f'startTime={self.startTime}, '
                f'durationInMinutes={self.durationInMinutes}, '
                f'day={self.day}, '
                f'teacherName={self.teacherName})')
