print("Welcome to the Number Guessing Game!")
import random
from art import logo
guessed_number = random.randint(1, 100)
print(guessed_number)
print(logo)
print("choose a number between 1 to 100")
level_difficulty=input("choose difficulty level: type 'easy' or 'hard'").lower()
if level_difficulty=='easy':
    print("you have 10 attempts remaining to guess the number")
else:
    print("you have 5 attempts remaining to guess the number")
easy=10
hard=5
guess_correct = True
for i in hard:
    guess_choice = int(input("make a guess: "))
    if i > hard:
        print("you lost")
        guess_correct = False
    else:
        if guess_choice < guessed_number:
            print("too low")
            print(f"Guess again, you have only {i-1} attempts")
        elif guess_choice > guessed_number:
            print("Too high")
            print("guess again")
        else:
            print(f"you got it. The answer was {guessed_number}")




            print("you lost")

print(guess_choice)