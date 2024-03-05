import random

endOfGame=False
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
display=[]
for _ in range(wordLength):
    display+="_"
print(display)
while not endOfGame: #not false means true
    guess = input("guess the letter: ").lower()
    if guess in display:
        print(f"You're already guessed {guess}")

    for position in range(wordLength):
        letter=choosenWord[position]
        if letter==guess:
            display[position]=letter
            print("keep going")
    if guess not in choosenWord:
        print(f"You guessed {guess}, that's not in the word")
        lives=lives-1
        if lives==0:
            endOfGame=True
            print("You lost")
    print(f"{' '.join(display)}")
    if "_" not in display:
        endOfGame=True
        print("You win")

    # from HangManStages import stages
    print(stages[lives])
    #print("You lost")