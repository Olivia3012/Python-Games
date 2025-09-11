import pygame
from dataclasses import dataclass
from jtlgames.vector20 import Vector20Factory
import pygame
from jtlgames.spritesheet import SpriteSheet
from pathlib import Path
import random
images = Path(__file__).parent / 'images'
images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"




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
    gravity: float = 0.5
    player_start_x: int = 300
    player_start_y: int = 0
    player_v_y: float = 0  # Initial y velocity
    player_v_x: float = 0  # Initial x velocity
    player_width: int = 30
    player_height: int = 30
    player_jump_velocity: float = 0.5
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

        self.screen = pygame.display.set_mode((GameSettings.width, GameSettings.height))
        self.clock = pygame.time.Clock()

        # Turn Gravity into a vector
        self.gravity = pygame.Vector2(0, self.settings.gravity)
        """self.flappy = ["flappybird.png", "flappydown.png"]
        self.x = 0"""

    def vec_to_center(self, pos):
        print("I am at", Player.posx, Player)

    def run(self):
        """Main game loop"""
        player = Player( self, 300, 30, "fat_frog.png", 40, 20)
        Don = Player(self, 40, 30, "Party_frog.png", 20, 50)
        Ron = Player(self, 100, 30, "flappydown.png", 30, 25)
        if GameSettings.frame_rate%100:
            self.x += 1
            if self.x > 1:
                self.x = 0
        player_group = pygame.sprite.Group()
        player_group.add(player)
        player_group.add(Don)
        player_group.add(Ron)
        self.myVar = 0
        platform = Platform(game)
        platform_group = pygame.sprite.Group()
        #platform2 = Platform(self)
        #platform_group.add(platform2)
        


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            
            self.screen.fill(Colors.BACKGROUND_COLOR)
            player.update(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
            Don.update(pygame.K_a, pygame.K_d, pygame.K_w)
            Ron.update(pygame.K_v, pygame.K_n, pygame.K_SPACE)
            player_group.draw(self.screen)
            player.draw(self.screen, 200)
            Don.draw(self.screen, 10)
            Ron.draw(self.screen, 100)
            self.myVar += 1
            platform.update(300, 300)
            platform.update(200, 200)
            platform.update(150, 400)
            platform.update(400, 400)
            platform.update(12, 250)
            platform.update(300, 100)
            
            
            
            pygame.display.flip()
            self.clock.tick(self.settings.frame_rate)

        pygame.quit() 

class Platform(pygame.sprite.Sprite):
    def __init__(self, game: Game):
        Game.myVar = 0
        self.game = game
        game = Game(GameSettings)
        pos_list = [(300, 300), (200, 200), (150, 400), (400, 400), (12, 250), (300, 100)]
    def update(self, x, y):
        pygame.draw.rect(game.screen, (game.myVar%255, game.myVar%100, 200), (x, y, 100, 10)) 

class Player(pygame.sprite.Sprite):
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game, x, y, image, image_size_x, image_size_y):
        super().__init__()
        global pos_list
        self.game = game
        settings = self.game.settings

        self.width = settings.player_width
        self.height = settings.player_height

        
        # Vector for our jump velocity, which is just up
        self.v_jump = pygame.Vector2(-settings.player_jump_velocity, -settings.player_jump_velocity)

        # Player position
        """self.pos = pygame.Vector2(settings.player_start_x, 
                                  settings.player_start_y if settings.player_start_y is not None else settings.height - self.height)
        """
        self.pos = pygame.Vector2(x, y)
        
        # Player's velocity
        self.vel = pygame.Vector2(settings.player_v_x, settings.player_v_y)  # Velocity vector
        self.vel = settings.thrust

        self.LENGTH = 0.5

        gravity: float = 0.4
        self.gravity = pygame.Vector2(0, gravity)

        """filename = images / 'spritesheet.png'  # Replace with your actual file path
        cellsize = (16, 16)  # Replace with the size of your sprites
        spritesheet = SpriteSheet(filename, cellsize)
        self.frog_sprites = scale_sprites(spritesheet.load_strip(0, 5, colorkey=-1) , 2)
        self.image = self.frog_sprites[4]
        self.frog = scale_sprites(spritesheet.load_strip(0, 5, colorkey=-1) , 2)
        self.rect = self.image.get_rect()"""
        self.image = pygame.image.load(images_dir / image)
        self.image = pygame.transform.scale(self.image, (image_size_x, image_size_y))
        self.rect = self.image.get_rect()
        #fat frog sprite code
        self.myVar = 0
        self.rect[0], self.rect[1] = pygame.Vector2(x, y)
        self.rect[2] = image_size_x
        self.rect[3] = image_size_y
        self.on_platform = False


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
        return self.rect.top <= 0
    
    def at_bottom(self):
        """Check if the player is at the bottom of the screen"""
        return self.rect.bottom >= self.game.settings.height
        """return self.rect[1] == 600 - self.rect[3] or 599 - self.rect[3] """
        

    def at_left(self):
        """Check if the player is at the left of the screen"""
        return self.rect.left <= 0
    
    def at_right(self):
        """Check if the player is at the right of the screen"""
        return self.rect.right >= self.game.settings.width    
    # Updates
    
    def update(self, left, right, up):
        """Update player position, continuously jumping"""
        #print("update called")
        
        self.update_jump(up)
        self.update_v()
        self.update_pos()
        self.update_input(up)
        keys = pygame.key.get_pressed()
        """if keys[pygame.K_UP]:
            self.LENGTH+=0.05"""
            
        if keys[right]:
            self.v_jump = self.v_jump.rotate(1)

        if keys[left]:
            self.v_jump = self.v_jump.rotate(-1)
        
        initial_position = self.pos
        end_position = self.pos + self.v_jump * self.LENGTH * 100


        #   x                    x + width  y-3                 y + 3
        if  150 < self.rect[0] < 250 and 397 < self.rect[1] < 403:
            self.rect[1] = 400 - self.rect[3]
            #              y
            self.vel = pygame.Vector2(0, 0)
        #deleted going down "self.going_down and" 

        # TODO: make each Platform object store its location and dimensions somehow. with a rect?
        # for p in platforms:  # platforms is a list of the 6 Platform objects
          #   if  p.x < self.rect[0] < p.x + p.w and p.y-3 < self.rect[1] < p.y + 3:
          #  self.rect[1] = p.y - self.rect[3]
          #  self.vel = pygame.Vector2(0, 0)

             
            self.on_platform = True
            
        if self.rect[0] < 150 < 250 < self.rect[0]:
            self.on_platform = False

        """platform = Platform
        if self.going_down and pos_list[0][0] < self.rect[0] < pos_list[0][0] + 100 and pos_list[0][1]- 2 < self.rect[1] <  pos_list[0][1] + 2:
            self.rect[1] = platform.pos_list[0][1] - self.rect.width
            self.vel = pygame.Vector2(0, 0)
             
            self.on_platform = True
            
        if self.rect[0] < pos_list[0][0] < pos_list[0][0] + 100 < self.rect[0]:
            self.on_platform = False"""
        
        
    def update_v(self):
        """Update the player's velocity based on gravity and bounce on edges"""
        if self.on_platform == False:
            self.vel += self.gravity  # Add gravity to the velocity

            
                
            drag = -self.vel * 0.01
            self.vel= self.vel + drag

        if self.at_bottom() and self.going_down():
            self.vel.y = 0
            print(self.rect[1])

        if self.at_top() and self.going_up():
            self.vel.y = -self.vel.y

         # Bounce off the top. 

        # If the player hits one side of the screen or the other, bounce the
        # player. we are also checking if the player has a velocity going farther
        # off the screeen, because we don't want to bounce the player if it's
        # already going away from the edge
        
        if (self.at_left() and self.going_left() ) or ( self.at_right() and self.going_right()):
            self.vel.x = -self.vel.x
            
    def update_pos(self):
        """Update the player's position based on velocity"""
        self.rect[0] += self.vel[0]
        self.rect[1] += self.vel[1]  # Update the player's position based on the current velocity

        # If the player is at the bottom, stop the player from falling and
        # stop the jump
        
        if self.at_bottom():
            self.rect[1] = self.game.settings.height - self.rect[3]
            self.jumping = False
            self.vel[0] = 0
        if self.at_top():
            self.rect[1] = 0
            

        # Don't let the player go off the left side of the screen
        if self.at_left():
            self.rect[0] = 0 + self.rect[2]
  
        # Don't let the player go off the right side of the screen
        elif self.at_right():
            self.rect[0] = self.game.settings.width - self.rect[2]

    def update_jump(self, up):
        """Handle the player's jumping logic"""
        
        # Notice that we've gotten rid of self.is_jumping, because we can just
        # check if the player is at the bottom. 
        
        """if self.at_bottom():
                self.vel += self.v_jump
                """
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.vel += self.v_jump 
            

        # Jumping means that the player is going up. The top of the  
        # screen is y=0, and the bottom is y=SCREEN_HEIGHT. So, to go up,
        # we need to have a negative y velocity
        
         
    def update_input(self, up):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.vel += self.v_jump * self.LENGTH 
 
    
    def draw(self, screen, color):
        #pygame.draw.rect(screen, Colors.PLAYER_COLOR, (self.pos.x, self.pos.y, self.width, self.height))
        
        
        end_position = pygame.Vector2(self.rect[0],self.rect[1]) + self.v_jump * self.LENGTH * 50
        pygame.draw.line(screen, (self.myVar%255, self.myVar%100, color), pygame.Vector2(self.rect[0],self.rect[1]), end_position, 1)
        self.myVar += 1


        
    
        



settings = GameSettings()
game = Game(settings)
game.run()
