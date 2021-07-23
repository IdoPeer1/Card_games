import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show_card(self):
        print(str(self.value) + " of " + str(self.suit))

class Deck():
    deck = []

    def __init__(self):
        self.create_deck()

    def create_deck(self):
       for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
             for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                 self.card_list.append(Card(v, s))

    def shuffle(self):
        return random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()
