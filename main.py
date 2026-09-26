import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ball import Ball

def main():
    print(f"Starting Pong with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Ball.containers = (updatable, drawable)

    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        updatable.update(dt)

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
