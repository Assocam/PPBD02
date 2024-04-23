import pygame
import random
import sys

# Inizializzazione di Pygame
pygame.init()

# Definizione dei colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Impostazioni di base
WIDTH, HEIGHT = 800, 600
FPS = 60

# Creazione della finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astronave Game")

# Definizione della classe Astronave
class Astronave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Definizione della classe Ostacolo
class Ostacolo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Creazione di tutti gli sprite
all_sprites = pygame.sprite.Group()
ostacoli = pygame.sprite.Group()
astronave = Astronave()
all_sprites.add(astronave)
for i in range(8):
    ostacolo = Ostacolo()
    all_sprites.add(ostacolo)
    ostacoli.add(ostacolo)

# Loop del gioco
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    # Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aggiornamento
    all_sprites.update()

    # Controllo collisioni
    hits = pygame.sprite.spritecollide(astronave, ostacoli, False)
    if hits:
        running = False

    # Rendering
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()