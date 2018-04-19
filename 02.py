import pygame

pygame.init()

window_surface = pygame.display.set_mode((128, 128))

lower_surface = pygame.Surface((128, 128))
lower_surface.fill((0, 255, 0))

upper_surface = pygame.Surface((64, 64))
upper_surface.fill((255, 0, 0))

while True:

    for event in pygame.event.get():
        pass

    window_surface.fill((0, 0, 0))
    window_surface.blit(lower_surface, (0, 0))
    window_surface.blit(upper_surface, (64, 64))

    pygame.display.update()

pygame.quit()
