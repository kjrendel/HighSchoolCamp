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

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # ToDo:Work goes here!

    Teal = (151, 220, 196)
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Blue = (0, 0, 255)
    Red =  (255, 0, 0)
    FLESH = (242, 195, 158)
    PI = 3.1415926538979323846

    screen.fill(White)


    # # Draw a circle
    pygame.draw.circle(screen, FLESH, [200, 200], 100)
    pygame.draw.arc(screen, Black, [140, 165, 125, 100], PI, 0, 5)
    pygame.draw.ellipse(screen, Blue, [150, 155, 30, 45])
    pygame.draw.ellipse(screen, Blue, [220, 155, 30, 45])
    #body attempt
    pygame.draw.line(screen,Blue, [200, 300], [200, 600], 8)
    # arm
    pygame.draw.line(screen, Blue, [200, 350], [300, 450], 8)
    # arm2
    pygame.draw.line(screen, Blue, [200, 350], [100, 450], 8)
    #leg1
    pygame.draw.line(screen, Black, [200, 600], [100, 675], 8)
    #leg2
    pygame.draw.line(screen, Black, [200, 600], [300, 675], 8)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()