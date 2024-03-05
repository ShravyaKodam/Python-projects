from art import logo,vs
from allData import data
import random
def format_data(account):
    """format the account data to printable"""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=='b'
score=0
game_should_continue=True
account_b=random.choice(data)
while game_should_continue:

    # print(data)
    print(logo)
    # print(vs)
    #print logo
    #import random function
    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #compare statements from data

    #ask user for guess
    guess=input("who has more followers? Type 'A' or 'B': ").lower()

    # check the values of followers
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct=check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score+=1
        print(f"you are right! current score is {score}")
    else:
        print(f"you lost, final score is {score}")
        game_should_continue=False
#if correct continue the game
#score increase
#repeat the game
#making account at the position B
#clear the screen
