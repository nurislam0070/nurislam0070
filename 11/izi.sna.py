import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

snake = [(200,200)]
direction = (20,0)

def new_food():
    return {
        "pos": (random.randrange(0,400,20), random.randrange(0,400,20)),
        "value": random.choice([1,2,3]),
        "time": pygame.time.get_ticks()
    }

food = new_food()
score = 0

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: direction=(0,-20)
    if keys[pygame.K_DOWN]: direction=(0,20)
    if keys[pygame.K_LEFT]: direction=(-20,0)
    if keys[pygame.K_RIGHT]: direction=(20,0)

    head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
    snake.insert(0, head)

    # eat food
    if head == food["pos"]:
        score += food["value"]
        food = new_food()
    else:
        snake.pop()

    # timer (food disappears)
    if pygame.time.get_ticks() - food["time"] > 5000:
        food = new_food()

    # draw
    screen.fill((0,0,0))

    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s,20,20))

    pygame.draw.rect(screen, (255,0,0), (*food["pos"],20,20))

    pygame.display.flip()
    clock.tick(10)