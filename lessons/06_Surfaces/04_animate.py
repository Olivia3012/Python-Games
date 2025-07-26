import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path
import random

images = Path(__file__).parent / 'images'
color = (255, 51, 255)
lilly_color = (29, 173, 75)
lilly_inside_color = (255, 51, 255)
frame_count = 0
frames_per_image = 5
pygame.font.init()
font = pygame.font.SysFont("nototraditionalnushu", 30)
print(pygame.font.get_fonts())
GameOver = False  


def scale_sprites(sprites, scale):
    """Scale a list of sprites by a given factor.

    Args:
        sprites (list): List of pygame.Surface objects.
        scale (int): Scale factor. 

    Returns:
        list: List of scaled pygame.Surface objects.    """
    return [pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale)) for sprite in sprites]

class Frog(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        filename = images / 'spritesheet.png'  # Replace with your actual file path
        cellsize = (16, 16)  # Replace with the size of your sprites
        spritesheet = SpriteSheet(filename, cellsize)
        self.frog_sprites = scale_sprites(spritesheet.load_strip(0, 4, colorkey=-1) , 2)
        self.image = self.frog_sprites[0]
        self.frog_position_x = x
        self.frog_position_y = y
        self.rect = self.image.get_rect()
        self.rect[0] = self.frog_position_x
        self.rect[1] = self.frog_position_y
        self.frog_index = 0
        
    def update(self):
        print(frame_count + 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        if frame_count % frames_per_image == 0: 
            self.frog_index = (self.frog_index + 1) % len(self.frog_sprites)                                      
            self.image = self.frog_sprites[self.frog_index]
    

class Alligator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        filename = images / 'spritesheet.png'  # Replace with your actual file path
        cellsize = (16, 16)  # Replace with the size of your sprites
        spritesheet = SpriteSheet(filename, cellsize)
        self.allig_sprites = scale_sprites(spritesheet.load_strip( (0, 4), 7, colorkey=-1), 3)
        self.rect = self.allig_sprites[0].get_rect()
        self.rect[0] = 25
        self.rect[1] = 300
        self.rect[2] = 48
        self.rect[3] = 16 * 3
        self.allig_index = 0

        width = self.rect[2]
        height = self.rect[3]
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)

        composed_image.blit(self.allig_sprites[0], (0, 0))
        composed_image.blit(self.allig_sprites[1], (width, 0))
        composed_image.blit(self.allig_sprites[2], (width * 2, 0))

        self.image = composed_image


    def draw_alligator(self, alligator, index):
        
        index = index % (len(alligator)-2)

        width = self.rect[2]
        height = self.rect[3]
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)
        print(pygame.SRCALPHA)

        composed_image.blit(self.allig_sprites[0], (0, 0))
        composed_image.blit(self.allig_sprites[1], (width, 0))
        composed_image.blit(self.allig_sprites[(index + 2) % len(self.allig_sprites)], (width * 2, 0))

        self.image = composed_image
    
    def update(self):
        if frame_count % frames_per_image == 0: 
                self.allig_index = (self.allig_index + 1) % len(self.allig_sprites)
        self.draw_alligator(self.allig_sprites, self.allig_index)
        print("working")
            




