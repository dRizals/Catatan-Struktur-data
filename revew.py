#menampilkan bilangan ganjil denran while
num=int(input('masukkan bilangan= '))
count=1
i=0
while count<=num:
    if i%2==1:
        print(count,i)
        count=count+1
    i=i+1
    
#menampilkan bilangan genap dengan for
angka=int(input('masukkan angka= '))

for i in range(angka):
    if i%2==0:
        print(i)


#menghitung faktorial
x=int(input('masukkan angka= '))
fak=1
for i in range(1,x+1):
    fak=fak*i
print(x,'=', fak)


    
