import art
import game_data
import random

restart_game = True


def initialPickAccountNumbers(accounts):
    first_index = random.randint(0, len(accounts) - 1)
    check_duplication = first_index
    second_index = random.randint(0, len(accounts) - 1)
    while check_duplication == second_index:
        second_index = random.randint(0, len(accounts) - 1)
    return first_index, second_index


def game():
    all_accounts = game_data.data
    first_element = {}
    second_element = {}
    has_game_ended = False
    round = 0
    chosen_element = {}
    chosen_index = -1

    print(art.logo)

    while not has_game_ended and len(all_accounts) > 2:
        print(f"\n========= ROUND: {round + 1} =========\n")
        if round == 0:
            first_index, second_index = initialPickAccountNumbers(all_accounts)
            first_element = all_accounts[first_index]
            second_element = all_accounts[second_index]
        else:
            first_index = chosen_index
            first_element = chosen_element
            second_index = random.randint(0, len(all_accounts) - 1)
            while first_index == second_index:
                second_index = random.randint(0, len(all_accounts) - 1)
            second_element = all_accounts[second_index]

        print(
            f"{first_element['name']}: {first_element['description']}, from {first_element['country']}"
        )
        print(art.vs)
        print(
            f"{second_element['name']}: {second_element['description']}, from {second_element['country']}"
        )

        choice = input("\nWhich account has more followers - 'A' or 'B': ")
        while choice != 'A' and choice != 'B':
            choice = input("Try again - 'A' or 'B': ")

        is_guess_correct = False
        if choice == 'A':
            is_guess_correct = first_element[
                                   'follower_count'] >= second_element['follower_count']
            chosen_element = first_element
            chosen_index = first_index
            all_accounts.pop(second_index)
            if first_index > second_index:
                first_index -= 1
        else:
            is_guess_correct = first_element[
                                   'follower_count'] <= second_element['follower_count']
            chosen_element = second_element
            all_accounts.pop(first_index)
            if second_index > first_index:
                second_index -= 1
            chosen_index = second_index

        if is_guess_correct:
            print("\nYour guess was correct!\n")
            round += 1
        else:
            print("\nYour guess was incorrect!\n")
            has_game_ended = True

        print(
            f"\n{first_element['name']} has {first_element['follower_count']} and {second_element['name']} has {second_element['follower_count']}\n")
    print(f"Reached round {round + 1}.")
    try_again = input("\nTry again: 'y' or 'n': ")
    while try_again != 'y' and try_again != 'n':
        try_again = input("\nTry to type again: 'y' or 'n': ")

    if try_again == 'y':
        game()
    else:
        print("\nG_G")


game()
