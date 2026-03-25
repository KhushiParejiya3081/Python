from abc import ABC,abstractmethod

class CAR(ABC):

    @abstractmethod
    def fetures(f):
        pass

class AUDI(CAR):

    def show(self):
        print("This Car is Audi")
    def fetures(self,f):
        print(" Fuel Type : ",f)
    def fetures(self,f):
        print("Seating : ",f)

c1=AUDI()
c1.show()
c1.fetures(5)

#class HDFC(RBI):

    #def show(self):
       # print("I AM HDFC")
   # def roi(self,r):
     #   print("Rate Of Intereste Given By HDFC Is : ",r)

#s1=SBI()
#s1.show()
#s1.roi(6.5)
#h1=HDFC()
#h1.show()
#h1.roi(6.9)
