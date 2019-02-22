from django.test import TestCase
from tsha.views import tsaSenn, tsaMia


class KaiBinTshiGiam(TestCase):
    def test_lian(self):
        kiatko = self.client.get('/李/阿水/').json()
        self.assertIn('Senn', kiatko)
        self.assertIn('Mia', kiatko)


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

    def test_KiThann(self):
        self.han = '媠'
        self.lo = 'Suí'

    def test_KiunnKhauTsha(self):
        self.han = '鄭'
        self.lo = 'Tēnn'


class MiaTshiGiam(TestCase):
    def tearDown(self):
        self.assertEqual(tsaMia(self.han), self.lo)

    def test_KooJi(self):
        self.han = '媠'
        self.lo = 'Suí'

    def test_SiangJi(self):
        self.han = '媠媠'
        self.lo = 'Suí-suí'

    def test_KhinSiannJi(self):
        self.han = '矣'
        self.lo = 'Ah'

    def test_BunIm(self):
        self.han = '向'
        self.lo = 'Hiòng'

    def test_KamJiTianBunIm(self):
        self.han = '丞'
        self.lo = 'Sîng'

    def test_KiunnKhauTsha(self):
        self.han = '雞'
        self.lo = 'Ke'

    def test_Phing(self):
        self.han = '萍'
        self.lo = 'Phîng'

    def test_KaTiKai(self):
        self.han = '小'
        self.lo = 'Sió'
