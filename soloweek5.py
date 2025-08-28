class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self._secret_identity = None 

    def set_secret_identity(self, identity):
        self._secret_identity = identity

    def get_secret_identity(self):
        return self._secret_identity

    def save_city(self):
        print(f"{self.name} uses {self.power} to save {self.city}!")

    def __str__(self):
        return f"Superhero: {self.name}, Power: {self.power}, City: {self.city}"


class Sidekick(Superhero):
    def __init__(self, name, power, city, catchphrase):
        super().__init__(name, power, city)
        self.catchphrase = catchphrase

    def cheer(self):
        print(f"{self.name} shouts: '{self.catchphrase}'")

    def save_city(self):
        print(f"{self.name} helps save {self.city} with {self.power}!")

if __name__ == "__main__":
    hero = Superhero("Captain Underpants", "Bugdebugger", "Parisere")
    hero.set_secret_identity("Solomon")
    print(hero)
    print("Secret Identity:", hero.get_secret_identity())
    hero.save_city()

    sidekick = Sidekick("Seargent Underpants", "Quick Typing", "Parisere", "Let's squash those bugs!")
    print(sidekick)
    sidekick.cheer()
    sidekick.save_city()


class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

if __name__ == "__main__":
    car = Car()
    plane = Plane()
    print("Car action:", end=" ")
    car.move()
    print("Plane action:", end=" ")
    plane.move()    