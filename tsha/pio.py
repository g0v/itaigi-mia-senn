from csv import DictReader
import io
import json
from json.decoder import JSONDecodeError
from urllib.request import urlopen
from 臺灣言語工具.羅馬字.台語 import 白話字
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Pio:
    github網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/'
    詞目總檔網址 = (
        github網址 + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    )
    詞目總檔屬性網址 = (
        github網址 +
        '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94'
        '.%E8%A9%9E%E7%9B%AE%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    )
    詞目總檔文白網址 = (
        github網址 +
        '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94'
        '.%E6%96%87%E7%99%BD%E5%B1%AC%E6%80%A7.csv'
    )
    甘字典網址 = (
        'https://github.com/fhl-net/Kam-Ui-lim_1913_Kam-Ji-tian'
        '/raw/master/dict.csv'
    )
    tongMia = 'miasenn.json'

    @classmethod
    def mia(cls):
        return cls._tshue()[0]

    @classmethod
    def senn(cls):
        return cls._tshue()[1]

    @classmethod
    def _tshue(cls):
        try:
            with open(cls.tongMia, 'rt', encoding='utf-8') as tong:
                return json.load(tong)
        except (FileNotFoundError, JSONDecodeError):
            kiatko = cls._sng()
            with open(cls.tongMia, 'wt', encoding='utf-8') as tong:
                json.dump(
                    kiatko, tong,
                    ensure_ascii=False, indent=2, sort_keys=True,
                )
            return kiatko

    @classmethod
    def _sng(cls):
        miakiatko = {}
        with urlopen(cls.甘字典網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    if row['word'].strip()[0].isupper():
                        臺羅 = row['word'].strip().strip('-').lower()
                        漢字 = row['chinese'].strip()
                        if len(漢字) == 1:
                            miakiatko[漢字] = (
                                拆文分析器.建立字物件(臺羅)
                                .轉音(白話字, '轉換到臺灣閩南語羅馬字拼音')
                                .轉音(臺灣閩南語羅馬字拼音, '轉調符')
                                .看語句()
                            )

        senn的屬性 = set()
        with urlopen(cls.詞目總檔屬性網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    屬性 = row['屬性'].strip()
                    if '百家姓' in 屬性:
                        senn的屬性.add(row['編號'].strip())
        miabuaih屬性 = set()
        with urlopen(cls.詞目總檔文白網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    屬性 = row['屬性'].strip()
                    if '白' in 屬性:
                        miabuaih屬性.add(row['編號'].strip())

        sennkiatko = {}
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in sorted(
                    DictReader(資料),
                    key=lambda x: x['文白屬性'], reverse=True
                ):
                    if row['屬性'].strip() in senn的屬性:
                        臺羅 = row['音讀'].strip().split('/')[0]
                        漢字 = row['詞目'].strip()
                        if 臺羅:
                            sennkiatko[漢字] = 臺羅
                    elif row['文白屬性'].strip() not in miabuaih屬性:
                        臺羅 = row['音讀'].strip().strip('-').split('/')[0].lower()
                        漢字 = row['詞目'].strip()
                        if 臺羅 and len(漢字) == 1:
                            miakiatko[漢字] = 臺羅
        return miakiatko, sennkiatko


sennPio = Pio.senn()
miaPio = Pio.mia()
