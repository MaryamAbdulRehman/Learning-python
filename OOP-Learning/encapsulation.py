class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance   #private variable
acc1=Bank("Maryam",10000000000)
acc2=Bank("Abdullah",5000000000000)
# acc1.balance=200000000000
print(acc1.name,acc1.__balance)
'''
Ab ya bank account ha iss ma agr hum khud sa hii update karny lag jaaye
to ya boht barra bug ha iss tarha hum khud sa apna balance update ni kar
sakty iss k liye ya to humy deposit ya withdraw karna parray ga.....Ab
hum iss balance ko private banaa dain gy k har koi modify na kar sakay
'''