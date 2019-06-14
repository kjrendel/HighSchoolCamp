"""
title: pygame_practice
author: Kaly
date: 2019-06-14 09:48
"""
# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (600, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")


Teal = (151, 220, 196)
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
FLESH = (242, 195, 158)
PI = 3.14159265358979323846

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 3

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, Red, [60 + x, 410 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, FLESH, [200 + x, 200 + y], 100)
    pygame.draw.arc(screen, Black, [140 + x, 165 + y, 125, 100], PI, 0, 5)
    pygame.draw.ellipse(screen, Blue, [150 + x, 155 + y, 30, 45])
    pygame.draw.ellipse(screen, Blue, [220 + x, 155 + y, 30, 45])
    # body attempt
    pygame.draw.line(screen, Blue, [200 + x, 300 + y], [200 + x, 600 + y], 8)
    # arm
    pygame.draw.line(screen, Blue, [200 + x, 350 + y], [300+ x, 450+ y], 8)
    # arm2
    pygame.draw.line(screen, Blue, [200 + x, 350 + y], [100+ x, 450+ y], 8)
    # leg1
    pygame.draw.line(screen, Black, [200 + x, 600 + y], [100+ x, 675+ y], 8)
    # leg2
    pygame.draw.line(screen, Black, [200 + x, 600 + y], [300+ x, 675+ y], 8)

# Loop as long as done == False


while not done:
    ball_pos += ball_change
    if ball_pos > 200:
        ball_change -= 3
    if ball_pos < 0:
        ball_change += 3



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(White)

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(60)

# Be IDLE friendly
pygame.quit()