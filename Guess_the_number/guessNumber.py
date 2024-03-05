
from random import randint
# Function to check the user's guess against the actual answer
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
def check_ans(guess, answer, turns):
    """check against guess. Returns the number of turns remaining"""
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")
#make a function to set for difficulty
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 to 100
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer=randint(1, 100)
    print(answer)
    turns=set_difficulty()
    #repeat the guessing functionaly if they get wrong.
    guess=0
    while guess !=answer:
        print(f"you have {turns} attempts remaining to guess the number")

        #lets the user guess the number
        guess=int(input("Make a guess: "))
        turns=check_ans(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
            return
        elif guess!=answer:
            print("Guess again")

#check the user guess again the actual answer

#track the number of attempts and reduce by 1 if the user guess worng
game()

# TODO
1.