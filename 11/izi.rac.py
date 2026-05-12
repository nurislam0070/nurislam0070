import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

player = pygame.Rect(180, 500, 40, 60)
enemy = pygame.Rect(180, 0, 40, 60)

coins = []
score = 0
enemy_speed = 5

font = pygame.font.SysFont(None, 36)

def spawn_coin():
    return {
        "rect": pygame.Rect(random.randint(0, 360), -20, 20, 20),
        "value": random.choice([1, 3, 5])
    }

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5

    # enemy
    enemy.y += enemy_speed
    if enemy.y > 600:
        enemy.y = 0
        enemy.x = random.randint(0, 360)

    # spawn coins
    if random.randint(1, 40) == 1:
        coins.append(spawn_coin())

    for coin in coins:
        coin["rect"].y += 5

    # collision
    for coin in coins[:]:
        if player.colliderect(coin["rect"]):
            score += coin["value"]
            coins.remove(coin)

    # increase speed
    if score >= 10:
        enemy_speed = 8

    # draw
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,255,0), player)
    pygame.draw.rect(screen, (255,0,0), enemy)

    for coin in coins:
        pygame.draw.rect(screen, (255,255,0), coin["rect"])

    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(60)