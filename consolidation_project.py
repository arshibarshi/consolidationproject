#Tuple Out Game - Ademir Ferreyra
#Dice game 

import os
import random

#Welcome screen 
def welcome():
    print(""""

                      Hello!
                   WELCOME TO
                THE TUPLE OUT GAME
    Rules:
    - Roll three dice each turn.
    - If all three dice match, you "tuple out" and score 0 points.
    - If two dice match, they are "fixed" and can't be re-rolled.
    - Re-roll the non-fixed dice to increase your score.
    - Stop rolling to score the total of all three dice.
    - First player to reach the target score wins!
    
    Good luck and may the best roller win!
    
    """)

#Calling welcome
welcome()

#Player(p) scores - begin with zero
p1 = 0
p2 = 0

#plan to add dice faces
def dice_face(value):
    if value == 1:
        return """
        -----
       |     |
       |  o  | 
       |     |
        -----
        """
    elif value == 2:
        return """
        -----
       | o   |
       |     | 
       |   o |
        -----
        """
    elif value == 3:
        return """
        -----
       | o   |
       |  o  | 
       |   o |
        -----
        """
    elif value == 4:
        return """
        -----
       | o o |
       |     | 
       | o o |
        -----
        """

    elif value == 5:
        return """
        -----
       | o o |
       |  o  | 
       | o o |
        -----
        """

    elif value == 6:
        return """
        -----
       | ooo |
       |     | 
       | ooo |
        -----
        """
    
#End game condition
target_score = 10

#dice - six sides
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
dice3 = [1,2,3,4,5,6]



#Dice roll
diceRolls = [dice1, dice2, dice3]

#displaying the dice when you first run the program
for x in diceRolls:
    print(x)

#shuffling through the dice with a loop

while p1 < target_score and p2 < target_score:
    for player in range(1,3):
        
        print(f"\n it's player {player}'s turn")

        #Roll dice using shuffle
        random.shuffle(dice1)
        random.shuffle(dice2)
        random.shuffle(dice3)

        #getting the result of the roll after shuffling
        roll1 = dice1[0]
        roll2 = dice2[0]
        roll3 = dice3[0]

        #added faces to the rolling line
        print(f"you rolled:")
        print(dice_face(roll1))
        print(dice_face(roll2))
        print(dice_face(roll3))



        if roll1 == roll2 == roll3:
            print("No points awarded this turn")
            continue
        
        #if dice can be rerolled or fixed

        fixed = []

        if roll1 == roll2:  
            fixed += [roll1]  
        if roll1 == roll3:
            fixed += [roll1]  
        if roll2 == roll3:  
            fixed += [roll2] 

        #remove duplicates from the fixed list
        fixed = list(set(fixed))

        print(f"{fixed} can't be rerolled")

        while True:
            print(f"fixed dice: {fixed}")

            reroll = input("Do you want to reroll the non-fixed dice? (y/n)").lower()
            #if the player wants to reroll the dice
            if reroll == 'y':
                if roll1 not in fixed:
                    random.shuffle(dice1)
                    roll1 = dice1[0]
                if roll2 not in fixed:
                    random.shuffle(dice2)
                    roll2 = dice2[0]
                if roll3 not in fixed:
                    random.shuffle(dice3)
                    roll3 = dice3[0]
                
                print(f"new rolls: {roll1},{roll2},{roll3}")

                if roll1 == roll2 == roll3:
                    print("Oh no you tupled out! No points this turn.")
                    break
            else:
                break

            # calculating and add scores
        if roll1 != roll2 or roll1 != roll3 or roll2 != roll3:
            score = roll1 + roll2 + roll3
            print(f"You scored {score} points this turn!")
            if player == 1:
                p1 += score
            else:
                p2 += score

        print(f"Scores - Player 1: {p1}, Player 2: {p2}")

# Announce winner
if p1 >= target_score:
    print("\nPlayer 1 wins!")
else:
    print("\nPlayer 2 wins!")
