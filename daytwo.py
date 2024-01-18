# class Robot:
#     new_var= "this is token"

# robot = Robot()
# print(robot.new_var)

# #constructor

# class Fruit:
#     def __init__(self, name:str, price:int):
#         self.name = name
#         self.price =price

#     def __str__(self) -> str:
#         return f"this fruit is {self.name} and price is { self.price} "
    

#     def getFruitvalue(self):
#         return " this is fruit value function"

# fruit = Fruit("apple",41)
# fruit2 = Fruit("mango",56)
# print(fruit)
# print(fruit2)
# print(fruit.getFruitvalue())

#inheritence
class Music:
    def playMusic():
        return" music has beeen started"
    
class Guitar(Music):
    def guitarMusic(self):
        return "jhing jhing"

guitar = Guitar()
print(guitar.guitarMusic())



#static method
class staticExample():
     @staticmethod
     def guitarMusic():
         return "jhing jhing"
print(staticExample.guitarMusic())
    
        