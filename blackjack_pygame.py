import pygame as pygame
from blackjack_deck import *
from constants import *
import sys
import time
import os

FPS = 60
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BlackJack')



screen.fill(background_color)
pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#game text display
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
    
#button display
def button(msg, x, y, w, h, ic, ac, action=None, event = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None and event.type == pygame.MOUSEBUTTONDOWN:
                action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


class Play:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        
    def blackjack(self):

        self.dealer.calc_hand()
        self.player.calc_hand()

        image_path = os.path.join(script_dir, 'img', self.dealer.card_img[1] + '.png')

        show_dealer_card = pygame.image.load(image_path).convert()
        
        if self.player.value == 21 and self.dealer.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Both with BlackJack!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("You got BlackJack!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.dealer.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Dealer has BlackJack!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0
        self.dealer.value = 0

    def deal(self):
        for i in range(2):
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        dealer_card = pygame.image.load(os.path.join(script_dir, 'img', self.dealer.card_img[0] + '.png')).convert()
        dealer_card_2 = pygame.image.load(os.path.join(script_dir, 'img', 'back.png')).convert()
            
        player_card = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[0] + '.png')).convert()
        player_card_2 = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[1] + '.png')).convert()

        
        game_texts("Dealer's hand is:", 500, 150)

        screen.blit(dealer_card, (400, 200))
        screen.blit(dealer_card_2, (550, 200))

        game_texts("Your's hand is:", 500, 400)
        
        if self.player.card_img:
            player_card = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[0] + '.png')).convert()
            screen.blit(player_card, (300, 450))

        if len(self.player.card_img) > 1:
            player_card_2 = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[1] + '.png')).convert()
            screen.blit(player_card_2, (410, 450))
        self.blackjack()
            
            

    def hit(self):
        self.player.add_card(self.deck.deal())
        self.blackjack()
        self.player_card += 1

        image_path = os.path.join(script_dir, 'img', self.dealer.card_img[1] + '.png')
        
        if self.player_card == 2:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[2] + '.png')).convert()
            screen.blit(player_card_3, (520, 450))

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load(os.path.join(script_dir, 'img', self.player.card_img[3] + '.png')).convert()
            screen.blit(player_card_4, (630, 450))
                
        if self.player.value > 21:
            show_dealer_card = pygame.image.load(image_path).convert()
            screen.blit(show_dealer_card, (550, 200))
            game_finish("You Busted!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0

        if self.player_card > 4:
            sys.exit()
            
            
    def stand(self):
        image_path = os.path.join(script_dir, 'img', self.dealer.card_img[1] + '.png')

        show_dealer_card = pygame.image.load(image_path).convert()
        screen.blit(show_dealer_card, (550, 200))
        self.blackjack()
        self.dealer.calc_hand()
        self.player.calc_hand()
        if self.player.value > self.dealer.value:
            game_finish("You Won!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
        else:
            game_finish("It's a Tie!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
        
    
    def exit(self):
        sys.exit()
    
    def play_or_exit(self):
        game_texts("Play again press Deal!", 200, 80)
        time.sleep(3)
        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        screen.fill(background_color)
        pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))
        pygame.display.update()

        
play_blackjack = Play()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.blit(background_image, (0, 0))    
        button("Deal", 30, 100, 150, 50, light_slat, dark_slat, play_blackjack.deal, event)
        button("Hit", 30, 200, 150, 50, light_slat, dark_slat, play_blackjack.hit, event)
        button("Stand", 30, 300, 150, 50, light_slat, dark_slat, play_blackjack.stand, event)
        button("EXIT", 30, 500, 150, 50, light_slat, dark_red, play_blackjack.exit, event)
    
    pygame.display.flip()
    clock.tick(FPS)
