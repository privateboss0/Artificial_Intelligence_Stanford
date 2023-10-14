#Work in progress as it contains some minor bugs still working on the fixes

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def dealerhand(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) >= 1:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Dream:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            try:
                card_value = int(card.rank)
            except ValueError:
                card_value = 11 if card.rank == "A" else 10

            self.value += card_value
            if card.rank == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def black_jack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if hasattr(self, "dealer") and self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.black_jack:
                print("hidden")
            else:
                print(card)

        if hasattr(self, "dealer") and not self.dealer:
            print("Value:", self.get_value())

class Game:
    def play(self):
        game_number = 0
        game_play = 0

        while game_play <= 0:
            try:
                game_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number to continue.")

        while game_number < game_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Dream()
            dealer_hand = Dream(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.dealerhand(1))
                dealer_hand.add_card(deck.dealerhand(1))

            print()
            print("*" * 30)
            print(f"Game{game_number} of {game_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_for_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["S", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' or (H/S)").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.dealerhand(1))
                    player_hand.display()

            if self.check_for_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.dealerhand(1))
                dealer_hand_value = dealer_hand.get_value

            dealer_hand.display(show_all_dealer_cards = True)

            if self.check_for_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_for_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing! Hope you see you soon again!")
            
    def check_for_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted😔... Dealer wins😭...TRY AGAIN!!")
                return True

            elif dealer_hand.get_value() > 21:
                print("Dealer busted😂... You Win🕺🏿💃...PLAY AGAIN!!")
                return True
                
            elif dealer_hand.black_jack() and player_hand.black_jack():
                print("Both players have blackjack..its a tie😐... PLAY AGAIN!! ")
                return True

            elif player_hand.black_jack():
                print("You have blackjack. You win!🔥🏃🏾‍♂️🏃🏾‍♂️🧊")
                return True

            elif dealer_hand.black_jack():
                print("Dealer has blackjack. Dealer wins😭. TRY AGAIN!!")
                return True

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win🕺🏿💃...PLAY AGAIN!!")

            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie😐..PLAY AGAIN!!!")
                
            else:
                print("Dealer wins😭. TRY AGAIN!!")
            return True
        return False

g = Game()
g.play()
