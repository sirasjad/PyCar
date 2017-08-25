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

# FUNCTIONS
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
	blueCar = blueCar.convert_alpha()
	screen.blit(blueCar, (x, y))

def car(x, y):
	carImg = pygame.image.load('inc/car.png')
	carImg = carImg.convert_alpha()
	screen.blit(carImg, (x, y))

def textprint(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def displaytext(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	textSurface, textRectangle = textprint(text, largeText)
	textRectangle.center = ((screenWidth/2), (screenHeight/2))
	screen.blit(textSurface, textRectangle)
	pygame.display.flip()
	sleep(2)
	main()

def crashCar():
	displaytext('GAME  OVER')

def background(y):
	backImg = pygame.image.load('inc/road.jpg')
	backImg = backImg.convert_alpha()
	backImgHeight = backImg.get_rect().height
	scrollY = y % backImgHeight
	screen.blit(backImg, (0, scrollY - backImgHeight))
	if scrollY < screenHeight:
		screen.blit(backImg, (0, scrollY))

def loader():
	loadTime = time()
	loading = True
	while loading:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		loadImg = pygame.image.load('inc/loading.png')
		loadImg = loadImg.convert_alpha()
		loadRectangle = loadImg.get_rect()
		screen.blit(loadImg, loadRectangle)
		pygame.display.flip()
		
		if time() > (loadTime + 7):
			screen.fill(white)
			pygame.display.flip()
			loading = False

# MAIN FUNCTION
def main():
	carPosX = 610
	carPosY = 475
	carPosXChange = 0
	backImgScrollSpeed = 0
	trafficPosX = randrange(220, 980)
	trafficPosY = -600
	trafficSpeed = 5
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
					carPosXChange = -25
				elif event.key == pygame.K_RIGHT:
					carPosXChange = 25
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					carPosXChange = 0
		
		checkTime = time()	
		background(backImgScrollSpeed)

		if checkTime >= startTime:
			backImgScrollSpeed = backImgScrollSpeed + 10
			
		if checkTime > (startTime + 10):
			trafficSpeed = 8
			backImgScrollSpeed = backImgScrollSpeed + 13
			
		if checkTime > (startTime + 20):
			trafficSpeed = 12
			backImgScrollSpeed = backImgScrollSpeed + 17
			
		if checkTime > (startTime + 35):
			trafficSpeed = 25
			backImgScrollSpeed = backImgScrollSpeed + 20
			
		if checkTime > (startTime + 40):
			trafficSpeed = 35
		
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
		FPS.tick(500)

loader()
main()
pygame.quit()
quit()

