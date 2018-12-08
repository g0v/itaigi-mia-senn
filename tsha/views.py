from tsha.pio import sennPio, miaPio
from django.http.response import JsonResponse


def kaibin(request, senn, mia):
    return JsonResponse({
        'Senn': tsaSenn(senn),
        'Mia': tsaMia(mia),
    })


def tsaSenn(senn):
    if senn in sennPio:
        return sennPio[senn]
    sootsai = 0
    kiatko = []
    while sootsai < len(senn):
        siang = senn[sootsai:sootsai + 2]
        koo = senn[sootsai:sootsai + 1]
        if siang in sennPio:
            kiatko.append(sennPio[siang])
            sootsai += 2
        elif koo in sennPio:
            kiatko.append(sennPio[koo])
            sootsai += 1
        else:
            kiatko.append(tsaMia(koo))
            sootsai += 1
    return '-'.join(kiatko)


def tsaMia(mia):
    kiatko = []
    for ji in mia:
        if ji in miaPio:
            kiatko.append(miaPio[ji])
        else:
            kiatko.append('?')
    siongbue = '-'.join(kiatko)
    return siongbue[:1].upper() + siongbue[1:]
