class Schedule(object):
    def __init__(self, startTime, durationInMinutes, day):
        self.startTime = startTime
        self.durationInMinutes = durationInMinutes
        self.day = day

    @staticmethod
    def from_dict(source):
        schedule = Schedule(source[u'startTime'], source[u'durationInMinutes'],
                            source[u'day'])
        return schedule

    def to_dict(self):
        schedule = {
            u'startTime': self.startTime,
            u'durationInMinutes': self.durationInMinutes,
            u'day': self.day
        }
        return schedule

    def __repr__(self):
        return (f'Schedule('
                f'startTime={self.startTime}, '
                f'durationInMinutes={self.durationInMinutes}, '
                f'day={self.day})')
