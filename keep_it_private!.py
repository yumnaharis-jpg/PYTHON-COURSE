


class myClass:                  
    __privateVar= 27;
    def __privateMethod(self):
        print("i'm inside class myClass")
    def hello(self):
       print("private variable value:", self.__privateVar)
foo =myClass()
foo.hello()
foo.__privateMethod()

#keep your secrets private...im telling you from experience...




