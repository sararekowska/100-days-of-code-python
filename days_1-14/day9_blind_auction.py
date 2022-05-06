import os

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
print("Welcome to the secret auction program")
bidders = {}
finished = False

def winner(dictionary):
    highest = 0
    winner_name = ""

    for person in dictionary:
        bid_amount = bidders[person]
        if bid_amount > highest:
            highest = bid_amount
            winner_name = person

    print(f"The winner is {winner_name} with a bid of {highest}")

while not finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if other_bidders == "no":
        finished = True
        winner(bidders)
    elif other_bidders == "yes":
        os.system('cls')