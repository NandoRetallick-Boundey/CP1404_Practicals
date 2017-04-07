"""
Author: Nando Retallick-Boundey
CP1404 prac
Hexadecimal colour conversion
"""

HEXADECIMAL_COLOUR = {"RED": "#FF0000", "GREEN": "#008000", "BLUE": "#0000FF",
                      "YELLOW": "#FFFF00", "GOLD": "#FFD700", "SILVER": "#C0C0C0",
                      "SNOW": "#FFFAFA", "IVORY": "#FFFFF0", "WHEAT": "#F5DEB3",
                      "STEELBLUE": "#4682B4"}

colour = input("Enter a colour: ").upper()
while colour != "":
    if colour in HEXADECIMAL_COLOUR:
        print("{:10} is {}".format(colour, HEXADECIMAL_COLOUR[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").upper()
