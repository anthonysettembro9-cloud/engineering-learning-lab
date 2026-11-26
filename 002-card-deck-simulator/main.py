import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = (rank + " of " + suit)
            deck.append(card)
    return deck

def draw_cards(deck):
    while True:
        if len(deck) < 2:
            print("Deck is empty!")
            break
        userInput = input("Press enter to see your two cards: ")
        if userInput == "":
            hand = []
            for draw in range(2):
                j = random.randint(0, len(deck)-1)
                randomCard = deck.pop(j)
                hand.append(randomCard)
            return hand
        else:
            print("Invalid, please press ENTER")

deck = create_deck()
hand = draw_cards(deck)
print(hand)
        





