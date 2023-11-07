import random

# Write your blackjack game here.
# C - card
# R - value, suit, rank, know where it is in deck
# C - Deck
SUITS = ['♥️', '♦️', '♣️', '♠️']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# C - deck
# R - is shuffled, card dealt from it, holds the cards in an order,
# C - Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                if card.rank == 'A':
                    card.value = 11
                elif card.rank in range(2, 11):
                    card.value = rank
                else:
                    card.value = 10

                print(card)
                self.cards.append(card)
        print(f'There are {len(self.cards)} in this deck.')

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def look_at_hand(self):
        '''Shows cards in hand to player'''
        for card in self.hand:
            print(card)

    def calculate_hand_value(self):
        '''return the total value of the hand'''
        # add value of each card together and print total
        hand_total = 0
        for card in self.hand:
            hand_total += card.value
        return hand_total
        
    def has_ace(self):
        hand_total = self.calculate_hand_value()
        for card in self.hand:
            if card.rank == 'A' and hand_total > 21:
                hand_total -= 10
        return hand_total

class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        super().__init__('Dealer')


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(name=input("What is your name? "))
        self.dealer = Dealer()
        self.deal_cards()
        # self.player.look_at_hand()

    def deal_cards(self):
        '''Deal 2 cards each to the player and the dealer '''
        while len(self.player.hand) < 2 and len(self.dealer.hand) < 2:
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            card = self.deck.cards.pop()
            self.dealer.hand.append(card)
        print(f'{self.player} has {self.player.hand} \n'
              f'and {self.dealer} has {self.dealer.hand}')

    def hit(self, player):
        '''Deal one card to the selected player'''
        pass

# print(ace_of_spades)
# print(four_of_clubs)


new_game = Game()
ace_of_spades = Card("♠️", "A", 11)
new_game.player.hand.append(ace_of_spades)
# print(new_game.player.calculate_hand_value())
new_game.player.look_at_hand()
print(new_game.player.has_ace())
# TODO Add values of each hand so player and dealer can decide to hit or stay
