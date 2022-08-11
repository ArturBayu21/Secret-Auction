import art
import os

bidders_data = {}

print(art.logo)
print("Welcome to the Secret Auction Program.")


# function that finds a winner
def find_winner(bidders):
    biggest_amount = 0
    for each_key in bidders:
        if bidders[each_key] > biggest_amount:
            biggest_amount = bidders[each_key]
            winner = each_key
    print(f"the winner is {winner} with ${biggest_amount} bid.")


# Storing bidder's data
is_continue = True
while is_continue == True:
    bidders_name = input("What is your name? : ")
    amount = int(input("What is your bid? : $"))
    bidders_data[bidders_name] = amount
    other_bidder = input(
        "Is there any other bidders? type 'yes' or 'no'! : ").lower()
    if other_bidder == "yes":
        os.system('cls')
    elif other_bidder == "no":
        is_continue = False
        find_winner(bidders_data)
