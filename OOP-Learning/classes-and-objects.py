"""
Class:
      It is just a blueprint(naqsha)
Object:
       Ya aik real instance hota ha jo hum class sa create karty hain
__init__:
         Data store karny k liye ya special method use hota  aur iss ka
         matlab ha initialize the object
 
"""

# Blueprint---Aur ya instance variable ha
class student:
    def __init__(self,name,marks,attendance):
        self.name=name
        self.marks=marks
        self.attendance=attendance

# Class k andar function define kar rahay hain to iss ko methods kahain gy functions nahii kahain gy
# Agar class k bahir koi function define kar ry hain to wo function hii hoga

# Ab ya class k andar method define kar rahay hain hum
    def calculate_grade(self):


       if self.marks>=90:
        return "A"
       elif self.marks>=75:
        return"B"
       else:
        return "C"
# Object create hoga ab using class
s1=student("Maryam",1000,90)
# s2=student("Zunaira",1025,95)
# s3=student("Zumar",1090,80)
print(s1.calculate_grade())
# print(s2)
# print(s3)
# print(s1.name)
# print(s2.name)
# print(s3.name)


'''
Ab instance aur class variable use ho ra
Instance Variable:
                  Init ka use using self ya instance variable ha.
                  It is belong to object
                  Aur har object k liye alag alag hoga
Class Variable:
              Jo outside init define hoty hain aur jo saary objects ma shareable hoty hain
              It is belong to class itself
              Sabhi objects k liye same hoga
Iss ka use:
           Jab object kaafi common ha aur ya shareable to all ha yaani kaafi students ka school same hota ha
'''







