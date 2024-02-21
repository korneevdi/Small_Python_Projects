"""
This program converts numbers between different number systems.

The user enters an integer number and the number system in which it is written using the keyboard.
After this, the user enters the number system into which he wants to convert this number.
Currently the program works for number systems with any bases from 2 to 16.
"""


def convert(number, base1, base2):
    # Convert the number to decimal number system
    decimal_number = int(str(number), base1)
    
    # Convert the number from decimal number system
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % base2
        converted_number = str(remainder) + converted_number
        decimal_number //= base2
    
    return converted_number

# Application example
n = input("Enter number: ")
a = int(input("Enter initial number system base: "))
b = int(input("Enter final number system base: "))

m = convert(n, a, b)
print("Number", n, "in the number system", b, "is:", m)
