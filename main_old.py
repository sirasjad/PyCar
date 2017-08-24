# PyCar | Developed by Sirajuddin Asjad and Kirisan Manivannan

# INCLUDES
from modules import *
from static import *

# MAIN
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(title)

loading = pygame.image.load("loading.png")
loading = loading.convert_alpha()
loadingRect = loading.get_rect()
screen.blit(loading, loadingRect)
pygame.display.flip()
time.sleep(3)

theClock = pygame.time.Clock()
running = True

while running:
	road = pygame.image.load("road.png")
	road = road.convert_alpha()
	roadRect = road.get_rect()
	screen.blit(road, roadRect)
	
	w,h = roadRect
	x = 0
	y = 0

	x1 = 0
	y1 = -h
	
	y1 = y1 + 5
	y = y + 5
	
	screen.blit(road,(x,y))
	screen.blit(road,(x1,y1))
	
	if y > h:
		y = -h
	if y1 > h:
		y1 = -h

	pygame.display.flip()
	pygame.display.update()
	theClock.tick(10)

car = pygame.image.load("car.png")
car = car.convert_alpha()
carRect = car.get_rect()
carRect.x = 500
carRect.y = 300
screen.blit(car, carRect)
pygame.display.flip()



input()