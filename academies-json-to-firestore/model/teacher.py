class Teacher(object):
    __NAME = u'name'
    __DESCRIPTION = u'description'
    __IMAGE_URL = u'imageUrl'
    __REQUIRED_KEYS = [__NAME, __DESCRIPTION, __IMAGE_URL]

    def __init__(self, name, description, imageUrl):
        self.name = name
        self.description = description
        self.imageUrl = imageUrl

    @staticmethod
    def from_dict(source):
        if source == None:
            return None
        for key in Teacher.__REQUIRED_KEYS:
            if source[key] == "" or source[key] == None:
                return None

        return Teacher(source[Teacher.__NAME], source[Teacher.__DESCRIPTION],
                       source[Teacher.__IMAGE_URL])

    def to_dict(self):
        teacher = {
            Teacher.__NAME: self.name,
            Teacher.__DESCRIPTION: self.description,
            Teacher.__IMAGE_URL: self.imageUrl
        }
        return teacher

    def is_empty(self):
        return not self.name or not self.description or not self.imageUrl

    def __repr__(self):
        return (f'Teacher('
                f'name={self.name}, '
                f'description={self.description}, '
                f'imageUrl={self.imageUrl})')
