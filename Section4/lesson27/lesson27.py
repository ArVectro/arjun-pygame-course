import pygame

width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game1") # This sets the title to "Game1"

def draw_fn():
    GScreen.fill((255, 255, 255)) # white
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # This checks for the quit message so we can actually exit the screen
            
            #GScreen.fill((255, 255, 255)) # white
            #pygame.display.update() # Without updating the GScreen, the screen will still be black - HOWEVER, THERE IS AN EASIER WAY TO DO THIS - by making a new function
            draw_fn()
if __name__ == "__main__":
    main()