import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for rank in ranks:
        card = (rank + " of " + suit)
        deck.append(card)
i = len(deck) - 1
for draw in range(5):
    j = random.randint(0, i)
    randomCard = deck.pop(j)
    print(randomCard)
    i -= 1


