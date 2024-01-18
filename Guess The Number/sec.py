# create random number in some range
# guess a number
# select [easy 10 ] or [hard 5] level:
# if live >0:
# if guessed number is > than random number print too high and decrease life
# elif gussed number < random number print too low and decrease life
# elif guessed number = random number print won the game
# else:
# Loose the  game
import random
print(f"Welcome to guess the number game.")
print(f"Here we have generated the number of range(0-50)")
random_number=random.choice(range(0,51))
print(random_number)
level=input("Enter 'easy' for easy level and 'hard' for hard level=").lower()
guessed_number=0
over=False
while not over:
    # guessed_number=int(input(f"Guess a number:"))
    if level=='easy':
        live=10
        while live > 0:
            print(f"You have {live}/10 live")
            guessed_number=int(input(f"Guess a number:"))
            if guessed_number==random_number:
                print(f"You won!")
                over=True
                break
            elif guessed_number > random_number:
                print("Too High guess!")
                over=False
                live=live-1
            elif guessed_number < random_number:
                print(f"Too low guess!")
                over=False
                live=live-1      
            elif live==0:
                 print("Oops! you loosed.")  
                 break
    elif level=='hard':
                live=5  
                while live >=1:
                    print(f"You have {live}/5 live!")
                    guessed_number=int(input("Guess a number"))
                    if guessed_number==random_number:
                        print("You won!")
                        over=True
                        break
                    elif guessed_number >random_number:
                        print("Too high guess!")
                        over=False
                        live=live-1
                    elif guessed_number < random_number:
                        print("Too low guess!")
                        over=False
                        live=live-1
                    elif live==0:
                         print("Oops! you loosed")
                         break
     
            # else:
            #     break
            #     over=True
