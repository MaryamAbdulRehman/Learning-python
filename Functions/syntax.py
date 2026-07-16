'''Function: print vs return
Reusable block of code ha.
Iss ko define karain gy 'def' kii help saya input la ga apny andar phir value ko hum use karain gy
return:ka use kar rahy hain to variable create karna ha 
print:ka use kar ry hain to variable create karny kii zarorat nahii

'''
"""def function_name(parameters):
    pass
    """
def greet(name):
    print("Hello",name)
greet("mariya")


def square(x): 
    return x*x  # return value ko store karega jo hum agy jaa k reuse kar sakty hain
                # return use karny k liye aik variable create karna ha
                # phr =(assignment operator) use karky phr function ko call karna ha
x=square(6)
print(x)   #print just content ko display karega

# Parmeters  and  Arguments
'''
def greet(name)---Yahan jo name ha wo parameter ha.Yani parameter wo jo function kii
definition k andar hoga.Ya bahir sa value recieve karega
Parameter is like placeholder value..Aur value argument sa aye gii

"Rania" ------Ya argument ha
Argument:Ya actual value jo tab pass karain gy jab function ko call karain gy

return:iss ka use zaroori nahi k karna hii karna ha..lakin jab humy sure ho k humy value chahiye tab use karna
jab return ka use karna ha to extra variable ko create karna ha aur uss k andar function ko call karna ha.Tab
value return mily giii

Functions are not about the syntax.They are about control over the program.Isse hum decide kar sakty hain k
code ka konsa part chaly ga.aur result wapis la sakty hain

'''

def add(a,b):
    print(a+b)
add(20,16)

'''
Create a function that number n.even numbers from 1 to n.agar 10 ha to 1 to 10 ma jo even numbers aty hain unn ko return karna ha
input 10 ha to even numbers ....2,4,6,8,10 ya milny chahiye yani%2==0 ana chahiye.Aur return karay k 5 mujy even numbers chahiye

1.Ab yahan pa loop chalayen gy jo 1 sa n number tak chalay ga
2.if condition ka use kar k even number ko filter karain gy
3.phr function ka use karain gy to apply this logic
4.phir jo bhi count nikly ga uss ko return kar dain gy 

'''
# Code

def count_even(n):
    count=0   #yahan count ko reset kiya ha yaani 0 sa hii count start hoga
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            count += 1
    return count
result=count_even(10)
print(result)

#==============
# Difference between print and return
#==============w

# print
def add(a,b):
    c=a+b
    print(c)
add(10,16)

# return
def multi(a,b):
    c=a*b
    return f"The multiplication is {c}"
m=multi(4,4)#return ma kuch bhi paas karain to agar wo console pa chahiye to uss k liye aik variable
#bana kar uss k andar uss function(multi) ko store karwaana mandatory ha otherwise output ni aye gii
print(m)
    
#========
# Local Variable / Global Variable
'''Local Variable: Ya wo variable hoty hain jo function k andar define hoty hain hum inn ko function 
k bahir use ni kar sakty.....
Local Variables function k andar hii banty hain aur function k andar hii use hoty hain

Global Variable: Ya function k bahir define karty hain aur function k bahir hii use karty hain
'''
# ======= 
# e.g
def xyz(a,b):
    a=10    #ya yahan define ho chukay hain 2no ab inn ka bahir use ni ho sakta
    b=20
    c=a*b
    return c
d=xyz(10,30)  #ya print nahii hoa
print(d)

# write the program and tells the number is even or odd?

def odd_eve():
    num=int(input("Enter your number= "))
    if num %2==0:
        print("even")
    else:
        print("odd")
    return num
user=odd_eve()
print(user)

# Triangle pattern

def tria():
    lines=int(input("Enter no.of lines ="))
    for i in range(1,lines+1):
        for j in range(i):
            print("*",end=" ")
        print()
    return f"The {lines} numbers of triangle is created"
triangle=tria()
print(triangle)


# Aik program likhain agar marks above 40 hain to paas otherwise Fail

