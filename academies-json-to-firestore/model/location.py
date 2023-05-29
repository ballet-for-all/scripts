class Location(object):
    __LAT = u'lat'
    __LNG = u'lng'
    __CITY = u'city'
    __DISTRICT = u'district'
    __BLOCK = u'block'

    def __init__(self, lat: float, lng: float, city: str, district: str,
                 block: str):
        self.lat = lat
        self.lng = lng
        self.city = city
        self.district = district
        self.block = block

    @staticmethod
    def from_dict(source):
        return Location(source[Location.__LAT], source[Location.__LNG],
                        source[Location.__CITY], source[Location.__DISTRICT],
                        source[Location.__BLOCK])

    def to_dict(self):
        location = {
            Location.__LAT: self.lat,
            Location.__LNG: self.lng,
            Location.__CITY: self.city,
            Location.__DISTRICT: self.district,
            Location.__BLOCK: self.block
        }
        return location

    def __repr__(self):
        return (f'Location('
                f'lat={self.lat}, '
                f'lng={self.lng}, '
                f'city={self.city}, '
                f'district={self.district}, '
                f'block={self.block})')
