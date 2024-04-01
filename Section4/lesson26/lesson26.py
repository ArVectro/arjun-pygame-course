import pygame

width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game1") # This sets the title to "Game1"

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # This checks for the quit message so we can actually exit the screen
            
            GScreen.fill((255, 255, 255)) # white
            pygame.display.update() # Without updating the GScreen, the screen will still be black

if __name__ == "__main__":
    main()