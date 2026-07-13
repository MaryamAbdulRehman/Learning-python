# 
# Chapter 4 : Lists
# 

# List:
# List Python ka aik built-in data type ha.
# List aik container ki tarha hoti ha jis ma hum multiple values store kar sakty hain.
# Aik list ma different data types bhi store kar sakty hain.
# Example:
# ["Mango", 25, 5.5, True]

fruits = ["Mango", "Apple", "Banana"]

print(fruits)

# 
# List Indexing
# 

# Indexing hamesha 0 sa start hoti ha.

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative Indexing

print(fruits[-1])

# 
# List Slicing
# 

# Slicing ka use list ka kuch specific part access karny k liye hota ha.

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[0:4])
print(numbers[2:6])
print(numbers[::2])

# 
# Updating List
# 

# Lists mutable hoti hain.
# Yani hum values ko change kar sakty hain.

fruits[1] = "Cherry"

print(fruits)

# 
# List Methods
# 

# append()
# List k end ma new item add karta ha.

fruits.append("Orange")

print(fruits)

# insert()
# Kisi specific index pa value insert karta ha.

fruits.insert(1, "Guava")

print(fruits)

# remove()
# Kisi specific value ko remove karta ha.

fruits.remove("Apple")

print(fruits)

# pop()
# Default last item remove karta ha.

fruits.pop()

print(fruits)

# reverse()
# List ko ulta kar deta ha.

fruits.reverse()

print(fruits)

# sort()
# Numbers ko ascending order ma arrange karta ha.

numbers = [45, 12, 78, 3, 99]

numbers.sort()

print(numbers)

# len()
# Total items count karta ha.

print("Total Items:", len(fruits))

#
# Mutable vs Immutable
#

# List mutable hoti ha.
# Is liye hum list ki values change kar sakty hain.

fruits[0] = "Strawberry"

print(fruits)

#
# Real Life Example
#

# Shopping Cart aik list ki tarha hota ha.
# Hum products add bhi kar sakty hain aur remove bhi.

cart = ["Milk", "Bread", "Eggs"]

cart.append("Juice")

print(cart)


# Practice Question 1


# User sa 5 fruits input lain aur list ma store karain.

items = []

for i in range(5):
    fruit = input("Enter Fruit Name: ")
    items.append(fruit)

print(items)


# Practice Question 2
# 

# User sa 5 students k marks lain aur sort karain.

marks = []

for i in range(5):
    mark = int(input("Enter Marks: "))
    marks.append(mark)

marks.sort()

print(marks)

# 
# Practice Question 3
# 

# List ka sum, maximum aur minimum print karain.

nums = [12, 44, 6, 90, 23]

print("Sum =", sum(nums))
print("Maximum =", max(nums))
print("Minimum =", min(nums))

# 
# Practice Question 4
# 

# Sirf even numbers new list ma store karain.

even_numbers = []

for number in nums:

    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# 
# Practice Question 5
# 

# Sab sa bara number manually find karain.

greatest = nums[0]

for number in nums:

    if number > greatest:
        greatest = number

print("Greatest Number:", greatest)

# 
# Practice Question 6
# 

# Sab sa chhota number manually find karain.

smallest = nums[0]

for number in nums:

    if number < smallest:
        smallest = number

print("Smallest Number:", smallest)

# 
# Practice Question 7
# 

# User ka name list ma mojood ha ya nahi.

students = ["Ali", "Maryam", "Amna", "Fatima"]

name = input("Enter Your Name: ")

if name in students:
    print("Name Found")
else:
    print("Name Not Found")

# 
# Practice Question 8
# 

# List ko reverse order ma print karain.

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)