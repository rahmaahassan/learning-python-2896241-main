#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    
    def drive(self, speed):
        self.mode = 'driving'
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetypr):
        super().__init__('Car')
        self.wheels = 4
        self.doors = 4
        self.enginetypr = enginetypr
    
    def drive(self, speed):
        super().drive(speed)
        print('Driving my', self.enginetypr, 'car at', self.speed)

class Motocycle(Vehicle):
    def __init__(self, enginetypr, hassidecar):
        super().__init__('Motocycle')
        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetypr = enginetypr
    
    def drive(self, speed):
        super().drive(speed)
        print('Driving my', self.enginetypr, 'motocycle at', self.speed)

car1 = Car('gas')
car2 = Car('electric')     
mc1 = Motocycle('gas', False)

print(car1.enginetypr)
print(mc1.wheels)
print(car2.wheels)

car1.drive(30)
mc1.drive(50)