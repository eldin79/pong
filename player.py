import pygame

from blockshape import BlockShape
from circleshape import CircleShape
from constants import PLAYER_SPEED

class Player(BlockShape):
    def __init__(self, x: float, y: float, width: float, height: float, facingRight: bool = True) -> None:
        super().__init__(x, y, width, height)
        self.facingRight = facingRight

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "white", (self.position.x, self.position.y, self.width, self.height))

    def move(self, dt: float) -> None:
        displacement_vector = pygame.Vector2(0, 1)
        displacement_vector *= PLAYER_SPEED * dt
        self.position += displacement_vector

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if self.facingRight:
            if keys[pygame.K_w]:
                self.move(-dt)
            if keys[pygame.K_s]:
                self.move(dt)
        else:
            if keys[pygame.K_UP]:
                self.move(-dt)
            if keys[pygame.K_DOWN]:
                self.move(dt)

    def collides_with(self, other: "CircleShape") -> bool:
        distance = self.position.distance_to(other.position)
        radius = self.width / 2
        if self.facingRight:
            radius += PLAYER_X
        else:
            radius += SCREEN_WIDTH - PLAYER_WIDTH - PLAYER_X
        total_radius = radius + other.radius
        return distance <= total_radius
