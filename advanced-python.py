  # Advanced Python   List compression

# numbers=[1,2,3,4,5,6]
# squares=[i*i for i in numbers]
# print(squares)

# Another way

num=[1,2,3,4,5,6,7]
squares=[]
for i in num:
    square=i*i
    squares.append(square)

# 2nd Program
# Even Numbers
number=[2,4,3,5,6,7,8,90,80,60,44]
even=[]
for i in number:
    if i % 2==0:
        even.append(i)
print(even)


# Odd numbers

num2=[2,3,4,23,21,65,78,97,55,20,60,8]
odd=[]
for i in num2:
    if i%2!=0:
        print(i)
        odd.append(i)
print(odd)

# Another way to write a program
num4=[2,3,4,23,21,65,78,97,55,20,60,8]
oddd=[i for i in num4 if i%2!=0]
print(oddd)

# 3rd program
# Print table 5


# num3=[1,5,2,10,15,20,25,6,9,30,35,40,45,50,44]
# five=[]
# for i in num3:
#     if i%5==0:
#         print(5 ,"x" ,i ,"=" ,five)
#         five.append(i)
#         i+=1
# print(five)

# Program

names=["maryam","maira","maria","mehmal"]
result=[]
for i in names:
    result.append(i.upper())
print(result)

# Another way

naam=["Maneeha","maryam","maira","maria","mehmal","Maliha"]
result=[i.upper() for i in naam]
print(result)



# Enumerate function
names_1=["ania","anaya","amna","alia","alina"]
for i in range(len(names_1)):
    print(i,names_1[i])

    # Shortcut  using enumerate

    # Enumerate Syntax:  for index , name in enumerate(list):    #Ya 2no cheezain nikal k da dega
# Enumerate Function: Position number aur value aik saath return karta ha enumerate.
# Jab aik list par loop chal raha hota ha to enumerate uss ka index number bhi nikal kar return kar dega 

name_2=["ania","anaya","amna","alia","alina","samiya","saman"]
for index , i in  enumerate(name_2,start=1):    #Agar 1 sa start karna ha index no.
    print(i,index)


