from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def features(self, name, fuel, seating, speed):
        pass


class AUDI(Car):

    def show(self):
        print("I AM AUDI CAR")

    def features(self, name, fuel, seating, speed):
        print("Car Name :", name)
        print("Fuel Type :", fuel)
        print("Seating Capacity :", seating)
        print("Max Speed :", speed, "km/h")


class VOLVO(Car):

    def show(self):
        print("I AM Volvo CAR")

    def features(self, name, fuel, seating, speed):
        print("Car Name :", name)
        print("Fuel Type :", fuel)
        print("Seating Capacity :", seating)
        print("Max Speed :", speed, "km/h")


c1 = AUDI()
c1.show()
c1.features("AUDI", "Petrol", 5, 180)


c2 = VOLVO()
c2.show()
c2.features("VOLVO", "Diesel", 5, 200)
