import random


class Deck:
    diamond_symbol = u"\u2666"
    heart_symbol = u"\u2665"
    club_symbol = u"\u2663"
    spade_symbol = u"\u2660"
    suites = [diamond_symbol, heart_symbol, club_symbol, spade_symbol]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    value_worth = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 1}

    def __init__(self):
        self.deck = [vl + st for vl in Deck.values for st in Deck.suites]

    def new_deck(self):
        self.deck = [vl + st for vl in Deck.values for st in Deck.suites]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self, player_hand, dealer_hand):
        player_hand.append(self.deck[-1])
        player_hand.append(self.deck[-3])
        dealer_hand.append(self.deck[-2])
        dealer_hand.append(self.deck[-4])
        self.deck = self.deck[:-4]
        return [player_hand, dealer_hand]
