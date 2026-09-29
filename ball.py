import pygame
from circleshape import CircleShape
from constants import BALL_RADIUS, LINE_WIDTH, BALL_SPEED

class Ball(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BALL_RADIUS)
        self.velocity = pygame.Vector2(-1, -1)
        self.velocity *= BALL_SPEED

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "blue", self.position, self.radius, 0)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
