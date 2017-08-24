# PyCar | Developed by Sirajuddin Asjad and Kirisan Manivannan

# INCLUDES
from modules import *
from static import *

# MAIN
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(project)

bg = pygame.image.load("bg.png")
bg = bg.convert_alpha()
time.sleep(3)
bgrect = bg.get_rect()
print(bgrect)
screen.blit(bg, bgrect)
pygame.display.flip()
time.sleep(5)