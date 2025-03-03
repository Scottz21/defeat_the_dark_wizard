from classes import *
# Function to create player character based on user input
def create_character():
    print("\nWelcome to Defeat the Dark Wizard.")
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin")  
    print("5. Rogue")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin (name)
    elif class_choice == '5':
        return Rogue(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    
# Battle Function: Facilitates battle between the player and the Dark Wizard. Has a user menu for actions.
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
# Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! Better luck next time.")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!! Great Job:)")
        
# Main function to handle flow of game
def main():
    player = create_character()
    wizard = DarkWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
    