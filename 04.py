import pygame

pygame.init()

window_surface = pygame.display.set_mode((512, 512))
image = pygame.image.load('./images/04.png')

while True:

    for event in pygame.event.get():
        pass

    window_surface.fill((0, 0, 0))

    window_surface.blit(image, (0, 0))

    pygame.display.update()

pygame.quit()
