logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


# Function to find the highest bidder
def user_functions(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Correct assignment of highest_bid
            winner = bidder  # Assign the current bidder as winner

    print(f"The winner is {winner} with a bid of ${highest_bid}")


auction_dict = {}
user_continues = True

# Loop to gather bids
while user_continues:
    name = input("What is your name? \n").capitalize()
    bid = int(input("Enter your bid:$  \n"))
    auction_dict[name] = bid

    # Check if there are more bidders
    more_user = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()

    if more_user == "no":  # Correct comparison with 'more_user',
        user_continues = False  # Stop the loop if no more bidders
        user_functions(auction_dict)  # Call the function with 'auction_dict'
    elif more_user == "yes":
        print("\n" * 100)  # Clear the screen by printing empty lines
