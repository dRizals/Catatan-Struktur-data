buah=['apel', 'nanas', 'jeruk']#variabel buah yg berisi list
print(buah)
buah=buah+['anggur']#menambah data list dalam buah
print(buah)
print(buah[1])#menampilkan data dari indeks list(indeks dimulai dari 0)
print()

for i in buah:#menampilkan data urut ke bawah
    print (i)
print()

buah[0]='mangga'#mengubah data
print(buah)
del buah[3]#menghapus data, del juga bisa untuk menghapus variabel
print(buah)
print(len(buah))#menampilkan jumlah/panjang data
print()

#menampilkan data dengan nomor urut
vokal=['a', 'i', 'u', 'e', 'o']
n=len(vokal)
for i in range(1,n):#range 1 sampai banyak/panjang data(n)
    print("{}. {}".format(i, vokal[i]))#biar ada (.) setelah nomor
print()

angka=[8,7,3,5,4,9,2]
print(angka)
print(min(angka))#mnampilkan angka terendah
print(max(angka))#sebaliknya

