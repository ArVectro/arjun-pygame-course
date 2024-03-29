import pygame
import os

width, height = 800, 600

FPS = 60 # we need to specify the frame rate so that the game runs the same in every computer no matter how fast the computer is running

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game1") # This sets the title to "Game1"
PICTURE = pygame.image.load(os.path.join('Users', 'arjun', 'pythoncode', 'mystuff', 'recources','download.jpg')) # This is our picture from the folder 'resources'

def draw_fn():
    GScreen.fill((255, 255, 255)) # white
    GScreen.blit(PICTURE, (0,0))
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # This checks for the quit message so we can actually exit the screen
            
            #GScreen.fill((255, 255, 255)) # white
            #pygame.display.update() # Without updating the GScreen, the screen will still be black - HOWEVER, THERE IS AN EASIER WAY TO DO THIS - by making a new function
            draw_fn()
if __name__ == "__main__":
    main()