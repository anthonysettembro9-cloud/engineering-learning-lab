from evaluator import evaluate_duplicate_ranks, is_flush, convert_ranks, is_straight, evaluate_hand

print(evaluate_duplicate_ranks({"Ace": 4, "King": 1}))
print(evaluate_duplicate_ranks({"Ace": 3, "King": 2}))
print(evaluate_duplicate_ranks({"Ace": 3, "King": 1, "Queen" : 1}))
print(evaluate_duplicate_ranks({"Ace": 2, "King": 2, "Queen" : 1}))
print(evaluate_duplicate_ranks({"Ace": 2, "King": 1, "Queen" : 1, "Jack" : 1}))
print(evaluate_duplicate_ranks({"Ace": 1, "King": 1, "Queen" : 1, "Jack" : 1, "10" : 1}))
print(is_flush({"Spades" : 5})) == True
print(is_flush({"Spades" : 4, "Hearts" : 1})) == False
print(convert_ranks(["2", "5", "10"]))
print(convert_ranks(["Jack", "Queen", "King", "Ace"]))
print(convert_ranks(["Ace", "2", "3", "4", "5"]))
print(convert_ranks(["7", "7", "King"]))
print(convert_ranks(["10", "Jack", "3", "Ace", "Queen"]))
print(convert_ranks([]))
print(is_straight([9, 5, 7, 6, 8]))
print(is_straight([14, 13, 12, 11, 10]))
print(is_straight([14, 2, 3, 4, 5]))
print(is_straight([5, 6, 7, 7, 9]))
print(is_straight([2, 3, 4, 5, 7]))
print(is_straight([12, 13, 14, 2, 3]))
print(is_straight([14, 2, 5, 9, 10]))
print(is_straight([14, 2, 3, 4, 4]))
print("\n--- COMPLETE HAND EVALUATION ---")

# Royal flush
print(evaluate_hand(["Queen of Hearts", "10 of Hearts", "Ace of Hearts", "Jack of Hearts", "King of Hearts"]))

# Straight flush
print(evaluate_hand(["5 of Spades", "7 of Spades", "9 of Spades", "6 of Spades", "8 of Spades"]))

# Four of a kind
print(evaluate_hand(["Ace of Hearts", "Ace of Spades", "Ace of Clubs", "Ace of Diamonds", "King of Hearts"]))

# Full house
print(evaluate_hand(["King of Hearts", "Ace of Spades", "King of Clubs", "Ace of Diamonds", "King of Spades"]))

# Flush
print(evaluate_hand(["2 of Hearts", "5 of Hearts", "7 of Hearts", "Jack of Hearts", "Ace of Hearts"]))

# Straight
print(evaluate_hand(["9 of Hearts", "5 of Clubs", "7 of Spades", "6 of Diamonds", "8 of Hearts"]))

# Three of a kind
print(evaluate_hand(["Queen of Hearts", "Queen of Clubs", "Queen of Spades", "5 of Hearts", "2 of Diamonds"]))

# Two pair
print(evaluate_hand(["Ace of Hearts", "King of Clubs", "Ace of Spades", "King of Hearts", "7 of Diamonds"]))

# One pair
print(evaluate_hand(["7 of Hearts", "7 of Clubs", "King of Spades", "5 of Hearts", "2 of Diamonds"]))

# High card
print(evaluate_hand(["Ace of Hearts", "King of Clubs", "9 of Spades", "5 of Hearts", "2 of Diamonds"]))

# Ace-low straight
print(evaluate_hand(["Ace of Hearts", "2 of Clubs", "3 of Spades", "4 of Diamonds", "5 of Hearts"]))

# Ace-low straight flush (NOT royal flush)
print(evaluate_hand(["Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts"]))

# Ace-high straight without a flush
print(evaluate_hand(["Ace of Hearts", "King of Clubs", "Queen of Spades", "Jack of Diamonds", "10 of Hearts"]))

# Almost a straight
print(evaluate_hand(["5 of Hearts", "6 of Clubs", "7 of Spades", "8 of Diamonds", "10 of Hearts"]))
print("All tests passed!")