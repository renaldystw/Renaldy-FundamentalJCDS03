# ----------------------2-------------------------

peopleInLine = [25, 25, 50, 50, 100]


def tickets(peopleInLine):
    kembalian = peopleInLine[0]
    for x in range(1, len(peopleInLine)):
        # IF INI JIKA PEMBAYARAN MENGGUNAKAN UANG PAS
        if peopleInLine[x] == 25:
            kembalian += peopleInLine[x]
            # print(kembalian, ' uang pas')
        # ELSE INI JIKA PEMBAYARAN MENGGUNAKAN UANG TIDAK PAS
        else:
            # if x == (len(peopleInLine)-1):
                # return print("YES HE CAN")
            calculate = peopleInLine[x] - 25
            if calculate > kembalian:
                return print("NO! HE CAN'T")
            kembalian -= calculate
            # print(kembalian, ' kembalian')
    print("YES! HE CAN")


tickets(peopleInLine)
