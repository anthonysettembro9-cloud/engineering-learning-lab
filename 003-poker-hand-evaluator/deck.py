import random

def create_deck():
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    for suit in suits:
        for rank in ranks:
            card = (rank + " of " + suit)
            deck.append(card)
    return deck

def draw_cards(deck, num_cards):
    if len(deck) < num_cards:
        print("Deck is empty!")
        return None
    
    hand = []
    for draw in range(num_cards):
            j = random.randint(0, len(deck)-1)
            randomCard = deck.pop(j)
            hand.append(randomCard)
    return hand