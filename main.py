import pygame
import random
import sys

# Pygame'i başlat
pygame.init()

# Oyun penceresi boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Demo - Top Yakalama Oyunu")

# FPS kontrolü
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (50, 150, 255)
RED   = (220, 50, 50)
DARK_RED = (120, 0, 0)

# Oyuncu çubuğu
player_width = 120
player_height = 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - 50
player_speed = 8

# Top
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = -ball_radius
ball_speed = 5

# Skor ve can
score = 0
lives = 3

font = pygame.font.SysFont("Arial", 26)
big_font = pygame.font.SysFont("Arial", 48)

# Kaçırınca ekranın kırmızı yanıp sönmesi için sayaç
miss_flash_timer = 0      # 0 iken normal, >0 iken kırmızı ekran

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Klavye girişleri
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Ekran dışına taşmayı engelle
        if player_x < 0:
            player_x = 0
        if player_x + player_width > WIDTH:
            player_x = WIDTH - player_width

        # Topun hareketi
        ball_y += ball_speed

        # Top ekranın altına düştüyse (kaçırdıysan)
        if ball_y - ball_radius > HEIGHT:
            lives -= 1                     # can azalt
            miss_flash_timer = 15          # 15 frame kırmızı yan
            # topu yeniden yukarıdan başlat
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)
            ball_y = -ball_radius

            # Canlar bittiyse oyun biter
            if lives <= 0:
                game_over = True

        # Çarpışma kontrolü (yakalanınca)
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius,
                                ball_radius * 2, ball_radius * 2)

        if player_rect.colliderect(ball_rect):
            score += 1
            # topu yeniden yukarıdan başlat
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)
            ball_y = -ball_radius

    # Ekranı çizme
    if miss_flash_timer > 0:
        screen.fill(DARK_RED)   # kaçırınca kısa süre kırmızı
        miss_flash_timer -= 1
    else:
        screen.fill(BLACK)

    # Oyuncu ve topu çiz
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLUE, player_rect)

    if not game_over:
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Skor ve can yazıları
    score_text = font.render(f"Skor: {score}", True, WHITE)
    lives_text = font.render(f"Can: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    # Oyun bittiyse ekrana mesaj yaz
    if game_over:
        over_text = big_font.render("OYUN BITTI", True, WHITE)
        info_text = font.render("Kapatmak icin pencereyi kapatin.", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2,
                                HEIGHT // 2 - over_text.get_height() // 2 - 20))
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2,
                                HEIGHT // 2 - info_text.get_height() // 2 + 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
