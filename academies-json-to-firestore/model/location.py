class Location(object):
    __LATITUDE = u'latitude'
    __LONGITUDE = u'longitude'
    __CITY = u'city'
    __DISTRICT = u'district'
    __BLOCK = u'block'

    def __init__(self, latitude: float, longitude: float, city: str,
                 district: str, block: str):
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.district = district
        self.block = block

    @staticmethod
    def from_dict(source):
        return Location(source[Location.__LATITUDE],
                        source[Location.__LONGITUDE], source[Location.__CITY],
                        source[Location.__DISTRICT], source[Location.__BLOCK])

    def to_dict(self):
        location = {
            Location.__LATITUDE: self.latitude,
            Location.__LONGITUDE: self.longitude,
            Location.__CITY: self.city,
            Location.__DISTRICT: self.district,
            Location.__BLOCK: self.block
        }
        return location

    def __repr__(self):
        return (f'Location('
                f'latitude={self.latitude}, '
                f'longitude={self.longitude}, '
                f'city={self.city}, '
                f'district={self.district}, '
                f'block={self.block})')
