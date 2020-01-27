class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if enemy.character_name != "Zombie":
            enemy.health -= self.power
        if (self.character_name == "Hero"):
            print("You do {} damage to the {}.".format(self.power, enemy.character_name))
        elif (self.character_name == "Goblin" or self.character_name == "Zombie"):
            enemy.health -= self.power
        print("The {} does {} damage to you.".format(self.character_name, self.power))

    def print_status(self):
        if self.character_name == "Hero":
            print("You have {} health and {} power.".format(self.health, self.power))
        elif self.character_name == "Goblin" or self.character_name == "Zombie":
            print("The {} has {} health and {} power.".format(self.character_name, self.health, self.power))


class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "Hero"
        super(Hero, self).__init__(health, power)
class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "Goblin"
        super(Goblin, self).__init__(health, power)
class Zombie(Character):
    def __init__(self, health, power):
        self. character_name = "Zombie"
        super(Zombie, self).__init__(health, power)

hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)

def main(enemy):

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy.character_name}")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            if not hero.alive():
                print("You are dead.")

main(zombie)
