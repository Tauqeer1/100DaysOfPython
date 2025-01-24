import os

def clear_console():
    print(f"name {os.name}")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("Welcome to secret auction program")

auction_bids = {}
answer = "yes"

while answer == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    auction_bids[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    clear_console()

highest_bider = {
    "name": '',
    "bid": 0
}
for key in auction_bids:
    if auction_bids[key] > highest_bider["bid"]:
        highest_bider["name"] = key
        highest_bider["bid"] = auction_bids[key]


print(f"The winner is {highest_bider["name"]} with a bid of ${highest_bider["bid"]}.")