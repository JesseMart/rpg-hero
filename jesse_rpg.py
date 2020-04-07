import random

class Character:
    def __init__(self, health, power, bounty):
        self.health = health
        self.power = power
        self.bounty = bounty
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
            

    def attack(self, enemy):
        if enemy.character_name != "Zombie" and enemy.character_name != "Shadow":
            enemy.health -= self.power

        if (self.character_name == "Hero"):
            chance = [1, 2, 3, 4 ,5]
            if random.choice(chance) == 2:
                double_damage = self.power * 2
                enemy.health -= double_damage
                print("***** Double damage inflicted! *****")
                print(f"You do {double_damage} damage to the {enemy.character_name}.")
                print(f"{enemy.character_name} now has {enemy.health} health.")
            else:
                print(f"You do {self.power} damage to the {enemy.character_name}.")
                

        if (enemy.character_name == "Medic"):
            health_chance = [1, 2, 3, 4, 5]
            if random.choice(health_chance) == 2:
                enemy.health += 10
                print("The Medic Healed 10 Health Points!!")
                print(f"The Medic's health is now {enemy.health}")
            else: 
                print(f"The {enemy.character_name} does {enemy.power} damage to you.")

        if (enemy.character_name == "Shadow"): 
            hit_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if random.choice(hit_count) == 1:
                print("The Shadow takes Damage!")
                enemy.health -= hero.health
            else:
                print("The Shadow takes no damage!")
                
        elif (self.character_name == "Goblin" or self.character_name == "Zombie" or self.character_name == "Shadow"):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def bounty_collect(self, enemy):
        hero_purse = 0
        hero_purse += enemy.bounty
        print(f"You collected the bounty, you have {hero_purse} coins.")

    def print_status(self):
        if self.character_name == "Hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "Goblin" or self.character_name == "Zombie" or self.character_name == "Shadow" or self.character_name == "Medic":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")


class Hero(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "Hero"
        super(Hero, self).__init__(health, power, bounty)
class Goblin(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "Goblin"
        super(Goblin, self).__init__(health, power, bounty)
class Zombie(Character):
    def __init__(self, health, power, bounty):
        self. character_name = "Zombie"
        super(Zombie, self).__init__(health, power, bounty)
class Medic(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "Medic"
        super(Medic, self).__init__(health, power, bounty)
class Shadow(Character):
    def __init__(self, health, power, bounty):
        self.character_name = "Shadow"
        super(Shadow, self). __init__(health, power, bounty)




medic = Medic(100, 10, 10)
shadow = Shadow(1, 10, 6)
hero = Hero(100, 15, 0)
goblin = Goblin(100, 10, 4)
zombie = Zombie(10, 1, 10000)
enemyList = [medic, shadow, goblin, zombie]
current_enemy = random.choice(enemyList)

def main(enemy):

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print(f"***** {enemy.character_name} is your enemy! *****\n")
        print(" What do you want to do?")
        print(f"1. Fight {enemy.character_name}")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            if not enemy.alive():
                enemy.print_status()
                print(f"The {enemy.character_name} is dead.")
                hero.bounty_collect(enemy)

        elif raw_input == "2":
            pass

        elif raw_input == "3":

            print("GOODBYE.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Enemy attacks hero
            enemy.attack(hero)
            if not hero.alive():
                hero.print_status()
                print("You are dead.")

main(current_enemy)
