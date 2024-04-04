# BlackJack

from art import logo

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_list):

    # Check blackjack, 0 represents a blackjack
    if len(cards_list) == 2 and sum(cards_list) == 21:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)

def compare(your_score, computer_score):
    if your_score == computer_score:
        return "It is a draw!"
    elif computer_score == 0:
        return "Computer got a blackjack. You lose"
    elif your_score == 0:
        return "You got a blackjack. You win"
    elif your_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif your_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():

    print(logo)

    your_cards = []
    computer_cards = []
    ending_game = False

    # Deal both user and computer a starting hand of 2 random cad values
    for x in range(0, 2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not ending_game:

        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)

        print(f"You cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            ending_game = True

        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another.lower() == 'y':
                your_cards.append(deal_card())
            elif another.lower() == 'n':
                ending_game = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Print out the player's and computer's final hand and their scores at the end of the game.
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(your_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower() == 'y':
    play_game()








