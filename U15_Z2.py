class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self,capacity):
    #def seating_capacity(self):
        return print (f"Capacity of one bus {self.name} {capacity} passengers")
        #return print (f"Capacity of one bus {self.name} {self.capacity} passengers")

class Autobus(Transport):
    capacity=50 
    #def __init__(self, name, max_speed, mileage, capacity):
    #    super().__init__(name=name,max_speed=max_speed,mileage=mileage)
    #    self.capacity=capacity
       
a1=Autobus('Renault Logan',180,12)
a1.seating_capacity(20)
print (a1.capacity)
