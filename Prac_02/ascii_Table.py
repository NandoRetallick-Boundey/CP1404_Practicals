MIN_CHARACTER_CODE = 33
MAX_CHARACTER_CODE = 127

character_to_convert = str(input("Enter a character: "))
character_code = ord('{}'.format(character_to_convert))

print("The ASCII code for {} is {}".format(character_to_convert, character_code))

code_to_convert = int(input("Enter a number between {} and {}: ".format(MIN_CHARACTER_CODE, MAX_CHARACTER_CODE)))
code_character = chr(code_to_convert)

while code_to_convert < MIN_CHARACTER_CODE or code_to_convert > MAX_CHARACTER_CODE:
    print("Invalid input please try again")
    code_to_convert = int(input("Enter a number between {} and {}: ".format(MIN_CHARACTER_CODE, MAX_CHARACTER_CODE)))
    code_character = chr(code_to_convert)

print("The character for {} is {}".format(code_to_convert, code_character))

for i in range(33, 127):
    print("{:4} {:>4}".format(i, chr(i)))
