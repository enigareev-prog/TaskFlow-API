class Dog:
    def __init__(self, name):
        self.name = name


dog1 = Dog(input("Enter dog 1's name: "))
dog2 = Dog(input("Enter dog 2's name: "))

print(dog1.name)
print(dog2.name)