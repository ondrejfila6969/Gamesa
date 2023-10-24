import pygame
import random

pygame.init()

width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python hunter")

# Nadefinované barvy (RGB):
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Základní nastavení:
clock = pygame.time.Clock()
fps = 70 
distance = 15
score = 0


# Custom font:
custom_font = pygame.font.Font("Font/custom.otf", 40)

custom_text = custom_font.render("Python hunter", True, yellow)
custom_rect = custom_text.get_rect()

custom_rect.center = (width//2, 30)

# Hudba v pozadí:
pygame.mixer.music.load("Music/background_music.mp3")
pygame.mixer.music.play()

# pygame.mixer.music.play()

# Notebook:
notebook_image = pygame.image.load("Pictures/notebook.png")
notebook_image_rect = notebook_image.get_rect()

notebook_image_rect.centerx = random.randint(0 + 20, width - 10)
notebook_image_rect.centery = random.randint(60 + 20, height - 26)

# Python item:
python = pygame.image.load("Pictures/python-bonus.png")
python_rect = python.get_rect()

python_rect.centerx = random.randint(0 + 20, width - 22)
python_rect.bottom = random.randint(height - 550, height - 32)


# Herní cyklus:
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
               
    # Zachytávání kláves:
    keys = pygame.key.get_pressed()  
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and notebook_image_rect.top >= 70:
        notebook_image_rect.y -= distance
        # print(notebook_image_rect.top)
        
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and notebook_image_rect.bottom <= 590:
        notebook_image_rect.y += distance
        # print(notebook_image_rect.bottom)
        
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and notebook_image_rect.left >= 20:
        notebook_image_rect.x -= distance
        # print(notebook_image_rect.left)
        
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and notebook_image_rect.right <= 1180:
        notebook_image_rect.x += distance
        # print(notebook_image_rect.right)
    

    # Zachycení kolize:
    
    if notebook_image_rect.colliderect(python_rect):
        # print("kolize")
        score += 1
        python_rect.centerx = random.randint(0 + 27, width - 22)
        python_rect.centery = random.randint(60 + 27, height - 22)
        print(python_rect.centery)

    # Překrývání obrazovky:
    screen.fill(black)
    
    # Ohraničení:
    pygame.draw.line(screen, yellow, (0, 60), (width, 60), 2)        

    # Text skore:
    score_text = custom_font.render(f"Score: {score}", True, yellow)
    score_rect = score_text.get_rect()

    score_rect.x = 10
    score_rect.y = 6
    
    # Zobrazování obrázků:
    screen.blit(notebook_image, notebook_image_rect)
    screen.blit(python, python_rect)
    
    # Zobrazení textu:
    screen.blit(custom_text, custom_rect)
    screen.blit(score_text, score_rect)
    
    # Zpomalení na fps
    clock.tick(fps)
     
    # Update obrazovky:
    pygame.display.update()
    
pygame.quit()