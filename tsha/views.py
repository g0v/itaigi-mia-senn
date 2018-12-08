from tsha.pio import sennPio


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
            kiatko.append('?')
            sootsai += 1
    return '-'.join(kiatko)
