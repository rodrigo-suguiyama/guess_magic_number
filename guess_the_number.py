from random import randint


def check_is_number(text):
    try:
        user_number = int(input(text))
    except ValueError:
        user_number = check_is_number("Please, choose a integer number: ")
    return user_number


def set_attempt(difficult_chosen):
    match difficult_chosen:
        case 1:
            return 10
        case 2:
            return 5
        case 3:
            return 3
        case 4:
            return 9999


def check_difficult_is_valid_number(x):
    if x in [1, 2, 3, 4]:
        return x
    else:
        print("\nPlease choose again a number corresponding a difficult "
              "between 1 and 4 to select the difficult:")
        difficult_level = check_is_number(difficult_text)
        difficult_level = check_difficult_is_valid_number(difficult_level)
        return difficult_level


print("   Game Name: Guess the magic number   ")
print("     Choose a difficult:  ")

difficult_text = ("- Easy (10 attempts) = [1]\n- Medium (5 attempts) = [2]\n"
                  "- Hard (3 attempts) = [3]\n- Chicken (no limit) = [4]\n"
                  "Type here the corresponding number to difficult: ")

difficult = check_is_number(difficult_text)
difficult = check_difficult_is_valid_number(difficult)

"""
while difficult != (1, 2, 3, 4):
    print("\nPlease choose again a number between 1 and 4 to select the difficult:")
    difficult = check_is_number(difficult_text)
"""
max_attempts = set_attempt(difficult)

number1 = check_is_number("Type the first integer number: ")
number2 = check_is_number("Type the second integer number: ")

while number2 == number1:
    number2 = int(input("Please, choose a different number from the first one: "))

if number1 > number2:
    number3 = number2
    number2 = number1
    number1 = number3

magic_number = randint(number1, number2)

count = 0
user_guess_number = check_is_number(f"Try to guess the magic number between {number1} and {number2}: ")
count += 1


while magic_number != user_guess_number and count < max_attempts:
    if user_guess_number < magic_number:
        user_guess_number = check_is_number("The number of your guess is smaller then the magic number, try again: ")
        count += 1
    else:
        user_guess_number = check_is_number("The number of your guess is bigger then the magic number, try again: ")
        count += 1

if max_attempts > count:
    print(f"\nYeah, the magic number is {magic_number}")
    print(f"You've done in {count} attempts!")
else:
    print("Game Over, try again")
