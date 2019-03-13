# -------------------1-----------------------------


# p0 = 1500
# percent = 5
# aug = 100
# p = 5000


# def nb_year(p0, percent, aug, p):
#     looping = True
#     tahun = 0
#     percent = percent / 100
#     while looping == True:
#         calculate = p0 + (p0*percent) + aug
#         p0 = calculate
#         tahun += 1
#         if p0 >= p:
#             looping = False
#             print(tahun, 'Years')


# nb_year(p0, percent, aug, p)

# ----------------------2-------------------------

# peopleInLine = [25, 25, 25, 100, 25, 50]


# def tickets(peopleInLine):
#     kembalian = peopleInLine[0]
#     for x in range(1, len(peopleInLine)):
#         # IF INI JIKA PEMBAYARAN MENGGUNAKAN UANG PAS
#         if peopleInLine[x] == 25:
#             kembalian += peopleInLine[x]
#             # print(kembalian, ' uang pas')
#         # ELSE INI JIKA PEMBAYARAN MENGGUNAKAN UANG TIDAK PAS
#         else:
#             # if x == (len(peopleInLine)-1):
#                 # return print("YES HE CAN")
#             calculate = peopleInLine[x] - 25
#             if calculate > kembalian:
#                 return print("NO HE CAN'T")
#             kembalian -= calculate
#             # print(kembalian, ' kembalian')
#     print("YES HE CAN")


# tickets(peopleInLine)

# ----------------------3-------------------------

# n = int(input('Masukan Angka :'))
# start = 1
# for x in range(0, n+1):
#     for y in range(n, x, -1):
#         print(' ', end='')
#     for z in range(x):
#         print(start, end='')
#         start += 2
#         print(' ', end='')
#     print('')


# def rowSumOddNumbers(n):
#     start = 1
#     sumOddNum = 0
#     for x in range(0, n+1):
#         for z in range(x):
#             if x == (n):
#                 print(start,  end='')
#             start += 2
#             print(' ', end='')
#     for i in range(n):
#         start -= 2
#         sumOddNum += start
#         # print(start)
#         if i == (n - 1):
#             return print(' = ', sumOddNum)


# rowSumOddNumbers(int(input('Which row do you want to count? ')))
