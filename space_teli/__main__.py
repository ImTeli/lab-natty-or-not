import pygame
import random
from core.player import Player
from core.enemies import Enemy
from core.config import EXPLOSION_PATH, MUSIC_PATH


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def show_menu(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "SPACE TELI", 64, 400, 100)
    draw_text(screen, "Pressione qualquer tecla para iniciar...", 36, 400, 300)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Teli")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    explode = pygame.mixer.Sound(EXPLOSION_PATH)
    explode.set_volume(1)

    show_menu(screen)

    # Pontuação
    score = 0

    player = Player(400, 500)
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(player)
    enemies = pygame.sprite.Group()

    # Música

    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.set_volume(0.1)  # Define o volume da música de fundo para 10%
    pygame.mixer.music.play(-1)  # -1 significa loop infinito

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    if bullet:
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        player.laser_sound.play()

        keys_pressed = pygame.key.get_pressed()
        all_sprites.update(keys_pressed)
        enemies.update()
        bullets.update()

        # Verifica colisões entre os projéteis e os inimigos
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if hits:
            explode.play()
        score += len(hits) * 10

        # Verifica colisões entre o jogador e os inimigos
        if pygame.sprite.spritecollide(player, enemies, True):
            running = False  # Termina o jogo se houver colisão

        # Cria novos inimigos em posições aleatórias no eixo X
        if pygame.time.get_ticks() % 10 == 0:
            x_position = random.randint(0, 800)
            enemy = Enemy(x_position, -50)
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Desenha tudo na tela
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Desenha a pontuação
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
