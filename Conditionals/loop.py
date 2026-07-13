# 
# Loops
#

# range number generate karta ha.
for i in range(1,6):
    print(i)

# Even numbers
for i in range(2,21,2):
    print(i)

# Table
num=int(input("Enter number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

# While loop
i=1
while i<=5:
    print(i)
    i+=1

# Break
for i in range(1,11):
    if i==6:
        break
    print(i)

# Continue
for i in range(1,11):
    if i==6:
        continue
    print(i)

# Practice 1
total=0
for i in range(1,101):
    total+=i
print(total)

# Practice 2
fact=1
n=int(input("Enter number: "))
for i in range(1,n+1):
    fact*=i
print(fact)

# Practice 3

# List ma sab sa bara number find karain.
nums=[3,77,12,90,45]
greatest=nums[0]
for x in nums:
    if x>greatest:
        greatest=x
print(greatest)

# 
# Practice 4
# 

# 1 sa 50 tak sirf odd numbers print karain.

for number in range(1, 51, 2):
    print(number)


# 
# Practice 5
# 

# User sa aik number lain aur uss ka table reverse order ma print karain.

number = int(input("Enter your number: "))

for table in range(10, 0, -1):
    print(f"{number} x {table} = {number * table}")

# 
# Practice 6
# 

# 1 sa 10 tak numbers ka square print karain.

for number in range(1, 11):
    print(number, "Square =", number ** 2)


# 
# Practice 7
# 

# List ma jitny bhi even numbers hain unko count karain.

numbers = [12, 45, 67, 88, 90, 13, 24]

count = 0

for number in numbers:

    if number % 2 == 0:
        count += 1

print("Total Even Numbers:", count)


# 
# Practice 8
# 

# List ma jitny bhi odd numbers hain unko count karain.

numbers = [12, 45, 67, 88, 90, 13, 24]

count = 0

for number in numbers:

    if number % 2 != 0:
        count += 1

print("Total Odd Numbers:", count)


# 
# Practice 9
# 

# User sa aik word lain aur uss ka har character alag alag print karain.

word = input("Enter any word: ")

for character in word:
    print(character)

# 
# Practice 10
# 

# String ma vowels count karain.

sentence = input("Enter a sentence: ")

vowels = 0

for character in sentence.lower():

    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        vowels += 1

print("Total Vowels:", vowels)


# 
# Practice 11
# 

# List ma sab sa chhota number find karain.

numbers = [45, 11, 98, 23, 5, 67]

smallest = numbers[0]

for number in numbers:

    if number < smallest:
        smallest = number

print("Smallest Number:", smallest)


# 
# Practice 12
# 

# Countdown print karain.

for number in range(20, 0, -1):
    print(number)

print("Blast Off ")


# 
# Practice 13
# 

# break ka use.
# Jaisy hii 7 aaye loop ko wahii rok dain.

for number in range(1, 11):

    if number == 7:
        break

    print(number)


# 
# Practice 14
# 

# continue ka use.
# Sirf number 5 ko skip karna ha.

for number in range(1, 11):

    if number == 5:
        continue

    print(number)


# 
# Practice 15
# 

# pass ka use.
# Abhi condition ma koi kaam nahi karna.

for number in range(1, 6):

    if number == 3:
        pass

    print(number)


# 
# Practice 16
# 

# Star Pattern

for row in range(1, 6):
    print("*" * row)


# 
# Practice 17
# 

# Reverse Star Pattern

for row in range(5, 0, -1):
    print("*" * row)


# 
# Practice 18
# 

# 1 sa 100 tak jitny numbers 5 sa divide hoty hain wo print karain.

for number in range(1, 101):

    if number % 5 == 0:
        print(number)


# 
# Practice 19

# User sa 5 numbers input lain.
# Phir unka total calculate karain.

total = 0

for value in range(5):

    number = int(input("Enter Number: "))

    total += number

print("Total Sum:", total)


# 
# Practice 20
# 

# List ma kisi number ko search karain.

numbers = [12, 45, 67, 89, 100, 23]

search_number = int(input("Enter number to search: "))

found = False

for number in numbers:

    if number == search_number:
        found = True
        break

if found:
    print("Number Found")
else:
    print("Number Not Found")