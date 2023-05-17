class Teacher(object):
    def __init__(self, name, description, imageUrl):
        self.name = name
        self.description = description
        self.imageUrl = imageUrl

    @staticmethod
    def from_dict(source):
        teacher = Teacher(source[u'name'], source[u'description'],
                          source[u'imageUrl'])
        return teacher

    def to_dict(self):
        teacher = {
            u'name': self.name,
            u'description': self.description,
            u'imageUrl': self.imageUrl
        }
        return teacher

    def __repr__(self):
        return (f'Teacher('
                f'name={self.name}, '
                f'description={self.description}, '
                f'imageUrl={self.imageUrl})')
