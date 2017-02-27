from random import shuffle


class Card(object):
    def __init__(self, rank, suit, isVisible = 'False'):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """Возращает количество очков которое дает карта"""
        return " A23456789TJQK".index(self.rank)

    def get_rank(self):
           return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

class Deck(object):
    def __init__(self):
        #ранги
        ranks = "A23456789TJQK"
        #масти
        suits = "Diamonds", "Spades", "Clubs", "Hearts"
        #генератор списків, що створює колоду з 52 карт
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()