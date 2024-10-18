class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
  
autobus=Transport('Renault Logan',180,12)

print (f"The name of the car:{autobus.name}.\
 Speed:{autobus.max_speed}. Mileage:{autobus.mileage}")
