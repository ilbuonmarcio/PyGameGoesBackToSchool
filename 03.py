import pygame

pygame.init()

window = pygame.display
window_surface = window.set_mode((128, 128))

while True:

    for event in pygame.event.get():
        pass

    window_surface.fill((0, 0, 0))
    pygame.draw.line(
        window_surface, # superficie di disegno
        (255, 0, 0), # colore della linea
        (0, 0), (25, 50), # x1 y1, x2 y2
        5               # spessore linea
    )

    pygame.draw.circle(
        window_surface, # superficie di disegno
        (0, 255, 0), # colore della linea
        (64, 64), # x, y
        32, # raggio del cerchio
        2 # spessore perimetro
    )

    window.update()

pygame.quit()
