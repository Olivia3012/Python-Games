import pygame

import random

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Color Background + scroll')
background1_x = 0
background2_x = 600


def tile_colors(screen, num_tiles):
    image = pygame.Surface([screen_width, screen_height])
    tile = pygame.Surface((screen_width/num_tiles, screen_height))
    
    for i in range(num_tiles):
        tile.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        image.blit(tile, (i*(screen.get_width()/num_tiles), 0))
        

    return image
    

background1 = tile_colors(screen, 599)
background2 = tile_colors(screen, 599)


        
    
# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    screen.blit(background1,(background1_x, 0))
    screen.blit(background2, (background2_x, 0))

    background1_x -= 2
    background2_x -= 10

    if background1_x  < -600 :
        background1_x = 600

    if background2_x < -600 :
        background2_x = 600
    
    

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()





    

    



"""pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')

def make_tiled_bg(screen, bg_file):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    
    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image

background = make_tiled_bg(screen, assets/'background_tile.gif')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
"""