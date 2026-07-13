
# Begineers Code

names=["Hamna","Hanan","Haani"]
marks=[70,80,90]
for i in range(len(names)):
    print(names[i],marks[i])

# Zip multiples items list ma sa la kar unn ko pair up karay ga

'''Yahan zip aik value name ma sa la ra aur aik numbers ma sa aur dono ko same time pa zip kar raha 
Zip function ka use tab karna ha jab humy pata ho k data aik dosre sa relatable ha.Agar relatable 
nahi to humy zip function use nahii karna
'''

name=["Sania","Sana","Seerat"]
numbers=[90,98,99]
for naam, number in zip(name,numbers):
    print(naam,number)

# Second thing is   Unzip
'''
Unzip is just a concept not a function.Iss ka matlab paired data ko lena ha aur uss ko separate
kar ky wapis bhaj dena ha into individual list

'''

data=[("nimra",80),("noreen",90),("naila",50)]
names,marks=zip(*data) 
print(list(names))
print(type(marks))
"""zip yahan pa reverse operation karay ga yaani jo pehly items hain inn ko alag rakh da ga aur marks ko alag
zip(*data) ---->Ya jo pehly number pa items hain unn ko aik list ma la aye ga like:["nimra","noreen","naila"]
Iss k baad jo numbers hain unn ko lag list ma la aye ga.[80,90,50]"""
