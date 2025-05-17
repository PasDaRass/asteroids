import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collision_check(self, other):
        if pygame.math.Vector2.distance_to(self.position, other.position) <= (
            self.radius + (other.radius / 2.5 )): # makes up for ship shape (PLAYER_RADIUS is now 8)       
            return True
        else:
            return False
