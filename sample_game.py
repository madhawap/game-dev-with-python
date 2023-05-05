import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the game window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("My Game")

# Set up the game loop
clock = pygame.time.Clock()
game_running = True

# Set up the player sprite
player_width = 50
player_height = 50
player_x = (win_width - player_width) // 2
player_y = win_height - player_height
player_speed = 50
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# ToDo: Add the following as a collection
# Set up the animation variables
x = 50
y = 50
width = 50
height = 50
vel = 5

# Set up the animation variables
x1 = 50
y1 = 150
width1 = 50
height1 = 50
vel1 = 4

# Set up the animation variables
x2 = 50
y2 = 350
width2 = 50
height2 = 50
vel2 = 8

# Load sound effect
# collision_sound = pygame.mixer.Sound('collision_sound.wav')
collision_with_other_box_sound = pygame.mixer.Sound(os.path.join("assets", "hit.wav"))
collision_with_wall_sound = pygame.mixer.Sound(os.path.join("assets", "wall.wav"))

# Main game loop
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.move_ip(-player_speed, 0)
            elif event.key == pygame.K_RIGHT:
                player_rect.move_ip(player_speed, 0)
            elif event.key == pygame.K_UP:
                player_rect.move_ip(0, -player_speed)
            elif event.key == pygame.K_DOWN:
                player_rect.move_ip(0, player_speed)

    # Update the animation variables
    x += vel
    if x > win_width - width or x < 0:
        vel = -vel

    # Update the animation variables
    x1 += vel1
    if x1 > win_width - width1 or x1 < 0:
        vel1 = -vel1

    # Update the animation variables
    x2 += vel2
    if x2 > win_width - width2 or x2 < 0:
        vel2 = -vel2

    # Check for collision with blue box
    if player_rect.colliderect(pygame.Rect(x, y, width, height)):
        # Play collision sound effect
        collision_with_other_box_sound.play()
        # Reset player position
        player_rect.x = (win_width - player_width) // 2
        player_rect.y = win_height - player_height

    # Check for collision with blue box
    if player_rect.colliderect(pygame.Rect(x1, y1, width1, height1)):
        # Play collision sound effect
        collision_with_other_box_sound.play()
        # Reset player position
        player_rect.x = (win_width - player_width) // 2
        player_rect.y = win_height - player_height

    # Check for collision with blue box
    if player_rect.colliderect(pygame.Rect(x2, y2, width2, height2)):
        # Play collision sound effect
        collision_with_other_box_sound.play()
        # Reset player position
        player_rect.x = (win_width - player_width) // 2
        player_rect.y = win_height - player_height

    # Stop player from going beyond game frame
    player_rect.left = max(player_rect.left, 0)
    player_rect.right = min(player_rect.right, win_width)
    player_rect.top = max(player_rect.top, 0)
    player_rect.bottom = min(player_rect.bottom, win_height)

    # Check if player has won
    if player_rect.top <= 0:
        # Show win display
        font = pygame.font.SysFont(None, 48)
        win_text = font.render("You Win!", True, (0, 255, 0))
        win_rect = win_text.get_rect(center=(win_width // 2, win_height // 2))
        win.fill((255, 255, 255))
        win.blit(win_text, win_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        # Reset player position
        player_rect.x = (win_width - player_width) // 2
        player_rect.y = win_height - player_height

    # Draw the game
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), player_rect)
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.draw.rect(win, (0, 0, 255), (x1, y1, width1, height1))
    pygame.draw.rect(win, (0, 0, 255), (x2, y2, width2, height2))
    pygame.display.update()

    wall_collision = False
    if player_rect.left <= 0:
        wall_collision = True
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            collision_with_wall_sound.play()
    elif player_rect.right >= win_width:
        wall_collision = True
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            collision_with_wall_sound.play()
    elif player_rect.top <= 0:
        wall_collision = True
        if pygame.key.get_pressed()[pygame.K_UP]:
            collision_with_wall_sound.play()
    elif player_rect.bottom >= win_height:
        wall_collision = True
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            collision_with_wall_sound.play()

    if wall_collision:
        # Stop player from going beyond game frame
        player_rect.left = max(player_rect.left, 0)
        player_rect.right = min(player_rect.right, win_width)
        player_rect.top = max(player_rect.top, 0)
        player_rect.bottom = min(player_rect.bottom, win_height)
    else:
        # Allow player to move freely within game frame
        player_rect.clamp_ip(pygame.Rect(0, 0, win_width, win_height))

    # Wait for the next frame
    clock.tick(60)

# Clean up and quit
pygame.quit()
