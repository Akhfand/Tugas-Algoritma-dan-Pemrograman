#tugas ali kayanya 2 piramid
tinggi = int(input("Mau seberapa tinggi kak: "))

for i in range(tinggi):
    for k in range(2 * i + 1):
        print ('*', end='')
    for j in range(tinggi - i - 1):
        print (' ', end='')
    print()

