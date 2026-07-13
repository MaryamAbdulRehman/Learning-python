# 
# Conditional Statements
# 

age=int(input("Enter age: "))
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")

marks=int(input("Enter marks: "))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Fail")

# Practice 1
a=int(input("First: "))
b=int(input("Second: "))
c=int(input("Third: "))

greatest=a
if b>greatest:
    greatest=b
if c>greatest:
    greatest=c
print("Greatest:",greatest)

# Practice 2
eng=int(input("English: "))
math=int(input("Math: "))
phy=int(input("Physics: "))
per=(eng+math+phy)/3
if per>=40 and eng>=33 and math>=33 and phy>=33:
    print("Pass")
else:
    print("Fail")

# Practice 3
msg=input("Message: ")
if "buy now" in msg or "click here" in msg:
    print("Spam")
else:
    print("Safe")

# Practice 4
username=input("Username: ")
if len(username)<10:
    print("Valid")
else:
    print("Too Long")
