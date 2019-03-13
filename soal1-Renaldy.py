# -------------------1-----------------------------
p0 = 1500000
percent = 2.5
aug = 10000
p = 2000000


def nb_year(p0, percent, aug, p):
    looping = True
    tahun = 0
    percent = percent / 100
    while looping == True:
        calculate = p0 + (p0*percent) + aug
        p0 = calculate
        tahun += 1
        if p0 >= p:
            looping = False
            print(tahun, 'Years')


nb_year(p0, percent, aug, p)
