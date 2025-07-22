# Section 1: Classes and Objects (1–10)

# Task 1: Car class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} costs ${self.price}"


car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)

print(car1.display())
print(car2.display())

# Task 2: BankAccount class
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance


# Task 3: Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


# Task 4: Circle class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Task 5: Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"{self.title} by {self.author}"


# Task 6: Laptop class
class Laptop:
    warranty_period = 2  # shared class variable

    def __init__(self, brand):
        self.brand = brand


# Task 7: Movie class
class Movie:
    count = 0

    def __init__(self, title):
        self.title = title
        Movie.count += 1


# Task 8: Product class
class Product:
    tax_rate = 0.18

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Task 9: Employee with __str__
class Employee:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name} works in {self.dept}"


# Task 10: Rectangle with __eq__
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        return (self.length == other.length and self.breadth == other.breadth)

# Section 2: Inheritance (11–20)

# Task 11: Vehicle Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, wheels=4):
        super().__init__(brand)
        self.wheels = wheels

class Bike(Vehicle):
    def __init__(self, brand, wheels=2):
        super().__init__(brand)
        self.wheels = wheels

class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity


# Task 12: super() constructor
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


# Task 13: Shape with Square and Triangle
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Task 14: Multi-level Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

class Manager(Employee):
    def __init__(self, name, id, team_size):
        super().__init__(name, id)
        self.team_size = team_size


# Task 15: Multiple Inheritance
class Father:
    def skills(self):
        return ["driving", "fishing"]

class Mother:
    def skills(self):
        return ["cooking", "painting"]

class Child(Father, Mother):
    def all_skills(self):
        return Father.skills(self) + Mother.skills(self)


# Task 16: Hierarchical Inheritance
class Teacher:
    def teach(self):
        return "Teaching..."

class MathTeacher(Teacher):
    def subject(self):
        return "Math"

class ScienceTeacher(Teacher):
    def subject(self):
        return "Science"


# Task 17: isinstance()
car = Car("Ford")
print(isinstance(car, Vehicle))  # True


# Task 18: issubclass()
print(issubclass(Truck, Vehicle))  # True


# Task 19: E-commerce Hierarchy
class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, warranty):
        super().__init__(name)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, warranty, os):
        super().__init__(name, warranty)
        self.os = os


# Task 20: MRO Demo
class A:
    def show(self): return "A"
class B(A):
    def show(self): return "B"
class C(A):
    def show(self): return "C"
class D(B, C): pass

d = D()
print(d.show())  # Shows method from B due to MRO: D -> B -> C -> A

# Section 3: Encapsulation (21–25)

# Task 21: Student with private attributes
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks


# Task 22: BankAccount with private balance
class BankAccount:
    def __init__(self, owner):
        self.__balance = 0
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Task 23: UserProfile with validation
class UserProfile:
    def __init__(self):
        self.__email = None
        self.__phone = None

    def set_email(self, email):
        if "@" in email:
            self.__email = email

    def set_phone(self, phone):
        if len(str(phone)) == 10:
            self.__phone = phone

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone


# Task 24: Employee with private salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary


# Task 25: Locker with private PIN
class Locker:
    def __init__(self):
        self.__pin = "1234"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin and len(new_pin) == 4:
            self.__pin = new_pin
            return "PIN changed"
        return "Invalid PIN"

    def check_pin(self, pin):
        return pin == self.__pin


# Section 4: Abstraction (26–30)

from abc import ABC, abstractmethod

# Task 26: Abstract Payment
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"


# Task 27: Shape with area and describe
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return "This is a shape"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Task 28: Animal abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


# Task 29: Transport template
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Bus(Transport):
    def start_engine(self):
        return "Bus engine started"

    def stop_engine(self):
        return "Bus engine stopped"


# Task 30: Appliance base class
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "500W"
    
    # Section 5: Polymorphism (31–35)

# Task 31: Method Overriding
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

dog = Dog()
print(dog.speak())


# Task 32: Duck Typing
class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

def render_shape(shape):
    return shape.draw()

print(render_shape(Circle()))
print(render_shape(Square()))


# Task 33: Simulate Method Overloading (default args)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))


# Task 34: Overloading using *args
class Sum:
    def add(self, *args):
        return sum(args)

s = Sum()
print(s.add(1, 2))
print(s.add(1, 2, 3))
print(s.add(1, 2, 3, 4))


# Task 35: Notification class
class Notification:
    def send(self, msg):
        return f"Sending: {msg}"

class SMS(Notification):
    def send(self, msg):
        return f"SMS: {msg}"

class Email(Notification):
    def send(self, msg):
        return f"Email: {msg}"

class PushNotification(Notification):
    def send(self, msg):
        return f"Push: {msg}"

notifs = [SMS(), Email(), PushNotification()]
for n in notifs:
    print(n.send("Hello!"))

# Task 36: Override __add__() for Vector addition
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: (6, 8)


dog = Dog()
print(dog.speak())  # Output: Dog barks


# Task 37: Override __len__() in Playlist class
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

