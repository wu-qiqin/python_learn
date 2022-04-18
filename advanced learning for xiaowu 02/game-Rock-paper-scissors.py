"""
Created by hu-jinwen on 2022/4/3
"""
import random

rock = 1
paper = 2
scissors = 3

player = int(input("choose rock or paper or scissors:"))
computer = random.randint(1, 3)

print("you chose %d- the computer chose %d" % (player, computer))

if ((player == rock and computer == scissors)
        or (player == paper and computer == rock)
        or (player == scissors and computer == paper)):

    print("you win!")

elif player == computer:
    print("let's try one more")

else:
    print("what a shame!")

