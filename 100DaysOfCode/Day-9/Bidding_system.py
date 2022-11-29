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
        print(i)
        print(int(bidding_details[i]))
        if bidding_details[i] < winning_amount:
            winner = i
    print(winner)

billing_details = {}
while(continue_the_game):
    get_name = input("Get the name")
    get_amount = int(input("Get the amount"))
    continue_the_gameresult = input("Do you wish to continue yes/no").lower()
    billing_details[get_name] = {get_amount}
    if(continue_the_gameresult== 'no'):
        get_maximum_winner(billing_details)
        continue_the_game = False


