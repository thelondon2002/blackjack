import random

# the name of the game is blackjack

# user, dealer

# deck of cards with values (2 - 10, J,K,Q = 10, A = 1/11)

# user given 1 card, dealer next, user, then dealer

# user, dealer given option to hit or stand

# random generator of certain amount of cards being dealt

# if Q, J, K paired with A = automatic WindowsError

# balance? (later)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]
        random.shuffle(self.cards)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)

        self.value += values[card.rank]

        if card.rank == 'A':
            self.aces += 1
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1




deck = Deck()


print("-----------------------------------------------------------------------------------------------------------------")
print("|                                                                                                               |")
print("|     B B B      L            A          C C C     K     K       J J J J       A          C C C     K     K     |")
print("|     B    B     L           A A        C          K   K            J         A A        C          K   K       |")
print("|     B B B      L          A   A       C          K K              J        A   A       C          K K         |")
print("|     B    B     L         A A A A      C          K   K            J       A A A A      C          K   K       |")
print("|     B B B      L L L    A       A      C C C     K     K     J J J       A       A      C C C     K     K     |")
print("|                                                                                                               |")
print("-----------------------------------------------------------------------------------------------------------------")
print("By London Haith\n\n\n")









values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

player_hand = Hand()
dealer_hand = Hand()
player_hand.add_card(deck.cards.pop())
dealer_hand.add_card(deck.cards.pop())
player_hand.add_card(deck.cards.pop())
dealer_hand.add_card(deck.cards.pop())

def get_player_action():
    while True:
        action  = input("What do you say champ, hit or stand?").lower()
        if action in ['hit', 'stand']:
            return action
        else:
            print("Invalid input. Please input either 'hit' or 'stand'.")

def display_partial_dealer_hand(dealer_hand):
    print("-------------------")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print(f"| {dealer_hand.cards[0].rank} of {dealer_hand.cards[0].suit}      |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|-----------------|")
    print("Dealer's Hand \n\n")


def display_player_hand(player_hand):
    print("-------------------")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print(f"| {player_hand.cards[0].rank} of {player_hand.cards[0].suit}      |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|-----------------|")
    print("Player's Hand \n\n")

