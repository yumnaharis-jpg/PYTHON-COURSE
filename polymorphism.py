class Iran():
    def language(self):
        return "Persian"
    
    def capital(self):
        return "Tehran"
    
    def population(self):
        return "83 million" 
class USA():
    def language(self):
        return "English"
    
    def capital(self):
        return "Washington D.C."
    
    def population(self):
        return "331 million"
object1 = Iran()
object2 = USA()
for obj in (object1, object2):
    print(obj.language())
    print(obj.capital())
    print(obj.population())
