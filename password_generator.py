from random import randint


def option1():
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    special_characters = '!@#$%^&*()_+'
    password = ''
    password_length = int(input("Provide password length: "))
    use_upper_case = input("Use upper case letters? (y/n): ")
    use_digits = input("Use digits? (y/n): ")
    use_special_characters = input("Use special characters? (y/n): ")

    # Create a string that contains all the characters the user wants to include in their password
    characters = lower_letters
    if use_upper_case == 'y':
        characters += upper_letters
    if use_digits == 'y':
        characters += numbers
    if use_special_characters == 'y':
        characters += special_characters

    for iterator in range(password_length):
        password += characters[randint(0, len(characters)-1)]

    print("Generated password: " + password + "\n")


def option2():
    print("Bye !")


def welcome_message():
    while True:
        print(" -- Password generator -- \n \
    Choose options:"
              "\n 1. Generlate password"
              "\n 2. exit the program")
        optoins = {'1': option1, '2': option2}
        choise = input("Your choise:: ")
        optoins.get(choise, lambda: print("Please enter a correct value"))()
        if choise == '2':
            break


if __name__ == '__main__':
    print("###---------------------------###")
    welcome_message()
