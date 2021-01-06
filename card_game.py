import random
def shuffle_deck(deck):
    shuffle_indx = list(range(52))
    random.shuffle(shuffle_indx)
    shuffled_deck = []
    for i in shuffle_indx:
        shuffled_deck.append(deck[i])
    return shuffled_deck

def get_top_card(deck):
    if len(deck) < 1:
        return "error", deck
    top_card = deck.pop()
    return top_card, deck

def play_a_game(deck, players, cards_each):
    hands = []
    for _ in range(players):
        hands.append([])
    for num in range(players * cards_each):
        card, deck = get_top_card(deck)
        hands[num % players].append(card)
    return hands

def sort_hand(single_hand):
    sorted_hand = sorted(single_hand, key=lambda x: sorted_deck.index(x))
    return sorted_hand

def score_hand(single_hand):
    total = 0
    for card in single_hand:
        if card == "error":
            total += 0
        else:
            card_score = rank[card[0]] * suit[card[1]]
            total += card_score
    return total

rank = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

suit = {
    's': 1,
    'd': 2,
    'h': 3,
    'c': 4
}

sorted_deck = []
for single_suit in suit:
    for single_rank in rank:
        sorted_deck.append(single_rank + single_suit)
print(f"Starting Deck: {sorted_deck}")

shuffled_deck = shuffle_deck(sorted_deck)
print(f"Shuffled Deck: {shuffled_deck}")

players = int(input("How many players? "))
cards_each = int(input("How many cards each? "))

hands = play_a_game(shuffled_deck, players, cards_each)
print(f"Dealt Hands: {hands}")
sorted_hands = [sort_hand(hand) for hand in hands]
print(f"Sorted Hands: {sorted_hands}")

scores = [score_hand(hand) for hand in hands]
winner = scores.index(max(scores))
print(f"Player{winner + 1} wins with {hands[winner]}")
unique_scores = sorted(set(scores), reverse=True)
rank_indx = {score: rank for rank, score in enumerate(unique_scores)}
ranks = [rank_indx[score] for score in scores]
print(f"Player Scores: {scores}")
print(f"Player Ranks: {ranks}")
for rank in range(players):
    rank_indices = [i for i, v in enumerate(ranks) if v == rank]
    for h in rank_indices:
        print(f"Player{h + 1} had {hands[h]} for a score of {scores[h]} and rank {ranks[h] + 1}")

