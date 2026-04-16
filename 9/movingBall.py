import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")

WHITE = (255,255,255)
RED = (255,0,0)

x, y = 400, 300
radius = 25
speed = 20

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x - speed - radius >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + speed + radius <= WIDTH:
                x += speed
            if event.key == pygame.K_UP and y - speed - radius >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + speed + radius <= HEIGHT:
                y += speed

    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()