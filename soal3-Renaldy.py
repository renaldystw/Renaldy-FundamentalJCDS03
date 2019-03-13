# ----------------------3-------------------------

n = int(input('Masukan Angka :'))
start = 1
# FOR INI UNTUK PRINT SEGITIGA
for x in range(0, n+1):
    for y in range(n, x, -1):
        print(' ', end='')
    for z in range(x):
        print(start, end='')
        start += 2
        print(' ', end='')
    print('')


def rowSumOddNumbers(n):
    start = 1
    sumOddNum = 0
    for x in range(0, n+1):
        for z in range(x):
            if x == (n):
                print(start,  end='')
            # MENAMBAH KELIPATAN ODD NUMBER
            start += 2
            print(' ', end='')
    # FOR UNTUK MENGHITUNG ROW YANG DIPILIH
    for i in range(n):
        start -= 2
        sumOddNum += start
        # print(start)
        if i == (n - 1):
            return print(' = ', sumOddNum)


rowSumOddNumbers(int(input('Which row do you want to count? ')))
