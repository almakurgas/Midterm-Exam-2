"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your script here

import random



jedan = 0
dva = 0
tri = 0
cetiri = 0
pet = 0
sest = 0


for i in range (100):
    palo = random.randint(1, 6)
    if palo == 1:
        jedan +=1

    elif palo ==2:
        dva +=1

    elif palo ==3:
        tri +=1

    elif palo ==4:
        cetiri +=1

    elif palo ==5:
        pet +=1

    elif palo ==6:
        sest +=1


print("Palo jedan:" + str(jedan))
print(" Palo dva:" + str(dva))
print("Palo tri:" + str(tri))
print(" Palo cetiri:" + str(cetiri))
print("Pala pet:" + str(pet))
print(" Palo sest:" + str(sest))
