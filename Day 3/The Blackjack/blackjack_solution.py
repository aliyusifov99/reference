# Step 1: Create a function that uses the list of cards to return a random card
import random
from art import logo

def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Step 3: Create a function called calculate_score() that takes in a list of cards and returns the total score
def calculate_score(cards):
    """Returns the total score of a given list of cards"""
    
    # Step 4: Inside calculate_score() check for a blackjack (2 cards with a score of 21) and return 0 instead of actual score. 0 will
    #  represent Blackjack in the game.
    if sum(cards)==21 and len(cards) == 2:
        return 0

    # Step 5: Inside calculate_score() check for an ace (11).If the score is already over 21, remove 11 and replace it with 1. hint: remove()
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Step 10:  Create a function called compare() and pass in the user_score() and computer_score(). If the computer and user both have 
#  the same score, then its a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0),
#  then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
#  If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    """Returns the winner of the game"""
    if user_score == computer_score:
        print("It's a draw!")
    elif user_score == 0:
        print("You win with a blackjack!")
    elif computer_score == 0:
        print("You lose, opponent has a Blackjack :D!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")

def play_game():
    # Step 12: Add the art.py logo
    print(logo)
    # Step 2: Give the user and computer 2 cards each using deal_card():
    user_cards = []
    computer_cards = []
    game_is_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Step 8: Check the score with every new card drawn and repeat steps 6 and 7 until the game is over.
    while not game_is_over:

        # Step 6: call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, end the game.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards) 
        print(f'Your cards are {user_cards} and your score is {user_score}')
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            game_is_over = True
        else:
            # Step 7: If the game is not over, ask the user if they want to hit or stay.
            user_should_deal = input('Type "y" to get another card and "n" to stop: ').lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_is_over = True

    # Step 9: Once the user is done, let the computer play. The computer should draw cards until the score is over 17.  
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'   Your final hand: {user_cards}, final score: {user_score}')
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)

# Step 11: Ask the user if they want to play again. If they type "y", then clean the console, start a new game and show the logo from art.py.
#  If they type "n", then exit the game.
while input('Do you want to play again? (y/n): ').lower() == 'y':

    play_game()