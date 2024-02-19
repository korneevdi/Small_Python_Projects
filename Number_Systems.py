"""
This program converts numbers between different number systems.

The user enters an integer number and the number system in which it is written using the keyboard.
After this, the user enters the number system into which he wants to convert this number.
Currently the program works for number systems with any bases from 2 to 16.
"""

a = input("Enter your number: ")                # user enters the initial number
c1 = input("Enter the number system: ")         # user enters the number system base


# Converting a number to decimal system
try:
    c = int(c1)
except ValueError:
    import sys
    sys.exit("The number system base is an integer number from 2 to 16")
if c > 1 and c < 17:
    b = int(a, base = c)
else:
    import sys
    sys.exit("The number system base is an integer number from 2 to 16")


# Converting a number from decimal system
c2 = input("Into which number system to convert: ")
try:
    c = int(c2)
except ValueError:
    import sys
    sys.exit("The number system base is an integer number from 2 to 16")
F = []
while b >= c:
    F.append(b%c)
    b = b//c
F.append(b)
F.reverse()
#print(F)
G = []
for i in F:
    if i < 10:
        G.append(i)
    elif i == 10:
        G.append("a")
    elif i == 11:
        G.append("b")
    elif i == 12:
        G.append("c")
    elif i == 13:
        G.append("d")
    elif i == 14:
        G.append("e")
    elif i == 15:
        G.append("f")
res = ""
for i in G:
    res += str(i)
print("The number in the system with base", c, ":", res)
