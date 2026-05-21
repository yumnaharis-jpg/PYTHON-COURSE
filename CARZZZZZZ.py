class BMW:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"BMW {self.year} {self.model}")
class FERRARI():
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"FERRARI {self.year} {self.model}")
object1= BMW(year=2020, model="X5")
object2= FERRARI(year=2020, model="SF90")
object1.display_info()
object2.display_info()