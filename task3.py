"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def recursivesum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + recursivesum(piece[1:])
print recursivesum([1, 3, 4, 2, 5])



