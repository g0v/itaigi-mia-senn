from django.test import TestCase
from tsha.views import tsaSenn


# Create your tests here.
class SennTshiGiam(TestCase):
    def tearDown(self):
        self.assertEqual(tsaSenn(self.han), self.lo)

    def test_KooJiSenn(self):
        self.han = '方'
        self.lo = 'Png'

    def test_SiangJiSenn(self):
        self.han = '東方'
        self.lo = 'Tong-hong'

    def test_HokSenn(self):
        self.han = '郭陳'
        self.lo = 'Kueh-Tân'
