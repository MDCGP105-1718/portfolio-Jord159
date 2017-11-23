class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.suit == "Clubs" or self.suit == "Spades":
            self.colour = "Black"
        elif self.suit == "Diamonds" or self.suit == "Hearts":
            self.colour = "Red"

    def Set_Suit(self, suit):
        self.suit = suit
        if self.suit == "Clubs" or self.suit == "Spades":
            self.colour = "Black"
        elif self.suit == "Diamonds" or self.suit == "Hearts":
            self.colour = "Red"

    def Get_Suit(self):
        return self.suit

    def Set_Value(self, value):
        self.value = value

    def Get_Value(self):
        return self.value

    def Get_Colour(self):
        return self.colour

    def __str__(self):
        return self.value + " of " + self.suit


suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

class Deck(Card):
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for val in range(13):
                self.deck.append(Card(suits[suit], values(val)))


class Hand(Deck):
    def __init__(self):
        self.hand = []

    def Get_Hand(self):
        return self.hand

    def Deal(self, NumCards):
        for num in range(NumCards):
            
