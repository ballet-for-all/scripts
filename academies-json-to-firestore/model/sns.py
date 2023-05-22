class Sns(object):
    __KAKAO_TALK = u'kakaoTalk'
    __NAVER_TALK_TALK = u'naverTalkTalk'
    __HOMEPAGE = u'homepage'
    __NAVER_BLOG = u'naverBlog'
    __NAVER_CAFE = u'naverCafe'
    __NAVER_MODOO = u'naverModoo'
    __INSTAGRAM = u'instagram'
    __FACEBOOK = u'facebook'

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
        sns = Sns(source[Sns.__KAKAO_TALK], source[Sns.__NAVER_TALK_TALK],
                  source[Sns.__HOMEPAGE], source[Sns.__NAVER_BLOG],
                  source[Sns.__NAVER_CAFE], source[Sns.__NAVER_MODOO],
                  source[Sns.__INSTAGRAM], source[Sns.__FACEBOOK])
        return sns

    def to_dict(self):
        sns = {
            Sns.__KAKAO_TALK: self.kakaoTalk,
            Sns.__NAVER_TALK_TALK: self.naverTalkTalk,
            Sns.__HOMEPAGE: self.homepage,
            Sns.__NAVER_BLOG: self.naverBlog,
            Sns.__NAVER_CAFE: self.naverCafe,
            Sns.__NAVER_MODOO: self.naverModoo,
            Sns.__INSTAGRAM: self.instagram,
            Sns.__FACEBOOK: self.facebook
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
