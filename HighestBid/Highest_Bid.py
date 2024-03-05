import os
clear =lambda: os.system('cls')
from art import logo
print(logo)
bid_dict = {}

bid_again=False
def find_highest_bidder(bidding_records):
    highest_bid=0
    winner = ""
    for bidder in bidding_records:
        bid_amount=bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${bid_amount}")
while not bid_again:
    name = input("enter your name: ")
    price = int(input("enter your bid amount: "))
    bid_dict[name] = price
    bid_more=input("Are there any other bidders? type Yes to continue or No to stop \n").lower()
    if bid_more =="no":
        bid_again=True
        find_highest_bidder(bid_dict)
    elif bid_more=="yes":
        os.system('cls')
