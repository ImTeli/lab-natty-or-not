import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove o projétil se sair da tela
