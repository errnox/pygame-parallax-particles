import math
from random import randrange, choice

import pygame


star = [0, 0, 0]
rot = 0
radius = 50
direction = 0

def init_star(screen, star):
  star = [screen.get_width() / 2,
          screen.get_height() / 2,
          10]

def center_star(screen, star):
  star[0] = screen.get_width() / 2
  star[1] = screen.get_height() / 2

 
def move_and_draw_star(screen, star, x, y):
  global rot
  global direction
  global radius

  if rot < 360:
    rot += 1
  else:
    rot = 0

  star[0] = x + radius * math.sin(rot * 2400)
  star[1] = y + radius * math.cos(rot * 2400)

  # Reset the position of the star
  if star[1] >= screen.get_height():
    star[1] = 0
    star[0] = randrange(0, 639)
    star[2] = 10

  color = (255, 255, 255)
  screen.fill(color, (star[0], star[1], star[2] + 10,
                      star[2] + 10))
 
def main():
  # Pygame stuff
  pygame.init()
  screen = pygame.display.set_mode((640,480))
  pygame.display.set_caption("Parallax Starfield Simulation")
  clock = pygame.time.Clock()
 
  center_star(screen, star)

  init_star(screen, star)
 
  while True:
    # Lock the framerate at 50 FPS
    clock.tick(50)
 
    # Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
 
    screen.fill((0,0,0))
    move_and_draw_star(screen, star, screen.get_width() / 2,
                       screen.get_height() / 2)
    pygame.display.flip()
 
if __name__ == "__main__":
  main()

