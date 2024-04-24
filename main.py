from art import logo
import os
import random

def winning_func():
    to_play = False
    if user_score == computer_score:
        return "It's a tie!"

    elif user_score == 21:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nWin, You have Blackjack 🏆"

    elif computer_score == 21:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nLose, opponent has Blackjack 😱"

    elif user_score > 21:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nYou went over. You lose 😣"

    elif computer_score > 21:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nOpponent went over. You win 😁"

    elif user_score < computer_score:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nYou Lose 😣"

    elif user_score < computer_score:
        return f"Your final hand: {user_cards_drawn}, final score: {user_score}\nComputer final hand: {computer_cards_drawn}, computer final score: {computer_score}\nOpponent went over. You win 😁"



# print(logo)
# input("Name")
# os.system('cls')

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_score = 0
user_cards_drawn = []

computer_score = 0
computer_cards_drawn = []



game = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no:  ")
print(logo)


# User - 1st cards, print and score calculation
user_cards = random.sample(cards,2)
user_cards_drawn += user_cards
user_score = user_cards_drawn[0] + user_cards_drawn[1]
print(f"Your cards: {user_cards_drawn}, current score: {user_score}")

# computer - 1st cards, score calculation but in hidden
computer_cards = random.sample(cards, 2)
computer_cards_drawn += computer_cards
computer_score += computer_cards[0] + computer_cards[1]
print(f"Computer's first card: {computer_cards[0]}")

to_play = True
while to_play:
    next_round = input("Type 'y' to get another card, type 'n' to pass: ")
    # second set
    if next_round == "y" and user_score <= 21:
        # user drawing extra card
        extra_card = random.sample(cards, 1)
        user_cards_drawn += extra_card
        user_score += extra_card[0]
        print(f"Your cards: {user_cards_drawn}, current score: {user_score}")

        extra_card_comp = random.sample(cards, 1)
        computer_cards_drawn += extra_card_comp
        computer_score += extra_card_comp[0]

    else:
        to_play = False
        print((winning_func()))



# else:
#     os.system('cls')






# fuction for deciding who is winning
    #tie, difference --- computer winning, user winning, "computer went over, user went over", "blackjack- user", computer
# function for drawing cards when score < 17

