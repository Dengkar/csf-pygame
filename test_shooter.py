import pygame
import sys
import random
from math import *
from pygame import mixer
import unittest
import pygame

from shooter import Balloon
pygame.init()

# Set the game window dimensions
width = 500
height = 500

# Create the game display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Shooter")

# Set the game clock
clock = pygame.time.Clock()

# Load the background music
mixer.music.load('gamemusic-6082 (1).mp3')
mixer.music.play()  # Play the background music

# Define the margin and lower bound for balloon placement
margin = 100
lowerBound = 100

# Initialize the score
score = 0

# Game loop
# while True:
#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:  # Handle quit event
#             pygame.quit()
#             sys.exit()

#     # Update the score display
#     score_font = pygame.font.SysFont('Arial', 24)
#     score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
#     display.blit(score_text, (10, 10))

#     # Draw the game elements
#     # ... (Draw balloons, player, etc.)

#     # Update the display
#     pygame.display.flip()

#     # Limit the game speed to 60 frames per second
#     clock.tick(60)


class TestBalloon(unittest.TestCase):

    def setUp(self):
        self.balloon = Balloon(10)

    def test_init(self):
        import pygame
import sys
import random
from math import *
from pygame import mixer
import unittest
import pygame

from shooter import Balloon
pygame.init()

# Set the game window dimensions
width = 500
height = 500

# Create the game display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Shooter")

# Set the game clock
clock = pygame.time.Clock()

# Load the background music
mixer.music.load('gamemusic-6082 (1).mp3')
mixer.music.play()  # Play the background music

# Define the margin and lower bound for balloon placement
margin = 100
lowerBound = 100

# Initialize the score
score = 0

# Game loop
# while True:
#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:  # Handle quit event
#             pygame.quit()
#             sys.exit()

#     # Update the score display
#     score_font = pygame.font.SysFont('Arial', 24)
#     score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
#     display.blit(score_text, (10, 10))

#     # Draw the game elements
#     # ... (Draw balloons, player, etc.)

#     # Update the display
#     pygame.display.flip()

#     # Limit the game speed to 60 frames per second
#     clock.tick(60)


class TestBalloon(unittest.TestCase):

    def setUp(self):
        self.balloon = Balloon(10)
        

    def test_init(self):
     balloon = Balloon(10)
     balloon.a = random.randint(31, 31)
     self.assertLessEqual(balloon.b - balloon.a, 20)
     self.assertGreaterEqual(balloon.x, margin)
     self.assertLessEqual(balloon.x, width - balloon.a - margin)
     self.assertEqual(balloon.y, height - lowerBound)
     self.assertEqual(balloon.angle, 90)
     self.assertEqual(balloon.speed, -10)
     for value in [-1, 0, 1]:
        self.assertIn(value, balloon.probPool)
     self.assertGreaterEqual(balloon.length, 50)
     self.assertLessEqual(balloon.length, 100)

    # Validate that the color is within the expected set
     # Randomly assign a valid color
    valid_colors = ['red', 'green', 'purple', 'orange', 'yellow', 'blue']
    color_index = random.randint(0, len(valid_colors) - 1)
    color = valid_colors[color_index]



if __name__ == '__main__':
    unittest.main()

