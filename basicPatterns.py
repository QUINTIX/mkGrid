import pygame
from math import log2
from math import ceil

def pixelChecker(surface, xy):
	#starter: four pixels
	surface.set_at((0,0), pygame.Color(0,0,0,255))
	surface.set_at((1,1), pygame.Color(0,0,0,255))
	surface.set_at((0,1), pygame.Color(255,255,255,255))
	surface.set_at((1,0), pygame.Color(255,255,255,255))

	#steps = int( ceil( log2( min(xy) ) ) )
	corner = 2
	rect = pygame.Rect(0,0, corner, corner)
	#for i in range(steps):
	#spread
	while corner < max(xy):
		#make 3 copies
		surface.blit(surface, (corner, 0), rect) 	#right
		surface.blit(surface, (0, corner), rect)	#down
		surface.blit(surface, (corner, corner), rect)	#right down

		corner *= 2 #double area each time
		rect.w = min((corner, xy[0])) #minimize overdraw 
		rect.h = min((corner, xy[1])) #minimize overdraw


def sierpinski(surface, xy):
	#starter: four pixels
	surface.set_at((0,0), pygame.Color(0,0,0,255))
	surface.set_at((1,1), pygame.Color(0,0,0,255))
	surface.set_at((0,1), pygame.Color(255,255,255,255))
	surface.set_at((1,0), pygame.Color(255,255,255,255))

	corner = 2
	rect = pygame.Rect(0,0, corner, corner)

	#spread
	while corner < max(xy):
		#make 2 copies
		surface.blit(surface, (corner, 0), rect) 	#right
		surface.blit(surface, (0, corner), rect)	#down
#		surface.blit(surface, (corner, corner), rect)	#right down

		corner *= 2 #double area each time
		rect.w = min((corner,xy[0])) 
		rect.h = min((corner,xy[1]))
