# PyCar | Developed by Sirajuddin Asjad and Kirisan Manivannan

# INCLUDES
from modules import *
from variables import *

# MAIN
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(title)
FPS = pygame.time.Clock()

def car(x, y):
	carImg = pygame.image.load('car.png')
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
	time.sleep(3)
	main()

def crashCar():
	message_display('You crashed!')

def main():
	carPosX = 500
	carPosY = 330
	carPosXChange = 0

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
		
		carPosX = carPosX + carPosXChange
		screen.fill(white)
		car(carPosX, carPosY)
		
		crashLimit = screenWidth - carWidth
		if carPosX > crashLimit or carPosX < 0:
			crashCar()
			
		pygame.display.flip()
		FPS.tick(120)

main()
pygame.quit()
quit()











