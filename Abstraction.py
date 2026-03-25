from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(r):
        pass

class SBI(RBI):

    def show(self):
        print("I AM SBI")
    def roi(self,r):
        print("Rate Of Intereste Given By SBI Is : ",r)

class HDFC(RBI):

    def show(self):
        print("I AM HDFC")
    def roi(self,r):
        print("Rate Of Intereste Given By HDFC Is : ",r)

s1=SBI()
s1.show()
s1.roi(6.5)
h1=HDFC()
h1.show()
h1.roi(6.9)
