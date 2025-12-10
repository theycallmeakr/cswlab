class myclass:
    def __init__(self):
        self.__private_variable = "this is prvate"
    def __private_method(Self):
        return "this is private"
    def display(self):
        return f"accessing private variable: {self.__private_variable}, and private method {self.__private_method()}"
    
obj=myclass()
print("print")
print(obj.display())



