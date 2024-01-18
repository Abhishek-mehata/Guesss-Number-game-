import logo_art
print(logo_art.logo)
print("Let me think a number between 1 to 50")
import random
easy_level_attempts=10
hard_level_attempts=5
def set_difficulty(level):
    # global attempts
    if level=='easy':
        return easy_level_attempts
        # attempts=10
    else:
        return hard_level_attempts
        # attempts=5
    # pass

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low!")
        return attempts-1
        # print("Guess again")
    elif guessed_number>answer:
        print("Your guess is too high!")
        return attempts-1
    else:
        print(f"Your guess is correct >>>The ans was {answer}")

def game():
    # print(logo_art.logo)
    answer=random.randint(1,50)
    print(answer)
    level=input("Choose the level ... Type 'easy' or 'hard'").lower()
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number != answer:
        print(f"You have {attempts} remaining/")
        guessed_number=int(input("Guess the number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("Over")
            return
        elif guessed_number != answer:
            print("Guess again")
game()
