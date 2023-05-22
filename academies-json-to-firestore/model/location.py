class Location(object):
    __LATITUDE = u'latitude'
    __LONGITUDE = u'longitude'
    __BLOCK = u'block'

    # TODO: city, district 정보 추가
    def __init__(self, latitude: float, longitude: float, block: str):
        self.latitude = latitude
        self.longitude = longitude
        self.block = block

    @staticmethod
    def from_dict(source):
        return Location(source[Location.__LATITUDE],
                        source[Location.__LONGITUDE], source[Location.__BLOCK])

    def to_dict(self):
        location = {
            Location.__LATITUDE: self.latitude,
            Location.__LONGITUDE: self.longitude,
            Location.__BLOCK: self.block
        }
        return location

    def __repr__(self):
        return (f'Location('
                f'latitude={self.latitude}, '
                f'longitude={self.longitude}, '
                f'block={self.block})')
