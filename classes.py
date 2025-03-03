import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        
# Use random int to randomize strike damage
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
      
        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == False:
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == True: 
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def heal(self):
        self.health += 15
        print(f"{self.name} regenerates 15 health! Current health: {self.health}")
        
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Crippling Strike')
        print('2. Battle Rage')
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            opponent.health -= 15
            opponent.attack_power -= 5
            if opponent.attack_power <= 0:
                opponent.attack_power = 2
            print(f"Crippling Strike was used on {opponent.name}. Their health was reduced to {opponent.health} and attack power to {opponent.attack_power}")
        elif action == '2':
            self.health += 7
            self.attack_power += 7
            print(f"{self.name} uses Battle Rage, and increases health and attack power by 7! health: {self.health}, attack power: {self.attack_power}")
            
# Mage class (inherits from Character)           
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Fire Strike') # Increases attack power by 10
        print('2. Dual Threat') # Strikes opponent for 10 damage and evades next attack. 
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            self.attack_power +=10
            opponent.health -= self.attack_power
            print(f"{self.name} uses Fire Strike and increases attack power by 10! Attack_power: {self.attack_power}")
        elif action == '2':
            self.health += 7
            self.attack_power += 10
            print(f"{self.name} uses Dual Threat, and attacks opponent for 10 damage while evading the next strike.")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name, quick_shot=50):
        super().__init__(name, health=125, attack_power= 50)
        self.quickshot = quick_shot
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Quickshot') # Double attack damage
        print('2. Evade') # Evades next attack from the opponent 
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            opponent.health -= self.quickshot
            print(f"{self.name} used a double arrow attack that doubles their total damage to {self.attack_power}.")
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage.")
        elif action == '2':
            self.evadeNextAttack = True 
            print(f"\n(self.name) used Evade. He will evade the next attack!")
                  
# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name, quick_shot = 45):
        super().__init__(name, health=100, attack_power= 35)
        self.quickshot = quick_shot
        self.evadeNextAttack = False
    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Holy Strike') # Bonus damage. Will increase damage by 10
        print('2. Divine Shield') # Evades next attack from the opponent 
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            self.attack_power += 10
            opponent.health-=self.attack_power
            print(f"{self.name} is using his Holy Strike ability to increase their total damage to {self.attack_power}.")
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage.")
        elif action == '2':
            self.evadeNextAttack = True 
            print(f"\n(self.name) used Divine Shield. He will evade the next attack!")
            
# Rogue class (inherits from Character)            
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        
    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Increase Attack Power')
        print('2. Life Steal')
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            self.attack_power += 20
            print(f"{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power}")
        elif action == '2':
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} uses Life Steal, and takes away {self.attack_power} health from {opponent.name} and regenerated some health.")
        else:
            # Default to Choice 1
            self.attack_power += 20
            print(f"{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power}")
            
# Dark Wizard class (inherits from Character)
class DarkWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
