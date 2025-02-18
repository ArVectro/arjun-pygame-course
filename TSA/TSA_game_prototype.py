import pygame 

pygame.init() # initiaties pygame
  
# create the display surface object of specific dimension e.g. (500, 500).   
win = pygame.display.set_mode((1000, 1000)) 
  
# set the pygame window name  
pygame.display.set_caption("HEIST game") 
  
# object current co-ordinates  
x = 200
y = 200
  
# dimensions of the object  
width = 32
height = 32
  
# velocity / speed of movement 
vel = 4.5
  
# Indicates pygame is running 
run = True
  
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<1000-width: 
          
        # increment in x co-ordinate 
        x += vel 
         
    # if left arrow key is pressed    
    if keys[pygame.K_UP] and y>0: 
          
        # decrement in y co-ordinate 
        y -= vel 
          
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN] and y<1000-height: 
        # increment in y co-ordinate 
        y += vel 
         
              
    # background
    win.fill((200, 200, 200)) 
      
    # rectangle
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
      
    # it refreshes the window 
    pygame.display.update()  
  
pygame.quit() 