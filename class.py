class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + "has sitted")

    def roll_over(self):
        print(self.name + " is rolling over")

dog = Dog('a',23)
dog.roll_over()

#子类
class LittleDog(Dog):

    def __init__(self, name, age):
        super.__init__(name,age)

#重写父类方法，在子类中定义一样名称的方法

