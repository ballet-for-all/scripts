class Location(object):
    def __init__(self, latitude: float, longitude: float, block: str):
        self.latitude = latitude
        self.longitude = longitude
        self.block = block

    @staticmethod
    def from_dict(source):
        location = Location(source[u'latitude'], source[u'longitude'],
                            source[u'block'])
        return location

    def to_dict(self):
        location = {
            u'latitude': self.latitude,
            u'longitude': self.longitude,
            u'block': self.block
        }
        return location

    def __repr__(self):
        return (f'Location('
                f'latitude={self.latitude}, '
                f'longitude={self.longitude}, '
                f'block={self.block})')
