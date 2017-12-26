"""
This is a User Vs System game.
The user starts the game.
For each turn user can pick 2,4,6 or 8 cards from the total number of cards.
In case there is one card left the above rule can be broken.
System will also follow the same.
The game continues until all cards are picked.
The player who leaves 6 or less remaining cards first loses.
"""

import random


def rand(x, y):
    r = random.randrange(2, 10, 2)
    if x - r < 0 or (x == r and r > 2) or y == r:
        return rand(x)
    else:
        return r


c = input("Enter 1 if you want to know about the game else press any other key ")

if c == "1":
    print(__doc__)

while True:
    n = int(input("Enter the no. of cards.Minimum 52. "))
    if n >= 52:
        break

print("Enter 2,4,6 or 8\n")

u = 0
r = 0

while True:
    pu = u
    u = int(input("Your turn "))

    if u not in [2, 4, 6, 8] or u == pu:
        continue
    if n - u > 0:
        n -= u
        t = 1
    else:
        continue

    if n <= 6:
        break

    if n == 1 or n == 2:
        t = 2
        break
    pr = r
    r = rand(n, pr)

    if n - r >= 0:
        n -= r
        t = 2
        print("System choses", r)

    if n > 2:
        print("Remaining cards:", n)
    elif n == 0:
        t = 2
        break
    else:
        t = 1
        break

    if n <= 6:
        break

if t == 1:
    print("System wins!\n")
else:
    print("You win!\n")

input('Press ENTER to exit')
