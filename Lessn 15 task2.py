class Transport(object):
   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
   def seating_capacity(self, capacity):

       return print(f"Вместимость одного автобуса", self.name,  capacity, "пассажиров")
class Autobus(Transport):
    def __init__(self,n,ms,ml):
        super().__init__(n,ms,ml)
auto=Autobus("Renault Logan",180,2)    
auto.seating_capacity(50)