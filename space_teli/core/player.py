import pygame
from core.config import PLAYER_SPRITE_PATH, PLAYER_SPEED, LASER_PATH
from core.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Redimensiona a imagem para 50x50 pixels
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 10  # Delay entre os tiros em milissegundos
        self.laser_sound = pygame.mixer.Sound(LASER_PATH)
        self.laser_sound.set_volume(0.1)

    def update(self, keys_pressed, *args):
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.laser_sound.play()
            return Bullet(self.rect.centerx, self.rect.top)
        return None