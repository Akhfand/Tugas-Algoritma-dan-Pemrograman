#Tugas perulangan (for)
ulang = int(input("Jumlah mahasiswa: "))

uts = []
uas = []

for i in range(ulang):
    print ("data ke- ", (i+1))
    nim = input("Masukan nim anda: ")
    uts.append(int(input("Masukan nilai uts anda: ")))
    uas.append(int(input("Masukan nilai uas anda: ")))
    print ("nim adalah %s nilai uts anda %i nilai uas anda %i"% (nim,uts[i],uas[i]))
    print ("---------------------------\n")

rata_uts = sum(uts) / ulang
rata_uas = sum(uas) / ulang

print ("Rata - rata nilai uts mahasiswa sebesar %i"% (rata_uts))
print ("Rata - rata nilai uas mahasiswa sebesar %i"% (rata_uas))



