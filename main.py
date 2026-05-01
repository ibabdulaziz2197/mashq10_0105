# 1
class Transport:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def move(self):
        print(f"Transport {self.speed} tezlikda {self.fuel} yoqilgi bilan harakat")



class Car(Transport):
    def __init__(self, brand, speed, fuel, color):
        super().__init__(speed, fuel)
        self.brand = brand
        self.color = color


    def move(self):
        super().move()
        print(f"Car {self.brand}, rang: {self.color}")



m1 = Car(brand="BMW", speed=150, fuel=30, color="Qora")
m1 = move()


# 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Ism: {self.name}, Yosh: {self.age}, Jins: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, grade, university):
        super().__init__(name, age, gender)
        self.grade = grade
        self.university = university

    def introduce(self):
        super().introduce()
        print(f"Kurs: {self.grade}, Universitet: {self.university}")


s = Student("Ali", 20, "Erkak", 2, "TATU")
s.introduce()


# 3
class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        return f"{self.name} ovqat yeyapti"


class Dog(Animal):
    def __init__(self, name, age, type, breed, color):
        super().__init__(name, age, type)
        self.breed = breed
        self.color = color

    def eat(self):
        parent_text = super().eat()
        return parent_text + " va tez yeyapti"

    def bark(self):
        return "It hurmoqda"

d = Dog("Rex", 3, "sut emizuvchi", "Ovcharka", "qora")

print(d.eat())
print(d.bark())

# 4
class Employee:
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def work(self):
        return f"{self.name} ishlamoqda"


class Manager(Employee):
    def __init__(self, name, salary, experience, department, team_size):
        super().__init__(name, salary, experience)
        self.department = department
        self.team_size = team_size

    def work(self):
        parent_text = super().work()
        return parent_text + f"\nManager {self.department} bo‘limini boshqarmoqda"

m = Manager("Ali", 5000, 5, "IT", 10)

print(m.work())

# 5
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        return "Shakl yuzasi aniqlanmagan"


class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        parent_text = super().area()
        calculated_area = self.width * self.height
        return f"{parent_text}\nTo‘g‘ri to‘rtburchak yuzasi: {calculated_area}"


r = Rectangle("To‘g‘ri to‘rtburchak", "qizil", 5, 4)

print(r.area())
