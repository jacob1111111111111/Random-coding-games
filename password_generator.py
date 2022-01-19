import random

amount_of_characters = int(input('How many characters do you want your passcode to be?\n'))
type_of_characters = input('Do you want special characters? (yes/no)\n')
upper_lower = input('Do you want uppercase letters? (yes/no)\n')
list_of_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', ')', '-', '_',
                      '=', '+', '{', '}', '"', '<', '.', '>', '/', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9']
passcode = ''
i = 0

while i < amount_of_characters:
    normal = list_of_characters[random.randint(0, 25)]
    special = list_of_characters[random.randint(0, 56)]
    if upper_lower == 'yes':
        rand = random.randint(0, 1)
        if type_of_characters == 'yes':
            if rand == 0:
                passcode += special.upper()
            else:
                passcode += special
        else:
            if rand == 0:
                passcode += normal.upper()
            else:
                passcode += normal
    else:
        if type_of_characters == 'yes':
            passcode += special
        else:
            passcode += normal

    i += 1
print('\nYour passcode is: \n' + passcode)
