"""Nando Johan Retallick-Boundey."""

name = str(input("Enter your name: "))
while len(name) == 0:
    name = str(input("Enter your name: "))

for char in range(0, len(name), 2):
    if char % 2 == 0:
        print("{}".format(name[char]), end="")
