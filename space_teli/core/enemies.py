import pygame
from core.config import ENEMY_SPRITE_PATH, ENEMY_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(ENEMY_SPRITE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensiona a imagem para 40x40 pixels
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = ENEMY_SPEED


    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()  # Remove o inimigo se sair da tela
