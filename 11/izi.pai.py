import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("_X_Z_L_Q_W_E_R_")
clock = pygame.time.Clock()

# Drawing modes:
# 1 - freehand, 2 - rectangle, 3 - circle,
# 4 - square, 5 - right triangle, 6 - equilateral triangle, 7 - rhombus
mode = 1
color = (255, 255, 255)
start = None

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_l: mode = 1
            if e.key == pygame.K_z: mode = 2
            if e.key == pygame.K_x: mode = 3
            if e.key == pygame.K_q: mode = 4  # square
            if e.key == pygame.K_w: mode = 5  # right triangle
            if e.key == pygame.K_e: mode = 6  # equilateral triangle
            if e.key == pygame.K_r: mode = 7  # rhombus

        if e.type == pygame.MOUSEBUTTONDOWN:
            start = e.pos

        if e.type == pygame.MOUSEBUTTONUP and start:
            end = e.pos
            x1, y1 = start
            x2, y2 = end

            # --- Rectangle ---
            if mode == 2:
                rect = pygame.Rect(min(x1, x2), min(y1, y2),
                                   abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, color, rect, 2)

            # --- Circle ---
            elif mode == 3:
                center = ((x1 + x2)//2, (y1 + y2)//2)
                radius = int(((x2-x1)**2 + (y2-y1)**2)**0.5 / 2)
                pygame.draw.circle(screen, color, center, radius, 2)

            # --- Square ---
            elif mode == 4:
                side = min(abs(x2 - x1), abs(y2 - y1))
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, color, rect, 2)

            # --- Right Triangle ---
            elif mode == 5:
                pts = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, pts, 2)

            # --- Equilateral Triangle ---
            elif mode == 6:
                mid = (x1 + x2) // 2
                pts = [(mid, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, pts, 2)

            # --- Rhombus ---
            elif mode == 7:
                mx, my = (x1 + x2)//2, (y1 + y2)//2
                pts = [(mx, y1), (x2, my), (mx, y2), (x1, my)]
                pygame.draw.polygon(screen, color, pts, 2)

            start = None

    pygame.display.flip()
    clock.tick(60)