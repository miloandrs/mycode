#!/usr/bin/env python3
"""Camilo Castro | Procedural Dice Game"""

#Libraries
from random import randint

class Player():
    # object initialize function
    def __init__ (self):
        self.dice = []

    # define a method to roll
    def roll(self):
        #This resets the current dice
        self.dice = []
        # Loop to create random entries
        for i in range(3):
            #This adds 3 random numbers from 1 to 6 into the dice list
            self.dice.append(randint(1,6))

    #method to det the values of the dice
    def get_dice(self):
        return self.dice

#define if the roll is under 9
class cheat_mulligan:(player):
    def cheat(self):
        if sum(self.dice) <= 9:
            self.dice = []
            for i in range(3):
                self.dice.append(random.randint(1,6))

# define to roll and aditional die
class cheat_aditional(player):
    def extra_roll(self):
        self.dice.append(random.randint(1,6))

class weighted(player):
    def weight(self):
        if self.dice[0] < 3:
            self.dice[0] = random.randint(3,6)

class sabotage(self):
    def sab(self, other_player):
        other_player.dice[random.randint(range(3))] = random.randint(1,3)



def main():
    """run time code"""
    # Initialize players
    player1 = Player()
    player2 = Player()

    #roll the dice
    player1.roll()
    player2.roll()

    print(f'Player 1 rolled {player1.get_dice()}')
    print(f'Player 2 rolled {player2.get_dice()}')

    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print('Draw!')
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins")





#Call main function
if __name__ == "__main__":
    main()
