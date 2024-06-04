import pygame, sys
from pygame.locals import QUIT
import bunny

WHITE = (255, 255, 255)
FPS = 30
WIDTH = 600
HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bunny Run')

player = bunny.Bunny(x=80, y=200, scale_x=.2, scale_y=.2)

clock = pygame.time.Clock()
while True:
	screen.fill(WHITE)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	player.update()
	player.blit(screen)
	
	pygame.display.update()
	clock.tick(FPS)


