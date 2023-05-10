class Vehicle:
    serial = ""
    license = ""
    def turnOnAirConditioner(self):
        print("Turn on Air")

class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class Pickup(Vehicle):
    pass


pickup1 = Pickup()
pickup1.turnOnAirConditioner()

car1 = Car()
car1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()