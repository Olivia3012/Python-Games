import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path

images = Path(__file__).parent / 'images'
color = (255, 51, 255)


def scale_sprites(sprites, scale):
    """Scale a list of sprites by a given factor.

    Args:
        sprites (list): List of pygame.Surface objects.
        scale (int): Scale factor.

    Returns:
        list: List of scaled pygame.Surface objects.
    """
    return [pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale)) for sprite in sprites]

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Frog jump game")

    # Load the sprite sheet
    filename = images / 'spritesheet.png'  # Replace with your actual file path
    cellsize = (16, 16)  # Replace with the size of your sprites
    spritesheet = SpriteSheet(filename, cellsize)


    # Load a strip sprites
    frog_sprites = scale_sprites(spritesheet.load_strip(0, 4, colorkey=-1) , 1)
    allig_sprites = scale_sprites(spritesheet.load_strip( (0, 4), 7, colorkey=-1), 2)

    # Compose an image
    log = spritesheet.compose_horiz([24, 25, 26], colorkey=-1)
    log = pygame.transform.scale(log, (log.get_width() * 4, log.get_height() * 4))

    # Variables for animation
    frog_index = 0
    allig_index = 0
    frames_per_image = 5
    frame_count = 0
    
            
    frog_position_x = 300
    frog_position_y = 300

    log_position_x = 50
    log_position_y = 300

    alligator_position_x = 50
    alligator_position_y = 7

    

    # Main game loop
    running = True
    
    frog_sprite_rect = frog_sprites[0].get_rect()
    frog_sprite_rect[0] = frog_position_x
    frog_sprite_rect[1] = frog_position_y

    log_sprite_rect = log.get_rect()
    log_sprite_rect[0] = log_position_x
    log_sprite_rect[1] = log_position_y

    alligator_sprite_rect = allig_sprites[0].get_rect()
    alligator_sprite_rect[0] = alligator_position_x
    alligator_sprite_rect[1] = alligator_position_y

    end_pos = frog_sprite_rect.center - pygame.Vector2(0, 50)
    
    pygame.math.Vector2(1, 0)
    def draw_alligator(alligator, index):
        """Creates a composed image of the alligator sprites.

        Args:
            alligator (list): List of alligator sprites.
            index (int): Index value to determine the right side sprite.

        Returns:
            pygame.Surface: Composed image of the alligator.
        """
        
        index = index % (len(alligator)-2)
        
        width = alligator[0].get_width()
        height = alligator[0].get_height()
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)

        composed_image.blit(alligator[0], (0, 0))
        composed_image.blit(alligator[1], (width, 0))
        composed_image.blit(alligator[(index + 2) % len(alligator)], (width * 2, 0))

        return composed_image
    
    while running:
        screen.fill((0, 0, 139))  # Clear screen with deep blue

        # Update animation every few frames
        frame_count += 1
        
        if frame_count % frames_per_image == 0: 
            frog_index = (frog_index + 1) % len(frog_sprites)
            allig_index = (allig_index + 1) % len(allig_sprites)
        
        # Get the current sprite and display it in the middle of the screen

        
        screen.blit(frog_sprites[frog_index], frog_sprite_rect)

        composed_alligator = draw_alligator(allig_sprites, allig_index)
        screen.blit(composed_alligator,  alligator_sprite_rect.move(0, 100))

        screen.blit(log,  log_sprite_rect.move(0, -100))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
                frog_sprite_rect = end_pos

        pygame.draw.line(screen, color, frog_sprite_rect.center - pygame.Vector2(1, 0), end_pos, width=1)


        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
