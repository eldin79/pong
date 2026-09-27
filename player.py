import pygame

from blockshape import BlockShape
from circleshape import CircleShape

class Player(BlockShape):
    def __init__(self, x: float, y: float, width: float, height: float, facingRight: bool = True) -> None:
        super().__init__(x, y, width, height)
        self.facingRight = facingRight

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "white", (self.position.x, self.position.y, self.width, self.height))

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def collides_with(self, other: "CircleShape") -> bool:
        distance = self.position.distance_to(other.position)
        radius = self.width / 2
        if self.facingRight:
            radius += 0
        else:
            radius += 0
        total_radius = radius + other.radius
        return distance <= total_radius
