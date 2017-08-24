# PyCar | Developed by Sirajuddin Asjad and Kirisan Manivannan

# INCLUDES
from modules import *
from static import *

# MAIN
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(title)

bg = pygame.image.load("loading.png")
bg = bg.convert_alpha()
bgRect = bg.get_rect()
screen.blit(bg, bgRect)
pygame.display.flip()
time.sleep(3)
RED = (255,0,0)
screen.fill(RED)
pygame.display.flip()

car = pygame.image.load("car.png")
car = car.convert_alpha()
carRect = car.get_rect()
screen.blit(car, carRect)
pygame.display.flip()
print("hello")