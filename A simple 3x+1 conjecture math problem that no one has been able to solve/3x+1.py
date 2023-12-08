# Made by FallDropch86, in other words, Arhan Jain.

# Sidenote : Eveything is written long, so you might have to scroll.

# In Maths, there is a simple problem which has been left unsolved for decades.
# This problem is known as the 3x+1 problem or the collatz conjecture and many other n number of names.
# In this problem you can select any number.
# After that, if the number is odd, then multiply it by 3 then add 1 to it.
# Then if the number you get is even, then divide it by 2.
# This is pretty straightforward.
# But the issue is that, no matter how long does this take, but there will be a point where - 
# you will simply end up in a 4-2-1 loop.
# No Mathematician has found a solution to this controversial problem.
# We don't know if there is any number which won't end up in the 4-2-1 loop
# Many famous Mathematicians once thought - "Maths isn't ripe/good enough yet for such porblems."
# One could always dream that this barrier would be broken by some mathematician
# The purpose of this simple python program is to spend hours finding a number that won't end up in the:
# dread 4-2-1 loop. Now who knows if we will find a number?
# VERY DIFFICULT ASIAN OHIO MATHS MODE :  ON

import time

x = int(input("Enter any number and pray not to get into the 4, 2, 1 loop : "))

if x == 0 or x < 0:
        print("Can't use 0 or negative integer because the actual testing is done for numbers which are anything but not 0 or below 0.")
        time.sleep(6)
else:
    while(True):
        if x%2==0:
            x = x / 2
            print(x)
            time.sleep(0.001)
            if x == 1:
                print("Whoops! looks like you ended up into the 4, 2, 1 loop!")
                time.sleep(6)
                break

        elif x%2!=0:
            x = 3 * x + 1
            print(x)
            time.sleep(0.001)
            if x == 1:
                print("Whoops! looks like you ended up into the 4, 2, 1 loop!")
                time.sleep(6)
                break