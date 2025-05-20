bids = {}

while True:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    bids[name] = price

    bidders = input("Are there more bidders? yes or no:\n")
    if bidders.lower() == "yes":
        print("\n"*20)
    else:
        break  # stop asking for more bids

highest_bid = 0
winner = ""
for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        winner = name
print(f"The winner is {winner} with a bid of €{highest_bid}")

