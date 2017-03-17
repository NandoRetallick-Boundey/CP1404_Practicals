
number_one = int(input("What is the first number?? "))

number_two = int(input("What is the second number?? "))

print("Even numbers: ", end=' ')

for i in range(number_one, number_two):
    if i % 2 == 0:
        print(i, end=' ')

print(' ')
print("Odd numbers: ", end=(' '))

for i in range(number_one, number_two):
    if i % 2 == 1:
        print(i, end=' ')

print(' ')
print("Square numbers: ", end=(' '))

for i in range(number_one, number_two):
    if (i ** 0.5).is_integer():
        print(i, end=' ')
