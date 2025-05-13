# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Animal Class
class Animal:
    def move(self):
        pass  # Default move method for animals

# Vehicle Class
class Vehicle:
    def move(self):
        pass  # Default move method for vehicles

# Dog class (inherits from Animal)
class Dog(Animal):
    def move(self):
        print("Running")

# Bird class (inherits from Animal)
class Bird(Animal):
    def move(self):
        print("Flying")

# Car class (inherits from Vehicle)
class Car(Vehicle):
    def move(self):
        print("Driving")

# Plane class (inherits from Vehicle)
class Plane(Vehicle):
    def move(self):
        print("Flying")

# instances
animals = [Dog(), Bird()]
vehicles = [Car(), Plane()]

# Polymorphism
print("Animals in motion:")
for animal in animals:
    animal.move()  # Calls the overridden move() method based on the instance

print("\nVehicles in motion:")
for vehicle in vehicles:
    vehicle.move()  # Calls the overridden move() method based on the instance
