# PyCar | Developed by Sirajuddin Asjad and Kirisan Manivannan

# INCLUDES
import pygame
from time import sleep, time
from random import randrange
from pygame.locals import *
from variables import *

# MAIN
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(title)
FPS = pygame.time.Clock()

def printTimer(seconds):
	font = pygame.font.Font('freesansbold.ttf', 20)
	text = font.render("Time:  %i seconds" % int(seconds), True, black)
	screen.blit(text, (20, 20))

def countScore(count):
	font = pygame.font.Font('freesansbold.ttf', 20)
	text = font.render("Score: %i points" % int(count), True, black)
	screen.blit(text, (20, 45))

def traffic(x, y):
	blueCar = pygame.image.load('inc/car2.png')
	screen.blit(blueCar, (x, y))

def car(x, y):
	carImg = pygame.image.load('inc/car.png')
	screen.blit(carImg, (x, y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	textSurface, textRectangle = text_objects(text, largeText)
	textRectangle.center = ((screenWidth/2), (screenHeight/2))
	screen.blit(textSurface, textRectangle)
	pygame.display.flip()
	sleep(2)
	main()

def crashCar():
	message_display('GAME  OVER')

def background():
	backImg = pygame.image.load('inc/road.png')
	backRectangle = backImg.get_rect()
	screen.blit(backImg, backRectangle)

def loader():
	loadTime = time()
	loading = True
	while loading:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		loadImg = pygame.image.load('inc/loading.png')
		loadRectangle = loadImg.get_rect()
		screen.blit(loadImg, loadRectangle)
		pygame.display.flip()
		
		if time() > (loadTime + 5):
			screen.fill(white)
			pygame.display.flip()
			loading = False

def main():
	carPosX = 610
	carPosY = 475
	carPosXChange = 0
	
	trafficPosX = randrange(220, 980)
	trafficPosY = -600
	trafficSpeed = 3

	startTime = time()
	score = 0

	exit = False
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					carPosXChange = -5
				elif event.key == pygame.K_RIGHT:
					carPosXChange = 5
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					carPosXChange = 0
		
		background()
		checkTime = time()
		
		if checkTime > (startTime + 5):
			# trafficSpeed = 6
			trafficSpeed = 60
		if checkTime > (startTime + 10):
			# trafficSpeed = 10
			trafficSpeed = 100
		if checkTime > (startTime + 15):
			# trafficSpeed = 15
			trafficSpeed = 150
		
		carPosX = carPosX + carPosXChange

		traffic(trafficPosX, trafficPosY)
		trafficPosY = trafficPosY + trafficSpeed
		
		car(carPosX, carPosY)
		printTimer(round(checkTime - startTime))
		countScore(score)

		if carPosX > 980 or carPosX < 220:
			crashCar()

		if trafficPosY > screenHeight:
			trafficPosY = 0 - carHeight
			trafficPosX = randrange(220, 980)
			score = score + 1

		if carPosY < (trafficPosY + carHeight):
			if carPosX > trafficPosX and carPosX < (trafficPosX + carWidth) or (carPosX + carWidth) > trafficPosX and (carPosX + carWidth) < (trafficPosX + carWidth):
				crashCar()

		pygame.display.flip()
		FPS.tick(120)

loader()
main()
pygame.quit()
quit()

# Spørre lærer: hvorfor lagger det, scrolling background
# Husk kilder


