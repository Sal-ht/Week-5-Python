# Superhero Class
class Superhero:
    def __init__(self, name, power, health):

        self.name = name       # Hero's name
        self.power = power     # Superpower (e.g., flight, strength)
        self._health = health  # Health (encapsulated with underscore)

    # Public method to describe the superhero
    def describe(self):
        return f"{self.name} has the power of {self.power} and {self._health} health!"

    # Encapsulation: Method to change health safely
    def heal(self, amount):
        self._health += amount
        print(f"{self.name} healed by {amount}. Health now: {self._health}")

    # Polymorphism: Action method, can be overridden in subclasses
    def action(self):
        print(f"{self.name} is using {self.power}!")

# Inheritance: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def __init__(self, name, health):
        # Call parent class constructor
        super().__init__(name, "flight", health)

    # Override the action method for flying hero
    def action(self):
        print(f"{self.name} is soaring through the sky with {self.power}!")

# Inheritance: StrengthHero inherits from Superhero
class StrengthHero(Superhero):
    def __init__(self, name, health):
        # Call parent class constructor
        super().__init__(name, "super strength", health)

    # Override the action method for strength hero
    def action(self):
        print(f"{self.name} is smashing everything with their {self.power}!")

# Create instances of Superheroes
hero1 = Superhero("Captain Hero", "invisibility", 100)
hero2 = FlyingHero("SkyMaster", 120)
hero3 = StrengthHero("Hulk", 150)

# Polymorphism
hero1.action()  # Default action: "Captain Hero is using invisibility!"
hero2.action()  # Overridden action: "SkyMaster is soaring through the sky with flight!"
hero3.action()  # Overridden action: "Hulk is smashing everything with their super strength!"

# Encapsulation: Healing heroes
hero1.heal(20)  # "Captain Hero healed by 20. Health now: 120"
hero2.heal(30)  # "SkyMaster healed by 30. Health now: 150"
hero3.heal(50)  # "Hulk healed by 50. Health now: 200"

# Hero descriptions
print(hero1.describe())  # "Captain Hero has the power of invisibility and 120 health!"
print(hero2.describe())  # "SkyMaster has the power of flight and 150 health!"
print(hero3.describe())  # "Hulk has the power of super strength and 200 health!"
