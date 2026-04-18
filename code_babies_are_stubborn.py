class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
        self.distance = int(input("Enter distance the you are going in km : "))

   
   
    def fare(self):
        return self.capacity * self.distance * 0.1
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
    def fare(self):    
        base_fare = super(). fare()
        maintenance_charge = base_fare * 0.1
        total_fare = base_fare + maintenance_charge
        return total_fare
bus = Bus(50)
print("Total Bus fare is:", bus.fare())    

    