def main():
    global frame_count
    
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((640, 600))
    pygame.display.set_caption("Frog jump game")

    # Load the sprite sheet
    filename = images / 'spritesheet.png'  # Replace with your actual file path
    cellsize = (16, 16)  # Replace with the size of your sprites
    spritesheet = SpriteSheet(filename, cellsize)

    frog = Frog(100, 100)
    grog = Frog(200, 100)

    frog_group = pygame.sprite.Group()
    frog_group.add(frog)
    frog_group.add(grog)
    
    alligator = Alligator()
    alligator_group = pygame.sprite.GroupSingle(alligator)
    # Load a strip sprites
    """allig_sprites = scale_sprites(spritesheet.load_strip( (0, 4), 7, colorkey=-1), 3)"""

    # Compose an image
    log = spritesheet.compose_horiz([24, 25, 26], colorkey=-1)
    log = pygame.transform.scale(log, (log.get_width() * 4, log.get_height() * 4))

    # Variables for animation
    """allig_index = 0"""
    frames_per_image = 5
 
    
    log_position_x = 50
    log_position_y = 300

    """alligator_position_x = 25
    alligator_position_y = 300"""

    line_length = 75
    
    # Main game loop
    running = True
    
    log_sprite_rect = log.get_rect()
    log_sprite_rect[0] = log_position_x
    log_sprite_rect[1] = log_position_y

    """alligator_sprite_rect = allig_sprites[0].get_rect()
    alligator_sprite_rect[0] = alligator_position_x
    alligator_sprite_rect[1] = alligator_position_y"""
    

    
    
    pygame.math.Vector2(1, 0)

    """
    def draw_alligator(alligator, index):
        #Creates a composed image of the alligator sprites.

        Args:
            alligator (list): List of alligator sprites.
            index (int): Index value to determine the right side sprite.

        Returns:
            pygame.Surface: Composed image of the alligator.
        
        
        index = index % (len(alligator)-2)
        
        width = alligator[0].get_width()
        height = alligator[0].get_height()
        composed_image = pygame.Surface((width * 3, height), pygame.SRCALPHA)

        composed_image.blit(alligator[0], (0, 0))
        composed_image.blit(alligator[1], (width, 0))
        composed_image.blit(alligator[(index + 2) % len(alligator)], (width * 2, 0))

        return composed_image
    """
    
    line_start_pos = pygame.Vector2(frog.frog_position_x+15, frog.frog_position_y)
    line_end_pos = pygame.Vector2(frog.frog_position_x+15, frog.frog_position_y - line_length)
    jumping = False
    new_line = pygame.Vector2(line_end_pos - line_start_pos)
    n1 =167
    n2 = 20
    n3 = 611
    n4 = 376
    n5 = 25 
    
      
    while GameOver == False:
        screen.fill(pygame.Color(0, 0, 139, 254))  # Clear screen with deep blue

        # Update animation every few frames
        frame_count += 1
        
        # Get the current sprite and display it in the middle of the screen

        lilly_pad2 = pygame.draw.circle(screen, lilly_color, (line_start_pos[0] + 0.8, line_start_pos[1] + 10), 15)

        """composed_alligator = draw_alligator(allig_sprites, allig_index)
        screen.blit(composed_alligator,  alligator_sprite_rect.move(0, 100))"""

        screen.blit(log,  log_sprite_rect.move(0, -100))
        screen.blit(log,  log_sprite_rect.move(210, -15))
        screen.blit(log,  log_sprite_rect.move(300, -250))

        frog_group.update()
        alligator_group.update()
        frog_group.draw(screen)
        alligator_group.draw(screen)

        keys = pygame.key.get_pressed()

        frog_jump_line = pygame.draw.line(screen, color, line_start_pos, line_end_pos, width=2)

        pygame.draw.circle(screen, lilly_color, (n1, 50), 15)
        pygame.draw.circle(screen, lilly_inside_color, (n1, 50), 5)
        pygame.draw.circle(screen, lilly_color, (n2, 100), 15)
        pygame.draw.circle(screen, lilly_color, (n3, 176), 15)
        pygame.draw.circle(screen, lilly_color, (n4, 294), 15)
        pygame.draw.circle(screen, lilly_color, (n4, 278), 10)
        pygame.draw.circle(screen, lilly_color, (n5, 401), 15)
        n1 += random.randint(-1, 2)
        n2 += random.randint(1, 6)
        n3 += random.randint(-1, 2)
        n4 += random.randint(1, 5)
        n5 += random.randint(1, 3)

        if n1 > 640:
            n1 = 0

        if n2 > 640:
            n2 = 0

        if n3 > 640:
            n3 = 0

        if n4 > 640:
            n4 = 0

        if n5 > 640:
            n5 = 0
        
        if frog.rect[0] > 640:
            frog.rect[0] = 630
            print("Jump line is off the map!")
        if frog.rect[0] < 0:
            frog.rect[0] = 10
            print("Jump line is off the map!")
        if frog.rect[1] > 600:
            frog.rect[1] = 470
            print("Jump line is off the map!")
        if frog.rect[1] < 0:
            frog.rect[1] = 10
            print("Jump line is off the map!")
        
        frog_end_pos = line_end_pos
        
        if keys[pygame.K_UP]:
            line_length += 5

        if keys[pygame.K_DOWN]:
            line_length -= 5
                
        if keys[pygame.K_RIGHT]:
            new_line = (line_end_pos - line_start_pos).rotate(4)
            line_end_pos = line_start_pos + new_line
            print("Going right")
            
        if keys[pygame.K_LEFT]:
            print("Going left")
            new_line = (line_end_pos - line_start_pos).rotate(-4)
            line_end_pos = line_start_pos + new_line

        if keys[pygame.K_SPACE]:
            if jumping == False:
                """frog_sprite_rect[0] = frog_end_pos[0] + 15
                frog_sprite_rect[1] = frog_end_pos[1]"""
                frog.rect = frog_end_pos
                line_start_pos = pygame.Vector2(frog.rect[0], frog.rect[1])
                line_end_pos = pygame.Vector2(line_start_pos[0] + new_line[0], line_start_pos[1] + new_line[1])
                print("working")
                jumping = True

        else:
            jumping = False


        """collider = pygame.sprite.groupcollide(frog_sprite_rect, log_sprite_rect, True, True, collided = None)
        if collider:
            print("You have been stunned, so your jump length is smaller.")
            line_lenth -= 25"""
        
           
        text = font.render("Phrogger Game", True, (0, 0, 0))
        screen.blit(text, (10, 10))  

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
