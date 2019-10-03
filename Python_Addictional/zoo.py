class Animal:
    def __init__(self, name, age):
        self.health = 200
        self.happiness = 100
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name},Age:{self.age}, Health:{self.health}, Happiness:{self.happiness}")


def Feed(self):
    self.health += 20
    self.happiness += 20

class Lion(Animal):
    pass

class Toger(Animal):
    pass


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)










zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()