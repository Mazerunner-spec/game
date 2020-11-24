# Import required modules
import random
import pygame

# Initialize pygame and start
pygame.init()

# Set game window width and height
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('HyperionDev Capstone 2 Game')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 120, 100))

score = 0

# Set player and enemy images
player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemyscull.png")
enemy2 = pygame.image.load("enemyscull.png")
enemy3 = pygame.image.load("enemyscull.png")
enemy4 = pygame.image.load("enemyscull.png")
enemy5 = pygame.image.load("enemyscull.png")
enemy6 = pygame.image.load("enemyscull.png")
prize = pygame.image.load("cherry (2).png")

# Get the heights and widths of the images
player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()
enemy5_height = enemy5.get_height()
enemy5_width = enemy5.get_width()
enemy6_height = enemy6.get_height()
enemy6_width = enemy6.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print(f"This is the height of the player image: {player_height}")
print(f"This is the width of the player image: {player_width}")

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = random.randint(0,(screen_width - player_width))
playerYPosition = random.randint(0,(screen_height - player_height))

# Make the enemies start at random places. Did have them set to random but that caused death many times at the start

enemy1XPosition = 1320
enemy1YPosition = 250

enemy2XPosition = 462
enemy2YPosition = 531

enemy3XPosition = 100
enemy3YPosition = 378

enemy4XPosition = 1390
enemy4YPosition = 422

enemy5XPosition = 19
enemy5YPosition = 19

enemy6XPosition = 366
enemy6YPosition = 1024


# Make the prize start in a random position

prizeXPosition = random.randint(0,(screen_width - prize_width))
prizeYPosition = random.randint(0,(screen_height - prize_height))

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

while True:
    screen.fill(0) # Clears the screen.
    screen.blit(background, (0, 0))
    # Draws players image to screen
    screen.blit(player, (playerXPosition, playerYPosition))
    # Draws enemies to screen
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(enemy5, (enemy5XPosition, enemy5YPosition))
    screen.blit(enemy6, (enemy6XPosition, enemy6YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # Updates the screen
    pygame.display.flip()

    # Loops through events in the game
    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            # Test if the key pressed is the one we want.    
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True    
            if event.key == pygame.K_RIGHT:
                keyRight = True
        # This event checks if the key is up(i.e. not pressed by the user)
        if event.type == pygame.KEYUP:
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False    
            if event.key == pygame.K_RIGHT:
                keyRight = False

    if keyUp == True:
        if playerYPosition > 0 :
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We then need to test if these boxes intersect. If they do then there is a collision.

    # Create bounding box for player sprite:
    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bound box for enemy sprites
    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy1_box.top = enemy1YPosition
    enemy1_box.left = enemy1XPosition

    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy2_box.top = enemy2YPosition
    enemy2_box.left = enemy2XPosition

    enemy3_box = pygame.Rect(enemy3.get_rect())
    enemy3_box.top = enemy3YPosition
    enemy3_box.left = enemy3XPosition

    enemy4_box = pygame.Rect(enemy4.get_rect())
    enemy4_box.top = enemy4YPosition
    enemy4_box.left = enemy4XPosition

    enemy5_box = pygame.Rect(enemy5.get_rect())
    enemy5_box.top = enemy5YPosition
    enemy5_box.left = enemy5XPosition

    enemy6_box = pygame.Rect(enemy6.get_rect())
    enemy6_box.top = enemy6YPosition
    enemy6_box.left = enemy6XPosition

    # Bound box for prize sprite
    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prizeYPosition
    prize_box.left = prizeXPosition

    # Test collision of the bounding boxes with all enemies. I'm sure there is a better way...
    if playerBox.colliderect(enemy1_box) or playerBox.colliderect(enemy2_box) or playerBox.colliderect(enemy3_box)  or playerBox.colliderect(enemy4_box) or playerBox.colliderect(enemy5_box) or playerBox.colliderect(enemy6_box):
        # Display lost message
        print("You died.")
        # Quit the game
        pygame.quit()
        exit(0)
    
    if playerBox.colliderect(prize_box):
        prizeXPosition = random.randint(0,(screen_width - prize_width))
        prizeYPosition = random.randint(0,(screen_height - prize_height))
        score += 1

    # If player catches trophy 5 times, they win
    if(score == 5):
        print("You won!")
        pygame.quit()
        exit(0)

    # Move enemies around. They teleport after going off of the screen
    enemy1XPosition -= 0.2
    enemy1YPosition += 0.2
    if(enemy1XPosition < 0) or (enemy1YPosition < 0):
        enemy1XPosition = random.randint(0,screen_width)
        enemy1YPosition = random.randint(0,screen_height)

    enemy2XPosition += 0.3
    enemy2YPosition += 0.25
    if(enemy2XPosition < 0) or (enemy2YPosition < 0):
        enemy2XPosition = random.randint(0,screen_width)
        enemy2YPosition = random.randint(0,screen_height)
    
    enemy3XPosition += 0.15
    enemy3YPosition -= 0.4
    if(enemy3XPosition < 0) or (enemy3YPosition < 0):
        enemy3XPosition = random.randint(0,screen_width)
        enemy3YPosition = random.randint(0,screen_height)

    enemy4XPosition -= 0.23
    enemy4YPosition -= 0.4
    if(enemy4XPosition < 0) or (enemy4YPosition < 0):
        enemy4XPosition = random.randint(0,screen_width)
        enemy4YPosition = random.randint(0,screen_height)

    enemy5XPosition -= 0.27
    enemy5YPosition += 0.15
    if(enemy5XPosition < 0) or (enemy5YPosition < 0):
        enemy5XPosition = random.randint(0,screen_width)
        enemy5YPosition = random.randint(0,screen_height)
    
    enemy6XPosition += 0.35
    enemy6YPosition -= 0.4
    if(enemy6XPosition < 0) or (enemy6YPosition < 0):
        enemy6XPosition = random.randint(0,screen_width)
        enemy6YPosition = random.randint(0,screen_height)
            
