import pygame

pygame.init()

WIDTH  =  500
HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

reload = pygame.mixer.Sound("reload.wav")
gun = pygame.mixer.Sound("gunshot.wav")
pygame.display.set_caption('PP1')
cursor = pygame.image.load('cursor.png')
largeText = pygame.font.Font('PressStart2P.ttf', 15)
titleText = pygame.font.Font('PressStart2P.ttf', 15)

ammo = 10
ammo_text = 'Ammo: ' + str(ammo)
Reloadtxt = largeText.render("PRESS 'R' TO RELOAD", True, RED)
gameLoop = True
frame = 0

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 290 > pos[0] > 190 and 320 < pos[1] < 370:
                    intro = False
        titleText = pygame.font.Font('PressStart2P.ttf', 20)
        screen.blit(titleText.render('PLAYER POINTER 1', True, WHITE), [90, 260])
        pygame.draw.rect(screen, WHITE, (190, 320, 100, 50))

        buttonText = pygame.font.Font('PressStart2P.ttf', 20)
        screen.blit(buttonText.render('PLAY', True, BLACK), [200, 335])


        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

while gameLoop:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ammo -= 1
            if ammo <= 0:
                ammo = 0
                ammo_text = 'RELOAD'
            else:
                ammo_text = 'Ammo: ' + str(ammo)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and ammo == 0:
            pygame.mixer.Sound.play(reload)
            ammo = 10
            ammo_text = 'Ammo: ' + str(ammo)
    screen.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor, [mouse_x - 25, mouse_y - 25])
    textSurface = largeText.render(ammo_text, True, WHITE)
    if ammo <= 0 and frame % 6 == 0:
        screen.blit(Reloadtxt, [110, 10])
    screen.blit(textSurface, [10, 480])
    pygame.display.flip()
    clock.tick(60)
