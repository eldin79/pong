import pygame

from constants import *
from ball import Ball
from player import Player

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

    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)

    player_one = Player(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    player_two = Player(SCREEN_WIDTH - PLAYER_WIDTH - PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, False)
    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        updatable.update(dt)

        if ball.position.y < BALL_RADIUS or ball.position.y > SCREEN_HEIGHT - BALL_RADIUS:
            ball.velocity.y *= -1

        if ball.position.x < PLAYER_X + PLAYER_WIDTH + PLAYER_WIDTH / 2 and (ball.position.y >= player_one.position.y and ball.position.y <= player_one.position.y + PLAYER_HEIGHT):
            ball.velocity.x *= -1

        if ball.position.x > SCREEN_WIDTH - PLAYER_WIDTH - PLAYER_X - PLAYER_WIDTH / 2 and (ball.position.y >= player_two.position.y and ball.position.y <= player_two.position.y + PLAYER_HEIGHT):
            ball.velocity.x *= -1

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
