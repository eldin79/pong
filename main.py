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
    pygame.display.set_caption("Pong")

    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    player_one_wins_text = font.render("Player One Wins!", True, "red")
    player_two_wins_text = font.render("Player Two Wins!", True, "red")
    text_rect_one = player_one_wins_text.get_rect()
    text_rect_two = player_two_wins_text.get_rect()
    text_rect_one.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    text_rect_two.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    restart_text = font.render("Press R to restart", True, "green")
    restart_rect = restart_text.get_rect()
    restart_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + RESTART_TEXT_ADJUST_Y)

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
    player_one_wins = False
    player_two_wins = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        if not player_one_wins and not player_two_wins:
            updatable.update(dt)

        if ball.position.y < BALL_RADIUS or ball.position.y > SCREEN_HEIGHT - BALL_RADIUS:
            ball.velocity.y *= -1

        if ball.position.x < PLAYER_X + PLAYER_WIDTH + PLAYER_WIDTH / 2 and (ball.position.y >= player_one.position.y and ball.position.y <= player_one.position.y + PLAYER_HEIGHT):
            ball.velocity.x *= -1

        if ball.position.x > SCREEN_WIDTH - PLAYER_WIDTH - PLAYER_X - PLAYER_WIDTH / 2 and (ball.position.y >= player_two.position.y and ball.position.y <= player_two.position.y + PLAYER_HEIGHT):
            ball.velocity.x *= -1

        if ball.position.x < 0 - BALL_RADIUS:
            player_two_wins = True
            screen.blit(player_two_wins_text, text_rect_two)
            screen.blit(restart_text, restart_rect)

        if ball.position.x > SCREEN_WIDTH + BALL_RADIUS:
            player_one_wins = True
            screen.blit(player_one_wins_text, text_rect_one)
            screen.blit(restart_text, restart_rect)

        if player_one_wins or player_two_wins:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                print("Restart game")
                ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player_one_wins = False
                player_two_wins = False

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
