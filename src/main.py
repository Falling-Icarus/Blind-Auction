import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)
loop = True
auction = {}

def winner(the_auction):
    name_person = ""
    value = 0
    for bidder in the_auction:
        if the_auction[bidder] > value:
            value = the_auction[bidder]
            name_person = bidder
    print(f"The winner is {name_person} with a bid of ${value}")


while loop == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "yes":
        print("\n" *100)
        loop = True
    else:
        loop = False
        winner(auction)

