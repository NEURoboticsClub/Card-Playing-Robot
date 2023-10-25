import pygame

pygame.init()

# Game variables and constand
WIDTH = 600
HEIGHT = 600
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

fps = 60
timer = pygame.time.Clock()

# Create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Matching Game")
title_font = pygame.font.Font("freesansbold.ttf", 56)
small_font = pygame.font.Font("freesansbold.ttf", 26)


def draw_backgroun():
    top_menu = pygame.draw.rect(screen, black, [0,0,WIDTH, 100])
    title_text = title_font.render("The Matching Game!", True, white)
    screen.blit(title_text, (10, 20))
    board_space = pygame.draw.rect(screen, gray, [0,100,WIDTH, HEIGHT-200])
    bottom_menu = pygame.draw.rect(screen, black, [0,HEIGHT-100 ,WIDTH, 100])


running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    draw_backgroun()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
pygame.quit()