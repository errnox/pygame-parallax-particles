import math
from random import randrange, choice

import pygame


MAX_STARS  = 250
STAR_SPEED = 2
DEPTH_LEVELS = 100
SLOW_DOWN = 0.1

deg = 0
direction = 0
stars = []

def init_stars(screen, stars):
  """
  Create the starfield"""
  for i in range(MAX_STARS):
    # A star is represented as a list with this format: [X,Y,speed]
    stars.append([randrange(0,screen.get_width() - 1),
            randrange(0,screen.get_height() - 1),
            choice(range(1,DEPTH_LEVELS))])
 
def move_and_draw_stars(screen, stars):
  """
  Move and draw the stars in the given screen"""
  global deg
  global direction
  for star in stars:
    deg += 1
    if math.sin(deg) % 2 == 0:
      direction = -1
    else:
      direction = 1
    if deg <= 360:
      star[0] += (star[2] * SLOW_DOWN * math.sin(star[2] * SLOW_DOWN)) * direction
      star[1] += star[2] * SLOW_DOWN * math.cos(star[2] * SLOW_DOWN)
    else:
      star[0] = screen.get_width() / 2
      star[1] = screen.get_height() / 2
      deg = 0

    # If the star has hit the bottom border then we reposition
    # it to the top of the screen with a random X coordinate.
    if star[1] >= screen.get_height():
      star[1] = 0
      star[0] = randrange(0, 639)
      star[2] = choice(range(1, DEPTH_LEVELS))
 
    # Adjust the star color acording to the speed.
    # The slower the star, the darker should be its color.
    # if star[2] == 1:
    #   color = (100,100,100)
    # elif star[2] == 2:
    #   color = (190,190,190)
    # elif star[2] == 3:
    #   color = (255,255,255)

    greyscale = 255
    color = (greyscale, greyscale, greyscale)
 
    # Draw the star as a rectangle.
    # The star size is proportional to its speed.
    screen.fill(color, (star[0], star[1], star[2] * SLOW_DOWN,
                        star[2] * SLOW_DOWN))
 
def main():
  # Pygame cruft
  pygame.init()
  screen = pygame.display.set_mode((640,480))
  pygame.display.set_caption("Parallax Starfield Simulation")
  clock = pygame.time.Clock()
 
  init_stars(screen, stars)
 
  while True:
    # Lock the framerate at 50 FPS
    clock.tick(50)
 
    # Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
 
    screen.fill((0,0,0))
    move_and_draw_stars(screen, stars)
    pygame.display.flip()
 
if __name__ == "__main__":
  main()