def display_final_hands(player_hand, final_hand):
    print("Dealer's Hand: \n")
    print("-------------------")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    for i, card in enumerate(dealer_hand.cards):
        print(f"|  {i + 1}: {card.rank} of {card.suit}    |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("|-----------------|\n\n")

    print("Player's Hand: \n")
    print("-----------------")
    print("|               |")
    print("|               |")
    for i, card in enumerate(player_hand.cards):
        print(f"|  {i + 1}: {card.rank} of {card.suit}    |")    
    print("|               |")
    print("|               |")
    print("|               |")
    print("|               |")
    print("|---------------|\n\n")


def determine_winner(player_hand, dealer_hand):
    if player_hand.value > 21:
        return "Dealer"
    elif dealer_hand.value > 21:
        return "Player"
    elif player_hand.value > dealer_hand.value:
        return "Player"
    elif dealer_hand.value > player_hand.value:
        return "Dealer"
    else:
        return "Tie"
    

def display_winner(winner):
    if winner == "Player":
        print("Hey!!!!! Keep Spending your money here, I feel a mega win coming!")
    elif winner == "Dealer":
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⢀⣐⣶⣯⣴⣖⣲⣛⡻⢿⡷⠿⣯⣽⣶⣖⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣋⣽⣿⠟⢊⠉⣽⡿⠟⣫⣿⣯⣽⣞⡶⣶⣏⣿⣙⠳⢦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⡻⣯⣿⣿⣿⣿⣲⣏⣽⣿⣿⣿⣿⣿⢯⠽⢿⣍⣛⠻⣯⣅⣀⡈⠙⢷⣄⠄⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣸⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⢿⠙⠻⣧⣜⡍⠹⡟⢻⣿⣏⣉⠳⠀⠙⢷⣤⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣽⣿⣿⣿⣿⣿⣿⣅⣿⢟⣷⡾⣛⣉⣟⣹⡿⣋⠓⠾⣢⣦⣭⡙⢻⡶⠾⠶⣄⠹⣯⣦⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣼⣻⣿⣿⣿⣿⣿⣿⣽⢿⣟⣥⠷⣍⣴⣿⢿⣬⣽⣭⣍⣩⣽⣟⣛⣻⣟⣽⣷⡤⣤⣙⢻⣯⡻⣮⣂⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣶⣶⡽⠷⢾⡷⣿⣿⣉⣉⢛⠻⢗⣎⣻⠷⠾⣽⣗⡘⢿⣿⣿⢷⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣾⣻⠇⣼⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣿⣿⣷⣛⠿⢿⣷⣭⣽⣿⣿⣿⣦⣽⣯⡁⠘⢿⡜⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢩⣿⣴⣿⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣭⠼⣽⣛⠷⣗⣾⡿⠭⠿⢽⣿⣿⣄⠹⣦⢸⣇⡇")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣴⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣟⠟⢛⡻⢿⣿⣟⣚⣻⡿⢿⣿⣿⣷⣶⣾⣇⠙⢧⣌⣸⡿⡇")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢻⣯⣾⣟⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣿⣿⣿⣿⣯⣿⣿⣶⢿⣷⣿⡿⢻⣯⡻⣄⠉⠻⣷⠇")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣾⣿⣿⣿⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣷⡌⣲⣿⣦⣶⣶⣭⣿⣿⣷⠀⢿⡷")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⡿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⡠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣿⣧⣿⣿⣿⣌⣧⣿⣿⣿⣟⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣾⣿⣼⣽⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⡿⣽⣿⢿⣿⣿⠗⣿⣿⣿⣿⢯⡽⡋⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣾⣧⣿⣯⣼⣿⣿⣀⣿⣿⣿⣿⣿⣗⣈⣉⣽⣾⣿⣿⣿⣿⣿⣿⣿⠚⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⡄⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣿⢻⣿⢿⣿⣿⣿⡟⣁⣛⣿⣿⣿⣷⣿⣿⣿⣻⣿⣿⢿⣿⣽⣿⣿⣦⡦⢼⣿⣿⣟⣿⣿⣿⡟⠉⢻⣾⢣⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⡇⣿⣿⣾⣿⣿⣿⣷⣟⡻⢽⣿⣿⣿⣟⣛⣟⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢶⡎⣱⠒⠃⣾⢿⠏⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⣿⡗⠩⣿⡵⣿⣿⣿⣿⣿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⡉⢿⣿⠋⢀⣿⣿⠄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⢹⣿⠷⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢿⣿⣿⢿⣿⡷⣿⣿⣿⣟⣟⢛⢿⣉⣁⢺⣿⣿⣈⡉⣿⣿⣲⣿⠏⠁⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⣠⢾⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣷⣿⣿⡿⣿⠀⣙⣷⣿⣻⣿⡿⣿⣯⣿⣮⣼⣿⣿⣿⣹⣿⡿⠃⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢀⡼⢛⣨⢾⣿⡾⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⠿⡿⠉⠛⠋⡻⠃⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀")
        print("⢴⠶⢶⣎⣩⣡⣽⣿⣿⡽⣾⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⡟⢋⢝⠉⠻⢿⣿⣴⣿⣿⣧⡴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠒⠷⢖⠚⣟⣿⣿⡞⢻⣛⠟⡗⡾⡘⢻⣿⣿⣿⣿⣿⡛⢿⡿⠿⠟⢿⠛⠿⣿⣾⣿⣿⣶⣠⣷⣾⣿⡟⡻⣺⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print(".....maybe next time.")
    else:
        print("Tie, play one more time. I can feel that big win coming.")




while True:
    display_partial_dealer_hand(dealer_hand)
    display_player_hand(player_hand)


    action = get_player_action()


    if action == 'hit':
         player_hand.add_card(deck.cards.pop())
    elif action == 'stand':
         break


while dealer_hand.value < 17:
    dealer_hand.add_card(deck.cards.pop())


display_final_hands(player_hand, dealer_hand)

winner = determine_winner(player_hand, dealer_hand)

display_winner(winner)

