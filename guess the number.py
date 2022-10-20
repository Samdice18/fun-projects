import random as r

def user_range():

    a = input("Enter a start range: ")
    b = input("Enter a stop range: ")

    if not a.isdigit() and b.isdigit():
        print("Enter only numbers....")
    else:
        return int(a), int(b)


def secret_num(range_start,range_stop):

    random_num = r.randint(range_start, range_stop)
    
    return  random_num


def run_game(random_number):

    not_guessed = True
    user_tries = 3

    print(f"The random number has been set, you have {user_tries} turns to guess the random number")

    while not_guessed :

        user_guess = input("Enter your guess: ")

        if not user_guess.isdigit():
            print("Please enter only numbers....")
            continue
        elif user_guess.isdigit():
            if int(user_guess) != random_number:
                user_tries -= 1
                print(f"Incorrect, you have {user_tries} turns left")
            elif int(user_guess) == random_number:
                not_guessed = False
                print("Congatulations...")
                print(f"The number was : {random_number}")

        if user_tries == 0:
            print("better luck next time...")
            user_option = input("Do you want to try again (y/n)? ").lower()
            if user_option == "y":
                continue
            else:
                break


if __name__ == '__main__':
    num1 , num2 = user_range()
    random_number = secret_num(num1, num2)
    run_game(random_number)

