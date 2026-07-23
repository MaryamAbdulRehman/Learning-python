'''
A single class has multiple objects or has multiple instances
'''

class Bags:
    name="Girly bag"
    def details():
        print("This is a girlies bag")
# ya ha object ban gaya
leather=Bags()
strip=Bags()
# pehly hum asy acess karty thy
print(Bags.name)
# lakin jab humny object bana liya to hum object k name sa acess karain .
print(leather.details) #jis bhi object ko access karain gy output aye ga 
print(strip.name)
