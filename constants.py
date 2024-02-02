import pygame as pygame
import sys
import os


display_width = 900
display_height = 700
pygame.init()
background_color = (0,110,34)
grey = (92, 90, 84)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (255, 255, 255)
dark_slat = (220,220,220)
dark_red = (255, 0, 0)
font = pygame.font.SysFont("impact", 20)
textfont = pygame.font.SysFont('Arial', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('couriernew', 70)


script_dir = os.path.dirname(os.path.abspath(__file__))

background_image_path = os.path.join(script_dir, "img", "background.png")
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (display_width, display_height))


SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

CARD_WIDTH = 130
CARD_HEIGHT = 150



