"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path



# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

# Screen dimensions.         
class Game_Settings():
    WIDTH, HEIGHT = 600, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders Ripoff")

    # Colors
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # FPS
    FPS = 60

    # Player attributes
    PLAYER_SIZE = 75

    player_speed = 5

    # Obstacle attributes
    OBSTACLE_WIDTH = 10
    OBSTACLE_HEIGHT = 22
    OBSTACLESIZE = 48
    obstacle_speed = 5

    Player_x_velocity = 2
    Player_y_velocity = 2
    Player_gravity = 0.75
    """is_jumping = False"""
    JAYDEN_COLOR = (175, 243, 100)
    JAYDEN_COLOR2 = (213, 10, 21)
    LINE_COLOR = (56, 250, 150)
    n = 0
    PROJECTILE_SIZE = 10


# Font
    font = pygame.font.SysFont(None, 36)

 
# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.image = pygame.Surface((Game_Settings.OBSTACLE_WIDTH, Game_Settings.OBSTACLE_HEIGHT))
        self.image.fill(Game_Settings.BLACK)
        self.image = pygame.transform.rotate(self.image, 100)
        self.rect = self.image.get_rect()
        self.rect.x = Game_Settings.WIDTH
        self.rect.y = Game_Settings.HEIGHT - Game_Settings.OBSTACLE_HEIGHT - 23
        self.explosion = pygame.image.load(images_dir / "explosion1.gif")
        self.angle = random.randint(0, 2)
            
        self.image = pygame.image.load(images_dir / "asteroid1.png")
        self.image = pygame.transform.scale(self.image, (Game_Settings.OBSTACLESIZE, Game_Settings.OBSTACLESIZE))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect.y = Game_Settings.HEIGHT - Game_Settings.OBSTACLE_HEIGHT - random.randint(25,450)
        self.velocity = pygame.Vector2(random.randint(-10, 1), random.randint(-5, 5))
        self.acceleration = pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5))

    def update(self):
        """self.rect.x -= Game_Settings.obstacle_speed"""
        self.velocity = pygame.Vector2()

        #self.image = pygame.transform.rotate(self.image, self.angle)

        
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

        self.acceleration[0], self.acceleration[1] = pygame.Vector2(random.randint(-5, -1), random.randint(-5, 5))

        self.velocity += self.acceleration 

        self.rect[0] += self.velocity[0]
        self.rect[1] += self.velocity[1]

            
  
    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image2 = self.explosion
        self.image = pygame.transform.scale(self.image, (Game_Settings.OBSTACLE_WIDTH, Game_Settings.OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image2 = pygame.transform.scale(self.image, (Game_Settings.OBSTACLE_WIDTH, Game_Settings.OBSTACLE_HEIGHT))
        self.rect2 = self.image.get_rect(center=self.rect.center)


# Define a player class

    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(images_dir/'alien1.gif')
        self.image = pygame.transform.scale(self.image, (Game_Settings.PLAYER_SIZE+10, Game_Settings.PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300
        self.position = (self.rect.x, self.rect.y)
        self.speed = Game_Settings.player_speed
        """self.is_jumping = False"""

        # For Sprites, the image and rect attributes are part of the Sprite class
        # and are important. The image is the surface that will be drawn on the screen

       
    def update(self):

        self.speed += 0.20

        self.rect.y += self.speed

        
        keys = pygame.key.get_pressed()
        


        if keys[pygame.K_UP]:
                self.speed = -5
                self.is_jumping = True

        if keys[pygame.K_DOWN]:
            self.rect.bottom += 2.5

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if keys[pygame.K_LEFT]:
            self.rect.x-=5

           
        # Keep the player on screen
        """if self.rect.top < 0:
            self.rect.top = 0"""
        if self.rect.bottom > Game_Settings.HEIGHT:
            self.rect.bottom = Game_Settings.HEIGHT
            self.is_jumping = False

        if self.rect.right > Game_Settings.WIDTH:
            self.rect.left = 1

        if self.rect.left < 0:
            self.rect.right = Game_Settings.WIDTH - 2

        if self.rect.bottom > Game_Settings.HEIGHT:
            self.rect.top = 2

        if self.rect.top < 0:
            self.rect.bottom = Game_Settings.HEIGHT - 2
        

        self.position = (self.rect.x, self.rect.y)
    
            
        # Jumping means that the player is going up. The top of the 
        # screen is y=0, and the bottom is y=settings.screen_height. So, to go up,
        # we need to have a negative y velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Projectile(pygame.sprite.Sprite):
    def  __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Game_Settings.PROJECTILE_SIZE, Game_Settings.PROJECTILE_SIZE])
        self.image.fill(Game_Settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = position[0], position[1]
        
        
    """
    def draw(self, surface):
        pygame.draw.circle(surface, Game_Settings.BLUE, self.rect[0], self.rect[1])
    """ 
    def update(self):

        self.rect[0] += 10

        if self.rect[0] > Game_Settings.WIDTH:
            self.kill

"""class Health_Bar():
    
    def draw():
        pygame.draw.rect"""



        


        # For Sprites, the image and rect attributes are part of the Sprite class
        # and are important. The image is the surface that will be drawn on the screen

# Create a player object
player = Player()
player_group = pygame.sprite.GroupSingle(player)


# Add obstacles periodically
def add_obstacle(obstacles, Game_Settings):
   
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
    if random.random() < 0.4:
        n = random.randint(0,1)
        obstacle = Obstacle(n)
        obstacles.add(obstacle)
        n+=1
        
        

        return 1
    return 0


# Main game loop
class game_loop():
    while True:
        clock = pygame.time.Clock()
        game_over = False
        last_obstacle_time = pygame.time.get_ticks()

        # Group for obstacles
        obstacles = pygame.sprite.Group()

        projectiles = pygame.sprite.Group()

        player = Player()

        obstacle_count = 0

        x = 0
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Update player
            player.update()
          
            # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 100:
                last_obstacle_time = pygame.time.get_ticks()
                obstacle_count += add_obstacle(obstacles, Game_Settings)

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_SPACE]:
                projectiles.add(Projectile(player.position))
                    
                
            
            obstacles.update()
            projectiles.update()

            # Check for collisions
            collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
            
            if collider:
                collider[0].explode()
                print(f"Good try! Final score = {obstacle_count}")
                game_over=True

            

            
                
                

            # Draw everything
            Game_Settings.screen.fill(Game_Settings.BLACK)
            initial_position = (0, Game_Settings.HEIGHT-5)
            end_position = (Game_Settings.WIDTH, Game_Settings.HEIGHT-5)
            pygame.draw.line(Game_Settings.screen ,Game_Settings.BLACK, initial_position, end_position, 2)
            player.draw(Game_Settings.screen)
            obstacles.draw(Game_Settings.screen)
            projectiles.draw(Game_Settings.screen)
            
            
            
            n = 1
            n1 = 1000
            # Display obstacle count
            obstacle_text = Game_Settings.font.render(f"Obstacles detected: {obstacle_count}", True, Game_Settings.WHITE)
            Game_Settings.screen.blit(obstacle_text, (10, 10))
            """if obstacle_count > n1 ():
                obstacle_text = Game_Settings.font.render(f"level: {n}", True, Game_Settings.WHITE)
                Game_Settings.screen.blit(obstacle_text, (10, 60))
                n1+=1000"""

            collider2 = pygame.sprite.groupcollide(projectiles, obstacles, True, True, collided = None)
            x += len(collider2)
            obstacle_text2 = Game_Settings.font.render(f"Obstacles killed: {x}", True, Game_Settings.WHITE)
            Game_Settings.screen.blit(obstacle_text2, (10, 35))

            

            

            pygame.display.update()
            clock.tick(Game_Settings.FPS)
    
        #Game over screen
        while game_over == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            Game_Settings.screen.fill(Game_Settings.JAYDEN_COLOR2)
            obstacle_text = Game_Settings.font.render(f"            Nice try, you avoided {obstacle_count} obstacle(s).", True, Game_Settings.WHITE)
            obstacle_text2 = Game_Settings.font.render("            Press 'c' to continue!", True, Game_Settings.WHITE)
            Game_Settings.screen.blit(obstacle_text, (10, 180))
            Game_Settings.screen.blit(obstacle_text2, (10, 215))
            obstacle_text3 = Game_Settings.font.render("            Jayden says to do better next time! >:)", True, Game_Settings.WHITE)
            Game_Settings.screen.blit(obstacle_text3, (10, 275))
            pygame.display.update()
            clock.tick(Game_Settings.FPS)
        
            if game_over == True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_c]:
                    game_over = False

                





if __name__ == "__main__":
    game_loop()
