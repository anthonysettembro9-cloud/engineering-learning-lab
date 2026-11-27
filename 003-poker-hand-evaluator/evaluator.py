def extract_ranks(hand):
    ranks = []
    for card in hand:
        rank = card.split(" of ")[0]
        ranks.append(rank)
    return ranks

def extract_suits(hand):
    suits = []
    for card in hand:
        suit = card.split(" of ")[1]
        suits.append(suit)
    return suits

def count_ranks(ranks):
    rank_counts = {}
    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    return rank_counts

def count_suits(suits):
    suit_counts = {}
    for suit in suits:
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    return suit_counts

def evaluate_duplicate_ranks(rank_counts):
    counts = list(rank_counts.values())
    ranking = ""
    if 4 in counts:
        ranking = "Four of a kind"
    elif 3 in counts:
        if 2 in counts:
            ranking = "Full house"
        else: 
            ranking = "Three of a kind"
    elif 2 in counts:
        if counts.count(2) == 2:
            ranking = "Two pair"
        else:
            ranking = "One pair"
    else:
        ranking = "High card"
    return ranking

def is_flush(suit_counts):
    counts = list(suit_counts.values())
    if 5 in counts:
        flush = True
    else:
        flush = False
    return flush

def convert_ranks(ranks):
    numerical_ranks = []
    face_values = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    for rank in ranks:
        try:
            numerical_ranks.append(int(rank))
        except ValueError:
            numerical_ranks.append(face_values[rank])
    return numerical_ranks

def is_straight(numerical_ranks):
    sorted_ranks = sorted(numerical_ranks)
    unique_ranks = set(numerical_ranks)
    difference = sorted_ranks[4] - sorted_ranks[0]
    count = len(unique_ranks)
    if difference == 4 and count == 5:
        straight = True
    elif sorted_ranks == [2, 3, 4, 5, 14]:
        straight = True
    else:
        straight = False
    return straight

def evaluate_hand(hand):
    hand_ranking = ""
    ranks = extract_ranks(hand)
    suits = extract_suits(hand)
    rank_counts = count_ranks(ranks)
    suit_counts = count_suits(suits)
    numerical_ranks = convert_ranks(ranks)
    straight = is_straight(numerical_ranks)
    flush = is_flush(suit_counts)
    duplicate_ranking = evaluate_duplicate_ranks(rank_counts)
    if flush and straight:
        if sorted(numerical_ranks) == [10, 11, 12, 13, 14]:
            hand_ranking = "Royal Flush"
        else:
            hand_ranking = "Straight Flush"
    elif duplicate_ranking == "Full house":
        hand_ranking = "Full House"
    elif flush:
        hand_ranking = "Flush"
    elif straight:
        hand_ranking = "Straight"
    else:
        hand_ranking = duplicate_ranking
    return hand_ranking