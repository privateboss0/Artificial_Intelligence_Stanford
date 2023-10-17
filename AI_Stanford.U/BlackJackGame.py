import secrets
#import cache

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

player_name = ''

playing = True

class Game:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Game(suit, rank))

    def __str__(self):
        deck_comp = ''
        for Game in self.deck:
            deck_comp += '\n '+Game.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        # Shuffle the deck using the secrets module
        for i in range(len(self.deck) - 1):
            random_index = secrets.randbelow(len(self.deck) - i) + i
            self.deck[i], self.deck[random_index] = self.deck[random_index], self.deck[i]

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Dream:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,Game):
        self.cards.append(Game)
        self.value += values[Game.rank]
        if Game.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

class Cache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

# Create a new Cache object
cache = Cache()

# Get the number of chips the player has
player_chips = cache.get(player_name)

# If the player's chips are not in the cache, Then get them from the database but no database in this project catch will remain empty
#if player_chips is None:
    #player_chips = get_player_chips_from_database(player_name)

# Set the player's chips in the cache
#cache.set(player_name, player_chips)

# Later, player chips can be called without having to query the database again but no database in this project
#player_chips = cache.get(player_name)

def take_bet(player_chips):
  while True:
    try:
      bet_amount = int(input('How many chips would you like to bet?: '))
    except ValueError:
      print('\nSorry, the number of chips must be a number!')
    else:
      if bet_amount > player_chips.total:
        print(f"\nSorry, your bet can't exceed {player_chips.total} chips.")
      else:
        player_chips.bet = bet_amount
        print(f"\nYour bet of {player_chips.bet} chips has been accepted - good luck!")
        break
    #cache.set(player_name, player_chips.total)
    
def introduction():
    global player_name
    print("\nWelcome to BlackJack! Get as close to 21 as you can without busting.\n\nThe Dealer will hit up to 17, Face cards count as 10 and Aces are 1/11.")
    player_name=input("The first round is about to begin, what is your name! ?: ")

def next_round():
    global player_name
    print("let's go another round! ")

def chip_count():
    global player_name
    print(f"{player_name}, your current chip count stands at {player_chips.total}")

def play_again():
    global player_name
    global playing
    while True:
        replay = input(f"{player_name}, would you like to play another round?: ").upper()
        if replay[0] == 'Y':
            return True
        elif replay[0] == 'N':
            print(f"\nThanks for playing - you leave the table with {player_chips.total} chips.")
            break
        else:
            print("Sorry, I don't understand what you are saying, do you want to play the next round, or not? Y or N!: ")
            continue

def total():
    global player_name
    while True:
        try:
            total = int(input(f'Hello {player_name}, how many chips will you be using this game?: '))
        except ValueError:
            print('\nSorry, the number of chips must be a number!')
        else:
            return total
            print(f"\nWelcome to the table - you currently have {total} chips to play with.")

def hit(deck,Dream):

    Dream.add_card(deck.deal())
    Dream.adjust_for_ace()

def hit_or_stand(deck,Dream):
    global player_name
    global playing
    while True:
        response = input(f"{player_name}, Would you like to hit or stand?: ")
        if response[0].upper() == 'H':
            hit(deck,Dream)
        elif response[0].upper() == 'S':
            print(f"{player_name} stands. It is the Dealer's turn")
            playing = False
        else:
            print("\nI can't understand what you are saying - are you hitting or standing?!")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand: ",*player.cards, sep='\n')
    print("Value of your cards: ",player.value)

def show_all(player,dealer):
    print("\nDealer's Hand: ",*dealer.cards, sep='\n')
    print("Dealer's Hand = ",dealer.value)
    print("\nPlayer's Hand: ",*player.cards, sep='\n')
    print("Player's Hand =  ",player.value)

def player_busts(player,dealer,chips):
    global player_name
    print(f"{player_name} busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    global player_name
    print(f"{player_name} wins the round!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer,chips):
    print("You have tied with the Dealer! It's a push, your chips have been refunded.")

counter = 0
while True:
    if counter > 0:
        next_round()
    elif counter == 0:
        introduction()

    deck = Deck()
    deck.shuffle()

    player_hand = Dream()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Dream()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips(total())

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing == True:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    if player_hand.value in range(0, 22):
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)

    chip_count()
    counter += 1
   
    if play_again() == True:
        continue
    else:
        break
