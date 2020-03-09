from enum import Enum
from random import choice

Weapon = Enum("Weapon", "Rock, Paper, Scissors, Lizard, Spock")

# Add a list attribute to each weapon of the weapons it can beat
Weapon.Rock.beats = [Weapon.Scissors, Weapon.Lizard]
Weapon.Paper.beats = [Weapon.Spock, Weapon.Rock]
Weapon.Scissors.beats = [Weapon.Paper, Weapon.Lizard]
Weapon.Lizard.beats = [Weapon.Spock, Weapon.Paper]
Weapon.Spock.beats = [Weapon.Scissors, Weapon.Rock]

# Add an dictionary attribute to each weapon of the action verbs it is capable of
Weapon.Rock.actions = {Weapon.Scissors: "blunts", Weapon.Lizard: "crushes"}
Weapon.Paper.actions = {Weapon.Spock: "disproves", Weapon.Rock: "covers"}
Weapon.Scissors.actions = {Weapon.Paper: "cut", Weapon.Lizard: "decapitates"}
Weapon.Lizard.actions = {Weapon.Spock: "poisons", Weapon.Paper: "eats"}
Weapon.Spock.actions = {Weapon.Scissors: "smashes", Weapon.Rock: "vapourizes"}


# Set up player class
class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.score = 0
        
        
    def display_results(self, opponent, message):
        print(f"{self.name} chose {self.weapon.name} and {opponent.name} chose {opponent.weapon.name}")
        print(f"{self.weapon.name} {self.weapon.actions[opponent.weapon]} {opponent.weapon.name}")
        print(message)
        
    
    def win(self):
        self.score += 1
        


def display_instructions():
    ''' Function to display instructions when game starts'''

    print("""
    ____________________________________________________________________
    First the human player choses a weapon, after that the computer
    will chose a weapon at random
    The object of the game is to pick a weapon that will beat the weapon
    the computer has chosen

    Rock - beats Sciccors and Lizard
    Paper - beats Spock and Rock
    Scissors - beats Paper and Lizard
    Lizard - beats Spock and Paper
    Spock - beats Scissors and Rock

    Have fun!\n
    _____________________________________________________________________
    """)  



def display_score(human, ai):
    """ Function to display score after each turn """
    
    print("------------------------------------------------------")
    print(f"{human.name} - {human.score}    -    Computer - {ai.score}\n")    
    


#Main Game

print("Welcome to Rock, Paper, Scissors, Lizard, Spock\n")
player_name = input("What is your first name: ").title()
yes_no = input(f"\nHello {player_name}, do you want to see the instructions (Y or N)? ")
if yes_no.upper() == "Y":
    display_instructions()


# Create player objects
human = Player(player_name)
ai = Player("Computer")


# Main Game loop
while True:

    # User choses weapon
    # Catches the error if user enters an invalid option and loops until valid or QUIT
    try:
        menu_options = [f"{weapon.value} - {weapon.name}" for weapon in Weapon]
        menu_options = "\n".join(menu_options)
        print(menu_options)
        user_choice = input("Make you selection (1 - 5) or type QUIT: ")
        human.weapon = Weapon(int(user_choice))
    except:
        if user_choice.upper() == "QUIT":
            print("Thank you for playing")
            exit()
        else:
            print("Sorry, that was not one of the options, try again!\n")    
            continue

    # Computer chooses weapon
    ai.weapon = choice(list(Weapon))

    # Decides who won, displays results and increases score of wining player
    if human.weapon == ai.weapon:
        print(f"You chose {human.weapon.name} and the computer chose {ai.weapon.name}")
        print("It was a DRAW\n")
    elif ai.weapon in human.weapon.beats:
        human.display_results(ai, "You WIN\n")
        human.win()
    else:
        ai.display_results(human, "You LOSE\n")
        ai.win()
        
    display_score(human, ai)