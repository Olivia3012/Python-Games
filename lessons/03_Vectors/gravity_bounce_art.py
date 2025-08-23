import pygame
from dataclasses import dataclass
from jtlgames.vector20 import Vector20Factory
import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path
import random
images = Path(__file__).parent / 'images'




class Colors:
    """Constants for Colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0) 
    RED = (255, 0, 0)
    PLAYER_COLOR = (0, 0, 255)
    BACKGROUND_COLOR = (255, 255, 255)
    LINE_COLOR = (163, 212, 231)

def scale_sprites(sprites, scale):
    return [pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale)) for sprite in sprites]


@dataclass         
class GameSettings:
    """Settings for the game"""
    width: int = 500
    height: int = 500
    gravity: float = 0.3
    player_start_x: int = 100
    player_start_y: int = None
    player_v_y: float = 0  # Initial y velocity
    player_v_x: float = 4  # Initial x velocity
    player_width: int = 30
    player_height: int = 30
    player_jump_velocity: float = 1
    frame_rate: int = 100
    thrust = pygame.Vector2(2,1)
    


class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""
    
    def __init__(self, settings: GameSettings):
        pygame.init()

        self.settings = settings
        self.running = True

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pygame.time.Clock()

        # Turn Gravity into a vector
        self.gravity = pygame.Vector2(0, self.settings.gravity)

    def vec_to_center(self, pos):
        print("I am at", Player.posx, Player)

    def run(self):
        """Main game loop"""
        player = Player(self)
        player_group = pygame.sprite.Group()
        player_group.add(player)


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            player.update()

            #self.screen.fill(Colors.BACKGROUND_COLOR)
            player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.settings.frame_rate)

        pygame.quit() 

class Player(pygame.sprite.Sprite):
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        settings = self.game.settings

        self.width = settings.player_width
        self.height = settings.player_height

        
        # Vector for our jump velocity, which is just up
        self.v_jump = pygame.Vector2(-settings.player_jump_velocity, -settings.player_jump_velocity)

        # Player position
        self.pos = pygame.Vector2(settings.player_start_x, 
                                  settings.player_start_y if settings.player_start_y is not None else settings.height - self.height)
        
        # Player's velocity
        self.vel = pygame.Vector2(settings.player_v_x, settings.player_v_y)  # Velocity vector
        self.vel = settings.thrust

        self.LENGTH = 0.1

        gravity: float = 0.3
        self.gravity = pygame.Vector2(0, gravity)

        filename = images / 'spritesheet.png'  # Replace with your actual file path
        cellsize = (16, 16)  # Replace with the size of your sprites
        spritesheet = SpriteSheet(filename, cellsize)
        self.frog_sprites = scale_sprites(spritesheet.load_strip(0, 2, colorkey=-1) , 2)
        self.image = self.frog_sprites[0]
        self.rect = self.image.get_rect()
        self.myVar = 0


    # Direction functions. IMPORTANT! Using these functions isn't really
    # necessary, but it makes the code more readable. You could just use
    # self.vel.x < 0, but writing "self.going_left()" is a lot easier to read and
    # understand, it makes the code self-documenting. 

    def going_up(self):
        """Check if the player is going up"""
        return self.vel.y < 0
    
    def going_down(self):
        """Check if the player is going down"""
        return self.vel.y > 0
    
    def going_left(self):
        """Check if the player is going left"""
        return self.vel.x < 0
    
    def going_right(self):
        """Check if the player is going right"""
        return self.vel.x > 0
    
    
    # Location Fuctions
    
    def at_top(self):
        """Check if the player is at the top of the screen"""
        return self.pos.y <= 0
    
    def at_bottom(self):
        """Check if the player is at the bottom of the screen"""
        return self.pos.y >= self.game.settings.height - self.height

    def at_left(self):
        """Check if the player is at the left of the screen"""
        return self.pos.x <= 0
    
    def at_right(self):
        """Check if the player is at the right of the screen"""
        return self.pos.x >= self.game.settings.width - self.width
    
    # Updates
    
    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_v()
        self.update_pos()
        self.update_input()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.LENGTH+=0.05
            

        if keys[pygame.K_DOWN]:
            self.LENGTH-=0.03

        if keys[pygame.K_RIGHT]:
            self.v_jump = self.v_jump.rotate(1)

        if keys[pygame.K_LEFT]:
            self.v_jump = self.v_jump.rotate(-1)
        
        initial_position = self.pos
        end_position = self.pos + self.v_jump * self.LENGTH * 100
        
        
    def update_v(self):
        """Update the player's velocity based on gravity and bounce on edges"""
         
        self.vel += self.gravity  # Add gravity to the velocity

        if self.at_bottom() and self.going_down():
            self.vel.y = 0

        if self.at_top() and self.going_up():
            self.vel.y = -self.vel.y
            
        drag = -self.vel * 0.01
        self.vel= self.vel + drag

         # Bounce off the top. 

        # If the player hits one side of the screen or the other, bounce the
        # player. we are also checking if the player has a velocity going farther
        # off the screeen, because we don't want to bounce the player if it's
        # already going away from the edge
        
        if (self.at_left() and self.going_left() ) or ( self.at_right() and self.going_right()):
            self.vel.x = -self.vel.x
            
    def update_pos(self):
        """Update the player's position based on velocity"""
        self.pos += self.vel  # Update the player's position based on the current velocity

        # If the player is at the bottom, stop the player from falling and
        # stop the jump
        
        if self.at_bottom():
            self.pos.y = self.game.settings.height - self.height

        if self.at_top():
            self.pos.y = 0

        # Don't let the player go off the left side of the screen
        if self.at_left():
            self.pos.x = 0
  
        # Don't let the player go off the right side of the screen
        elif self.at_right():
            self.pos.x = self.game.settings.width - self.width

    def update_jump(self):
        """Handle the player's jumping logic"""
        
        # Notice that we've gotten rid of self.is_jumping, because we can just
        # check if the player is at the bottom. 
        
        """if self.at_bottom():
                self.vel += self.v_jump
                """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.vel += self.v_jump

        # Jumping means that the player is going up. The top of the  
        # screen is y=0, and the bottom is y=SCREEN_HEIGHT. So, to go up,
        # we need to have a negative y velocity
        
         
    def update_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.vel += self.v_jump * self.LENGTH
 
    
    def draw(self, screen):
        #pygame.draw.rect(screen, Colors.PLAYER_COLOR, (self.pos.x, self.pos.y, self.width, self.height))
        
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.LENGTH+=0.05
            

        if keys[pygame.K_DOWN]: 
            self.LENGTH-=0.03

        if keys[pygame.K_RIGHT]:
            self.v_jump = self.v_jump.rotate(1)

        if keys[pygame.K_LEFT]:
            self.v_jump = self.v_jump.rotate(-1)"""
        
        initial_position = self.pos
        end_position = self.pos + self.v_jump * self.LENGTH * 100
        pygame.draw.line(screen, (self.myVar%255, self.myVar%100, 200), initial_position, end_position, 2)
        self.myVar += 1
        


settings = GameSettings()
game = Game(settings)
game.run()
