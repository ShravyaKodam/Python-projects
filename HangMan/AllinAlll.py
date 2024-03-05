from multiprocessing.connection import answer_challenge
import os
os.system('CLS')
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def calculator():
    operations={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
    }
    n1=int(input("Enter the number1 value: "))
    print([symbol for symbol in operations])
    should_continue=True
    while should_continue:
        operation_symbol=input("enter symbol: ")
        n2=int(input("Enter the number2 value: "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(n1,n2)
        print(f"{n1}{operation_symbol}{n2}={answer}")
        if input("type 'Y' to continue or 'N to exit")=='y'.lower():
            n1=answer
        else:
            should_continue=False
            os.system('CLS')
            calculator()
            _ = os.system('cls')
calculator()
'''
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
print("The platform is: ", os.name)
print("big output\n"* 5)
# wait for 5 seconds to clear screen
sleep(5)
# now call function we defined above
screen_clear()
'''
'''
import random

endOfGame=True
# import HangManWordlist
# choosenWord=random.choice(HangManWordlist.wordList)
#or
from HangManWordlist import wordList
choosenWord=random.choice(wordList)
print(f"the solution is: {choosenWord}")
wordLength=len(choosenWord)
lives=6
from HangManStages import logo,stages
print(logo)
display=["_" for _ in range(wordLength)]
print(' '.join(display))
# display=[]
# for _ in range(wordLength):
#     display+="_"
# print(display)
while endOfGame: #not false means true
    guess = input("guess the letter: ").lower()
    if guess in display:
        print(f"You're already guessed {guess}")

    for position in range(wordLength):
        letter=choosenWord[position]
        if letter==guess:
            display[position]=letter
    if guess not in choosenWord:
        print(f"You guessed {guess}, that's not in the word")
        lives=lives-1
        if lives==0:
            endOfGame=False
            print("You lost")
    print(f"{' '.join(display)}")
    if "_" not in display:
        endOfGame=False
        print("You win")

    # from HangManStages import stages
    print(stages[lives])
    print("You lost")
    '''