import random


def do_everything(n):
    if 10 < n < 15 or 110 < n < 115 or 210 < n < 215 or 310 < n < 315 or 410 < n < 415 or 510 < n < 515:
        output = str(n) + 'th'
    else:
        output = str(n) + list_of_ths[(n % 10) - 1]
    return output


list_of_ths = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
bound_1 = int(input("What do you want your lower bound to be?\n"))
bound_2 = int(input("What do you want your upper bound to be?\n"))
number, my_guess = random.randint(bound_1, bound_2), input("Enter your first guess in!\n")
i = 1

if isinstance(my_guess, int):
    while my_guess != number:
        if my_guess < number:
            print('too low, guess again\n')
            my_guess = input("what is your " + str(do_everything(i + 1)) + " guess?\n")
        elif my_guess > number:
            print('too high, guess again\n')
            my_guess = input("what is your " + str(do_everything(i + 1)) + " guess?\n")
        i += 1
else:
    print("Sorry, the input you just entered is not an integer. Please guess with an integer.")

print('nice job')
