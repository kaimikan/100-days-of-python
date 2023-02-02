import random


def process_hand(cards):
    sum = 0
    card_index = 0
    for card in cards:
        sum += card
        if card == 11:
            if sum > 21:
                cards[card_index] = 1
        card_index += 1

    return cards


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards) - 1)]


draw_choice = '-'
black_jack = 21
choice = input("Play BlackJack? 'y' or 'n': ")
while choice != 'n' and choice != 'y':
    choice = input("again: ")

if choice == 'y':
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card()]
    print(f"Your starting hand: {player_hand}")
    print(f"The computer drew: {computer_hand}")

    while choice == 'y':
        player_sum = sum(player_hand)
        computer_sum = sum(computer_hand)
        if player_sum >= black_jack:
            if player_sum == black_jack:
                print("You got a blackjack, congrats!")
                if computer_sum == black_jack:
                    print("The computer also got BlackJack so you are even")
            else:
                print("You busted, G_G")
            choice = 'n'
        elif computer_sum >= black_jack:
            if computer_sum == black_jack:
                print("The computer got a blackjack, you lose!")
            else:
                print("The computer busted, G_G")
            choice = 'n'
        else:
            if draw_choice != 'n':
                draw_choice = input("Draw another 'y' or stop drawing 'n': ")
                while draw_choice != 'n' and draw_choice != 'y':
                    draw_choice = input(
                        "try again - 'y' to draw or stop drawing 'n': ")

            if draw_choice == 'y':
                drawn_card = deal_card()
                print(f"You drew {drawn_card}")
                player_hand.append(drawn_card)
                player_hand = process_hand(player_hand)
                print(f"The sum of your hand is {sum(player_hand)}")
            else:
                print("You chose not to draw")

            # the computer stops drawing at 17
            if computer_sum < 17:
                if draw_choice == 'n' and computer_sum > sum(player_hand):
                    choice = 'n'
                else:
                    drawn_card = deal_card()
                    print(f"The computer drew {drawn_card}")
                    computer_hand.append(drawn_card)
                    computer_hand = process_hand(computer_hand)
                    print(f"The sum of their hand is {sum(computer_hand)}")
            elif draw_choice == 'n' and computer_sum < sum(player_hand):
                drawn_card = deal_card()
                print(f"The computer drew {drawn_card}")
                computer_hand.append(drawn_card)
                computer_hand = process_hand(computer_hand)
                print(f"The sum of their hand is {sum(computer_hand)}")
            else:
                # end the game when the computer finishes their drawings after we stop
                if draw_choice == 'n':
                    choice = 'n'

            if sum(computer_hand) == black_jack:
                print("The computer got BlackJack")

    print(
        f"The game ended with a score of {sum(player_hand)} for you and {sum(computer_hand)} for the computer."
    )
else:
    print("See you next time!")
