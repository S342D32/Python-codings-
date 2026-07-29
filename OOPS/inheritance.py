class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car stopped...")
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("Prius","Electric")
print(car1.name)
print(car1.type)
car1.start()
car1.stop()
