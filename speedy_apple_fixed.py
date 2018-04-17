import pygame

pygame.init()

window = pygame.display
window_surface = pygame.display.set_mode((400, 400))

class Apple(pygame.sprite.Sprite):

    def __init__(self, image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

apple_image = pygame.image.load('./images/apple.png')
my_apple = Apple(apple_image, 100, 100)

apple_group = pygame.sprite.Group()
apple_group.add(my_apple)

clock = pygame.time.Clock()
FPS = 60

game_ended = False
while not game_ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        my_apple.rect.y -= 5
    if pressed[pygame.K_s]:
        my_apple.rect.y += 5
    if pressed[pygame.K_a]:
        my_apple.rect.x -= 5
    if pressed[pygame.K_d]:
        my_apple.rect.x += 5

    window_surface.fill((0, 0, 0))
    apple_group.draw(window_surface)

    window.update()
    clock.tick(FPS)

pygame.quit()