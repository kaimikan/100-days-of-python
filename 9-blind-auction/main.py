from art import logo

print(logo)
print("welcome to the secret auction")

next_bidder = "y"

bids = {}

while next_bidder == "y":
    next_bidder = ""
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: "))
    bids[name] = bid
    next_bidder = input("Are there any other bidders? Type 'y' or 'n'. ").lower()
    while next_bidder != 'y' and next_bidder != 'n':
        next_bidder = input("Other bidders? Type 'y' or 'n'. ").lower()

max_bid = -1
max_bid_owner = ""
for person in bids:
    if bids[person] > max_bid:
        max_bid = bids[person]
        max_bid_owner = person

print(f"The bid was won by {max_bid_owner} with a bet of ${round(max_bid)}")
