import pygame
import random

pygame.init()

width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bone hunter")

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

custom_text = custom_font.render("Bone hunter", True, yellow)
custom_rect = custom_text.get_rect()

custom_rect.center = (width//2, 30)

# Hudba v pozadí:
pygame.mixer.music.load("Music/background_music.mp3")
pygame.mixer.music.play()

# Pes:
dog_image = pygame.image.load("Pictures/pes.png")
dog_rect = dog_image.get_rect()

dog_rect.centerx = random.randint(0 + 20, width - 22)
dog_rect.centery = random.randint(60 + 20, height - 26)

# Java item:
decrease_item = pygame.image.load("Pictures/java-decrease.png")
decrease_item_rect = decrease_item.get_rect()

decrease_item_rect.centerx = random.randint(0 + 20, width - 22)
decrease_item_rect.centery = random.randint(60 + 20, height - 26)

# Python item:
bonus = pygame.image.load("Pictures/python-bonus.png")
bonus_rect = bonus.get_rect()

bonus_rect.centerx = random.randint(0 + 20, width - 22)
bonus_rect.centery = random.randint(60 + 20, height - 26)


# Herní cyklus:
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
               
    # Zachytávání kláves:
    keys = pygame.key.get_pressed()  
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dog_rect.top >= 60:
        dog_rect.y -= distance
        # print(dog_rect.top)
        
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dog_rect.bottom <= 600:
        dog_rect.y += distance
        # print(dog_rect.bottom)
        
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dog_rect.left >= 10:
        dog_rect.x -= distance
        # print(dog_rect.left)
        
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dog_rect.right <= 1190:
        dog_rect.x += distance
        # print(dog_rect.right)
    

    # Zachycení kolize:
    if dog_rect.colliderect(decrease_item_rect):
        print("kolize :(")
        score -= 3
        decrease_item_rect.centerx = random.randint(0 + 20, width - 22)
        decrease_item_rect.centery = random.randint(60 + 20, height - 26)
        
    if dog_rect.colliderect(bonus_rect):
        print("kolize :D")
        score += 4
        bonus_rect.centerx = random.randint(0 + 20, width - 22)
        bonus_rect.centery = random.randint(60 + 20, height - 26)
        
        
        
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
    screen.blit(dog_image, dog_rect)
    screen.blit(decrease_item, decrease_item_rect)
        # Bonus:
    screen.blit(bonus, bonus_rect)
    
    # Zobrazení textu:
    screen.blit(custom_text, custom_rect)
    screen.blit(score_text, score_rect)
    
    # Zpomalení na fps
    clock.tick(fps)
     
    # Update obrazovky:
    pygame.display.update()
    
pygame.quit()