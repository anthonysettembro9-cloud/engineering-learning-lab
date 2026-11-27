from deck import create_deck, draw_cards
from evaluator import evaluate_hand



deck = create_deck()
while True:
    userInput = input("Press enter to see your hand: ")
    if userInput == "":
        hand = draw_cards(deck, 5)
        if hand is not None:
            for card in hand:
                print(card)
            print(evaluate_hand(hand))
        break
    else:
        print("INVALID. Please press enter")
