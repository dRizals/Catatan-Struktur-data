dic={'nama': 'rizal','email': 'rizal.com'}#key : value
print(dic)
print()

print(dic['email'])#mengakses data melalui key nya
print()

dicbaru={'telp': '0321'}
dic.update(dicbaru)#untuk menambah data
print(dic)
print()

dic['telp']= '0853'#mengubah value
print(dic)
del dic['telp']#menghapus data
print(dic)