def pf():
    num=int(input("Enter your number= "))
    if(num>=40):
        print("pass")
    else:
        print("fail")
        return num
marks=pf()
print(marks)


'''
default arg
keyword
*args  **kargs

'''
# default argument


def arg(name="maryam"):
    print(name)
arg("Rehman") #agar yahan value paas nahi karty to default value maryam print hotii means jo default argument ha 

# Keyword
# ===========
# Jab function ko call karain to pehly positional argument ayen gy then Keyword argument ayen gy like humain inn
#  ko opar define karna parray ga jesy def intruduce(name,age) agar name age na define kii aur keyword argument
#  pass kar diye to error aye ga

# e.g:

def introduce(name,age):
    print("Name:",name ,"Age:",age)
# introduce(25,"maryam")  #Ab ya asy print ho jaayen gy name ma 25 aur age ma maryam iss issue ko solve  karny k 
# liye hum keyword Argument ka use karain gy just like:

introduce(age=21,name="Maryam")#ya ha keyword argument bina keyword argument k order matter karta ha......iss ma 
# safety k liye keyword argument ka use kiya

'''
Agar hum asy karain k     introduce(name="maryam,age)   to iss ma error aye ga iss ma 2no ko paas karna zaroorii ha
'''


# Argument(*args) and Keyword Argument(**kwargs)
'''
*args iss kii humy zarorat kyun ha?    Iss ma jo * ha ya python ko kah raha ha k jo bhi positional argument aye gii 
uss ko aik container ma rakh loo.like: 10,20,30,40,43,54,23,67 aur ya container phr "tuple" ban jaata ha.phir for 
loop laga k aik aik items ko access kiya aur jo operation perform karny thy wo kiye...

*args items collect 
karay ga in a tuple form

====================
Rules:
*args sirf positional arguments hii collect karta ha...e.g agar hum bolain k hum:add(a=1,v=34) to iss tarha karny sa error aye ga


e.g: Agar asy hota ha function: 
  def greet(a,b)
  return a+b
greet(10,20,30,40,50,60,70,80,90)  hum itni values nahii da sakty jitnii hum chahty hain

iss k liye hum use karty hain   *args like: 

  def add(*numbers):
  total=0
  for n in numbers:
  total+=n
  return total
  print(add(10,20,30,40,50,60,70,80,90))
                                
'''

def add(*numbers):
    total=0
    for n in numbers:
        total+=n
    return total
a=add(10,20,30,40,50,60,70,80,90)
print(a)

'''
**kwargs (keyword arguments)
e.g:pehly hum iss tarha karty thy
def create_user(name,age,class):
print(name,age,class)
create_user("maryam,22,16)    .....Lakin agar humy future ma iss ka aur data chahiye
 like email,contact to humy opar pehly define karna parray ga......iss kaam ko asaan 
 karny k liye hum kwargs use karty hain

 
 keyword argument jitny chahain utny da sakty hain aur ya as a dictionary store hoty hain

 Rules:
 Aur keyword argument keyword arguments hii collect karay ga...
 e.g: def calculate(**amount)
    print(amount)
calculate(100)   ...Hum iss ko iss tarha nahii bhaj sakty agar humny opar double stearic use kiye hain to humy
neechy keyword arguments deny parrain gy like: calculate(price=700,Rs=500,) Things like that
 
 for example
'''
def create_user(**details):
    print(details)

create_user(name=["maryam","maria","mehmal"],age=[40,50,60],email=['maryam@gmail.com','maria@gmail.com','mehmal@gmail.com'])

'''

Summarize Function
Difference b/w *args  and  **kwargs

*args                                                   **kwargs
Ya extra positional argument accept karta               Ya extra keyword argument collect karay ga
As a tuple data store hoga                              Aur ya as a dictionary store hoga

Normal parameters ----> Fixed Inputs
*arguments(*args)-----> Unlimited but unnamed inputs(for loop)
**keyword arguments---> Unlimited named inputs



'''