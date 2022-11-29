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
print("Welcome to the great Secret Bid..!")


continue_the_game = True


def get_maximum_winner(bidding_details):
    winner = ""
    winning_amount = 0
    for i in bidding_details:
         if bidding_details[i] > winning_amount:
            winning_amount = bidding_details[i]
            winner = i
    print(f"The winner for the bid is {winner} of amount {winning_amount}")

billing_details = {}
while(continue_the_game):
    get_name = input("Get the name")
    get_amount = int(input("Get the amount"))
    continue_the_gameresult = input("Do you wish to continue yes/no").lower()
    billing_details[get_name] = get_amount
    if(continue_the_gameresult== 'no'):
        get_maximum_winner(billing_details)
        continue_the_game = False

"""
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    bidding_finished = False
    
"""

