class Sns(object):
    def __init__(self, kakaoTalk, naverTalkTalk, homepage, naverBlog,
                 naverCafe, naverModoo, instagram, facebook):
        self.kakaoTalk = kakaoTalk
        self.naverTalkTalk = naverTalkTalk
        self.homepage = homepage
        self.naverBlog = naverBlog
        self.naverCafe = naverCafe
        self.naverModoo = naverModoo
        self.instagram = instagram
        self.facebook = facebook

    @staticmethod
    def from_dict(source):
        sns = Sns(source[u'kakaoTalk'], source[u'naverTalkTalk'],
                  source[u'homepage'], source[u'naverBlog'],
                  source[u'naverCafe'], source[u'naverModoo'],
                  source[u'instagram'], source[u'facebook'])
        return sns

    def to_dict(self):
        sns = {
            u'kakaoTalk': self.kakaoTalk,
            u'naverTalkTalk': self.naverTalkTalk,
            u'homepage': self.homepage,
            u'naverBlog': self.naverBlog,
            u'naverCafe': self.naverCafe,
            u'naverModoo': self.naverModoo,
            u'instagram': self.instagram,
            u'facebook': self.facebook
        }
        return sns

    def __repr__(self):
        return (f'Sns('
                f'kakaoTalk={self.kakaoTalk}, '
                f'naverTalkTalk={self.naverTalkTalk}, '
                f'homepage={self.homepage}, '
                f'naverBlog={self.naverBlog}, '
                f'naverCafe={self.naverCafe}, '
                f'naverModoo={self.naverModoo}, '
                f'instagram={self.instagram}, '
                f'facebook={self.facebook})')
