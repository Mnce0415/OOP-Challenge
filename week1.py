class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5       # Default: moderately hungry
        self.energy = 5       # Default: moderately energetic
        self.happiness = 5    # Default: neutral mood
        self.tricks = []      # List to store learned tricks

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger: {old_hunger} → {self.hunger}, Happiness increased to {self.happiness}.")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy: {old_energy} → {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played! Energy decreased, happiness and hunger increased.")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"🐾 {self.name}'s Status 🐾")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        print(f"{self.name}'s Tricks:")
        if self.tricks:
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print("No tricks learned yet.")


# Example usage:
if __name__ == "__main__":
    my_pet = Pet("Max")
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.train("play dead")  
    my_pet.show_tricks()
    my_pet.get_status()

