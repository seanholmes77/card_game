'''
Card Game that populates a deck, shuffles it, deals hands to specs, and scores.

Rank and Suit are used to create a sorted deck for reference. Random's shuffle
method is used to shuffle the order of the sorted deck. The game is played by
dealing hands to the number of players for the number of cards specified. The
score is calculated by rank * suit (4=c, 3=h, 2=d, 1=s) and leaderboard posted.
'''
import random
def shuffle_deck(deck):
    '''Returns deck in shuffled order of input deck'''
    shuffle_indx = list(range(52))
    random.shuffle(shuffle_indx)
    temp_shuffled_deck = []
    for i in shuffle_indx:
        temp_shuffled_deck.append(deck[i])
    return temp_shuffled_deck

def get_top_card(deck):
    '''Returns top card and updated deck from an input deck'''
    if len(deck) < 1:
        return "error", deck
    top_card = deck.pop()
    return top_card, deck

def play_a_game(deck, players, cards_each):
    '''Returns list of dealt hands from inputs of deck, players to deal, and cards dealt to each'''
    temp_hands = []
    for _ in range(players):
        temp_hands.append([])
    for num in range(players * cards_each):
        card, deck = get_top_card(deck)
        temp_hands[num % players].append(card)
    return temp_hands

def sort_hand(single_hand, sorted_deck):
    '''Returns sorted hand based on each card's index in original sorted deck'''
    sorted_deck.insert(0, "error")
    sorted_hand = sorted(single_hand, key=lambda x: sorted_deck.index(x))
    return sorted_hand

def score_hand(single_hand, ranks, suits):
    '''Returns the point value of a hand based on rank and suit'''
    total = 0
    for card in single_hand:
        if card == "error":
            total += 0
        else:
            card_score = ranks[card[0]] * suits[card[1]]
            total += card_score
    return total

def main():
    try:
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

        dealt_sorted_deck = []
        for single_suit in suit:
            for single_rank in rank:
                dealt_sorted_deck.append(single_rank + single_suit)
        print(f"Starting Deck: {dealt_sorted_deck}")

        shuffled_deck = shuffle_deck(dealt_sorted_deck)
        print(f"Shuffled Deck: {shuffled_deck}")

        game_players = int(input("How many players? "))
        game_cards_each = int(input("How many cards each? "))

        hands = play_a_game(shuffled_deck, game_players, game_cards_each)
        print(f"Dealt Hands: {hands}")
        sorted_hands = [sort_hand(hand, dealt_sorted_deck) for hand in hands]
        print(f"Sorted Hands: {sorted_hands}")

        scores = [score_hand(hand, rank, suit) for hand in hands]
        winner = scores.index(max(scores))
        print(f"Player {winner + 1} wins with {sorted_hands[winner]}")
        unique_scores = sorted(set(scores), reverse=True)
        rank_indx = {score: rank for rank, score in enumerate(unique_scores)}
        ranks = [rank_indx[score] for score in scores]
        print(f"Player Scores: {scores}")
        print(f"Player Ranks: {ranks}")
        for rank in range(game_players):
            rank_indices = [i for i, v in enumerate(ranks) if v == rank]
            for h in rank_indices:
                print(f"Player {h + 1} had {sorted_hands[h]} for a score of {scores[h]} and rank {ranks[h] + 1}")
    except:
        print("Oh no! There was an error with the card game.")

if __name__ == '__main__':
    main()