pl = Playlist(["Song1", "Song2", "Song3"])
print(len(pl))  # Output: 3


# Task 38: Override __getitem__() and __setitem__() for ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, key):
        return self.items.get(key, 0)

    def __setitem__(self, key, value):
        self.items[key] = value

cart = ShoppingCart()
cart["apple"] = 3
cart["banana"] = 5
print(cart["apple"])   # Output: 3
print(cart["banana"])  # Output: 5



# Task 39: Override __contains__() for Inventory
class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

inv = Inventory(["milk", "bread", "eggs"])
print("milk" in inv)    # Output: True
print("butter" in inv)  # Output: False


# Task 40: Money comparison using __eq__, __gt__, __lt__
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

m1 = Money(100)
m2 = Money(150)
m3 = Money(100)

print(m1 == m3)  # True
print(m1 < m2)   # True
print(m2 > m3)   # True

# Task 41: Car with Engine (Composition)
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower}HP started."

class Car:
    def __init__(self, brand, engine_power):
        self.brand = brand
        self.engine = Engine(engine_power)  # Composition

    def start_car(self):
        return f"{self.brand} car starting. " + self.engine.start()

my_car = Car("Toyota", 120)
print(my_car.start_car())


# Task 42: Library has a list of Book objects (Aggregation)
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books  # Aggregation (books created outside)

    def list_books(self):
        return [book.title for book in self.books]

book1 = Book("Python 101")
book2 = Book("OOP Concepts")
my_library = Library([book1, book2])
print(my_library.list_books())


# Task 43: University with Departments (Composition)
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = [Department("Science"), Department("Arts"), Department("Engineering")]  # Composition

    def show_departments(self):
        return [dept.name for dept in self.departments]

uni = University("ABC University")
print(uni.show_departments())


# Task 44: Company with Employees (Aggregation)
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees  # Aggregation

    def show_employees(self):
        return [emp.name for emp in self.employees]

e1 = Employee("Alice")
e2 = Employee("Bob")
company = Company("TechCorp", [e1, e2])
print(company.show_employees())


# Task 45: Flight with Pilot, CabinCrew, and Passengers (Composition)class Pilot:
def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, count):
        self.count = count

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number
        self.pilot = Pilot("Captain Morgan")
        self.crew = CabinCrew(4)
        self.passengers = [Passenger("John"), Passenger("Emily")]

    def flight_info(self):
        return {
            "Flight No": self.flight_number,
            "Pilot": self.pilot.name,
            "Cabin Crew": self.crew.count,
            "Passengers": [p.name for p in self.passengers]
        }

flight = Flight("AI-203")
print(flight.flight_info())

# Task 46: Banking System
class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, acc_no, customer):
        self.acc_no = acc_no
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance

class Transaction:
    def __init__(self, account, type, amount):
        self.account = account
        self.type = type
        self.amount = amount

    def process(self):
        if self.type == "deposit":
            self.account.deposit(self.amount)
        elif self.type == "withdraw":
            self.account.withdraw(self.amount)

cust = Customer("Arun")
acc = Account("123456", cust)
txn1 = Transaction(acc, "deposit", 1000)
txn1.process()
txn2 = Transaction(acc, "withdraw", 400)
txn2.process()
print(f"Balance: ₹{acc.get_balance()}")


# Task 47: Quiz Application
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for q in self.questions:
            user_ans = input(q.prompt + " ")
            if user_ans.lower() == q.answer.lower():
                self.score += 1
        return f"Your score: {self.score}/{len(self.questions)}"

q1 = Question("What is 2 + 2?", "4")
q2 = Question("Capital of France?", "Paris")
quiz = Quiz([q1, q2])
# quiz.start()  # Uncomment to interact


# Task 48: Hotel Management System
class Room:
    def __init__(self, room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.is_booked = False

class Customer:
    def __init__(self, name):
        self.name = name

class Booking:
    def __init__(self, room, customer):
        self.room = room
        self.customer = customer

    def confirm(self):
        if not self.room.is_booked:
            self.room.is_booked = True
            return f"Room {self.room.room_no} booked for {self.customer.name}"
        return "Room already booked"

room1 = Room(101, "Deluxe")
cust1 = Customer("Priya")
booking = Booking(room1, cust1)
print(booking.confirm())


# Task 49: School Management System
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Student(Person):
    def get_role(self):
        return "Student"

class Teacher(Person):
    def get_role(self):
        return "Teacher"

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def enroll(self, student):
        self.students.append(student)

t = Teacher("Mr. Ram")
s1 = Student("Anu")
s2 = Student("Vikram")
course = Course("Maths", t)
course.enroll(s1)
course.enroll(s2)
print(f"{course.title} taught by {course.teacher.name}")
print("Enrolled students:", [s.name for s in course.students])


# Task 50: Library System
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))

    def borrow(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"You borrowed '{title}'"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"Returned '{title}'"
        return "Book not found"

lib = Library()
lib.add_book("1984")
lib.add_book("Python Basics")
print(lib.borrow("1984"))
print(lib.return_book("1984"))
