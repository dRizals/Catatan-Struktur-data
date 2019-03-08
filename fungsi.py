def loop():#membuat fungsi bernama loop tanpa argumen/parameter
    for i in range(0,10):
        print(i)
loop()#untuk memanggil fungsi yg dibuat
print()

def perulangan(n):#fungsi dengan argumen
    for i in range(1,n+1):# +1 biar pas 10
        print(i)
perulangan(10)#isi argumen saat memanggil fungsi
print()

def data(x,y,z):
    print('.:MyData:.')
    print('Nama: ', x)
    print('NIM: ', y)
    print('Prodi: ', z)

nama= input('Nama: ')#data inputan
nim= input('NIM: ')
prodi= input('Prodi: ')

data(nama,nim,prodi)#argummen dari data inputan
print()

def luas(a,t):
    return (a*t)/2#return untuk memproses/menghitung tapi tidak untuk menampilkan
print('luas segitiga = {} m**'.format(luas(3,4)))
#menggunakan print untuk menampilkan hasil dari return,
print()


