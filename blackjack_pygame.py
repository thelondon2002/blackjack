import pygame
from constants import *
import sys
import time
import os
import random

FPS = 60
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BlackJack')


screen.fill(background_color)
pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

 
def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def black_jack(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, blackjack, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
  
    def shuffle(self):
        random.shuffle(self.cards)
        

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
            
class Hand():
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 

    def add_card(self, card):
        if card is not None:
            self.cards.append(card)

    def calc_hand(self):
        self.value = 0
        aces_count = 0

        for card in self.cards:
            card_value = card[0]

            if card_value in 'JQK':
                self.value += 10
            elif card_value == 'A':
                aces_count += 1
            else:
                self.value += int(card_value)

        for _ in range(aces_count):
            if self.value + 11 <= 21:
                self.value += 11
            else:
                self.value += 1

    def display_cards(self):
        self.card_img = self.cards
        for card in self.cards:
            if card is not None:
                if card not in self.card_img:
                    self.card_img.append(card)
                

deck = Deck()
deck.shuffle()

player = Hand()
dealer = Hand()

for i in range(2):
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())


player.display_cards()
dealer.display_cards()


player.add_card(deck.deal())
             

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        self.round_in_progress = False
        self.deal_occurred = False
    
    def end_round(self, message, color):
        self.game_finish(message, 300, 150, color)
        time.sleep(4)
        self.play_or_exit()

    def clear_screen(self):
        screen.blit(background_image, (0,0))
 
    def play_or_exit(self):
        self.clear_screen()
    
        self.round_in_progress = False
        waiting_for_input = True

        game_texts("Click Deal to Play Again!", 450, 300)
        
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting_for_input = False

            self.clear_screen()
            
            screen_height = screen.get_height()
            button("Deal", 70, screen_height - 130, 150, 50, light_slat, dark_slat, self.deal)
            button("Hit", 270, screen_height - 130, 150, 50, light_slat, dark_slat, self.hit)
            button("Stand", 470, screen_height - 130, 150, 50, light_slat, dark_slat, self.stand)
            button("EXIT", 670, screen_height - 130, 150, 50, light_slat, dark_red, self.exit)

            pygame.display.update()

        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        self.round_in_progress = False
    
        
    def blackjack(self):

        self.dealer.calc_hand()
        self.player.calc_hand()
        self.deal_occurred = False

        image_path_hidden = os.path.join(script_dir, 'img', 'back.png')
        image_path_reveal = os.path.join(script_dir, 'img', self.dealer.card_img[1][0] + self.dealer.card_img[1][1] + '.png')


        show_dealer_card = pygame.image.load(image_path_reveal).convert()
        
        
        if self.dealer.value == 21:
            
            show_hidden_card = pygame.image.load(image_path_reveal).convert()
            card_width = int(show_hidden_card.get_width() * 0.5)
            card_height = int(show_hidden_card.get_height() * 0.5)
            screen.blit(show_hidden_card, (30 + card_width + 10, 200))
            black_jack("Dealer has Blackjack!", 400, 150, red)
            time.sleep(4)
            self.play_or_exit()
        else:
            
            show_hidden_card = pygame.image.load(image_path_hidden).convert()
            show_hidden_card = pygame.transform.scale(show_hidden_card, (CARD_WIDTH, CARD_HEIGHT))
            card_width = int(show_hidden_card.get_width() * 0.5)
            card_height = int(show_hidden_card.get_height() * 0.5)
            screen.blit(show_hidden_card, (30, 200))

        if self.player.value == 21 and self.dealer.value == 21:
            screen.blit(show_hidden_card, (400, 200))
            black_jack("Both with BlackJack!", 400, 150, grey)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            screen.blit(show_dealer_card, (400, 200))
            black_jack("You got BlackJack!", 400, 150, green)
            time.sleep(4)
            self.play_or_exit()
            
        pygame.display.update()
        self.player.value = 0
        self.dealer.value = 0

    def deal(self):
        if not self.round_in_progress:
            if not self.dealer.card_img:
                back_card = pygame.image.load(os.path.join(script_dir, 'img', 'back.png')).convert()
                back_card = pygame.transform.scale(back_card, (CARD_WIDTH , CARD_HEIGHT))
                screen.blit(back_card, (30, 200))
                pygame.display.update()
            

            for i in range(2):
                self.dealer.add_card(self.deck.deal())
                self.player.add_card(self.deck.deal())


            self.dealer.display_cards()
            self.player.display_cards()
            self.round_in_progress = True
            self.deal_occurred = True


            game_texts("The Dealer's Hand:", 180, 70)
            game_texts("The Player's Hand:", 690, 70)


            for i in range(2):
                if i == 0:
                    back_card = pygame.image.load(os.path.join(script_dir, 'img', 'back.png')).convert()
                    back_card = pygame.transform.scale(back_card, (CARD_WIDTH , CARD_HEIGHT))
                    screen.blit(back_card, (30 + i * (CARD_WIDTH + 10), 200))

                else:
                    card_value, card_suit = self.dealer.card_img[i]
                    dealer_card = pygame.image.load(os.path.join(script_dir, 'img', f'{card_value}{card_suit}.png')).convert()
                    dealer_card = pygame.transform.scale(dealer_card, (CARD_WIDTH, CARD_HEIGHT))
                    screen.blit(dealer_card, (30 + i * (CARD_WIDTH + 10), 200))

                player_card_value, player_card_suit = self.player.card_img[i]
                player_card = pygame.image.load(os.path.join(script_dir, 'img', f'{player_card_value}{player_card_suit}.png')).convert()
                image_path = os.path.join(script_dir, 'img', f'{player_card_value}{player_card_suit}.png')
                player_card = pygame.transform.scale(player_card, (CARD_WIDTH, CARD_HEIGHT))
                screen.blit(player_card, (display_width - 250 + i * (CARD_WIDTH + 10), 200))

            
            pygame.display.update()
        
        pygame.display.update()

            

    def hit(self):
        if self.round_in_progress:
            if self.player.value <= 21:
                new_card = self.deck.deal()
                self.player.add_card(new_card)
                self.player.calc_hand()

                card_value, card_suit = new_card
                player_card = pygame.image.load(os.path.join(script_dir, 'img', f'{card_value}{card_suit}.png')).convert_alpha()
                player_card = pygame.transform.scale(player_card, (CARD_WIDTH, CARD_HEIGHT))
                screen.blit(player_card, (display_width - 250 + len(self.player.cards) * (CARD_WIDTH + 10), 200))

                pygame.display.update()

                for i, card_img in enumerate(self.player.card_img):
                    player_card_value, player_card_suit = card_img
                    player_card = pygame.image.load(os.path.join(script_dir, 'img', f'{player_card_value}{player_card_suit}.png')).convert()
                    player_card = pygame.transform.scale(player_card, (CARD_WIDTH, CARD_HEIGHT))
                    screen.blit(player_card, (display_width - 250 + i * (CARD_WIDTH + 10), 200))
                    
                pygame.display.update()

                if self.player.value > 21:
                    game_finish("You Busted!", 450, 350, red)
                    time.sleep(4)
                    self.play_or_exit()
    
    def stand(self):
        card_value, card_suit = self.dealer.card_img[1]
        image_path = os.path.join(script_dir, 'img', f'{card_value}{card_suit}' + '.png')

        for i, card_img in enumerate(self.dealer.card_img[:2]):
            dealer_card_value, dealer_card_suit = card_img
            dealer_card = pygame.image.load(os.path.join(script_dir, 'img', f'{dealer_card_value}{dealer_card_suit}.png')).convert()
            dealer_card = pygame.transform.scale(dealer_card, (CARD_WIDTH, CARD_HEIGHT))
            screen.blit(dealer_card, (30 + i * (CARD_WIDTH + 10), 200))
  
        for i, card_img in enumerate(self.player.card_img[:2]):
            player_card_value, player_card_suit = card_img
            player_card = pygame.image.load(os.path.join(script_dir, 'img', f'{player_card_value}{player_card_suit}.png')).convert()
            player_card = pygame.transform.scale(player_card, (CARD_WIDTH, CARD_HEIGHT))
            screen.blit(player_card, (display_width - 250 + i * (CARD_WIDTH + 10), 200))
  
        pygame.display.update()

        self.dealer.calc_hand()
        self.player.calc_hand()

        if self.player.value > self.dealer.value:
            game_finish("You Won!", 450, 350, green)
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 450, 350, red)
        else:
            game_finish("It's a Tie!", 450, 350, grey)

        time.sleep(4)
        self.play_or_exit()

        
    
    def exit(self):
        sys.exit()
    

    screen.fill(background_color)
    pygame.draw.rect(screen, background_color, pygame.Rect(0, 0, 250, 700))
    pygame.display.update()

        
play_blackjack = BlackJack()
deal_button_clicked = False

def button(msg, x, y, w, h, ic, ac, action=None):
    global deal_button_clicked

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
                action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


running = True
waiting_for_input = True
screen_height = screen.get_height()
deal_button_clicked = False

screen.blit(background_image, (0,0))

while running:
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_blackjack.exit()
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        button("Deal", 70, screen_height - 130, 150, 50, light_slat, dark_slat, play_blackjack.deal)
        button("Hit", 270, screen_height - 130, 150, 50, light_slat, dark_slat, play_blackjack.hit)
        button("Stand", 470, screen_height - 130, 150, 50, light_slat, dark_slat, play_blackjack.stand)
        button("EXIT", 670, screen_height - 130, 150, 50, light_slat, dark_red, play_blackjack.exit)

        if play_blackjack.deal_occurred:
            play_blackjack.dealer.display_cards()
            play_blackjack.player.display_cards()


        pygame.display.update()
        clock.tick(FPS)
