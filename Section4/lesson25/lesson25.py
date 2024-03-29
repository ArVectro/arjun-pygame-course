import pygame

width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # This checks for the quit message so we can actually exit the screen

if __name__ == "__main__":
    main()