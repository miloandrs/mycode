#!/usr/bin/env python3
"""Camilo Castro | Procedural Dice Game"""

#Libraries
from random import randint

def main():
    """run time code"""
    # Initialize empty arrays
    player1_dice = []
    player2_dice = []

    #random dice throws
    for i in range(3):
        player1_dice.append(randint(1,6))
        player2_dice.append(randint(1,6))

    print(f'Player 1 rolled {player1_dice}')
    print(f'Player 2 rolled {player1_dice}')

    if sum(player1_dice) == sum(player2_dice):
        print('Draw!')
    elif sum(player1_dice) > sum(player2_dice):
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins")





#Call main function
if __name__ == "__main__":
    main()
