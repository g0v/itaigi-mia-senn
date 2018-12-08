from csv import DictReader
import io
import json
from json.decoder import JSONDecodeError
from urllib.request import urlopen


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
    tongMia = 'senn.json'

    @classmethod
    def senn(cls):
        try:
            with open(cls.tongMia, 'rt', encoding='utf-8') as tong:
                return json.load(tong)
        except (FileNotFoundError, JSONDecodeError):
            kiatko = cls._senn()
            with open(cls.tongMia, 'wt', encoding='utf-8') as tong:
                return json.dump(
                    kiatko, tong,
                    ensure_ascii=False, indent=2, sort_keys=True,
                )
            return kiatko

    @classmethod
    def _senn(cls):
        會使的屬性 = set()
        with urlopen(cls.詞目總檔屬性網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    屬性 = row['屬性'].strip()
                    if '百家姓' in 屬性:
                        會使的屬性.add(row['編號'].strip())
        kiatko = {}
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    if row['屬性'].strip() not in 會使的屬性:
                        continue
                    臺羅 = row['音讀'].strip()
                    漢字 = row['詞目'].strip()
                    kiatko[漢字] = 臺羅
        return kiatko


sennPio = Pio.senn()
