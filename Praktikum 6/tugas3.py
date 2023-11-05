#Tugas 3
#Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini
#*
#**
#***
#****

string = " "
bar = 1

x = int (input("masukan angka = "))

while bar <= x:
    kol = bar

    while kol >= 0:
        string = string + "*"
        kol = kol - 1
    string = string + " "
    bar =  bar +1
    print(string)