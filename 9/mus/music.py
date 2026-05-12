import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 28)

base = r'C:\Users\admin\Downloads'  
playlist = [
    os.path.join(base, "Eminem_-_Mockingbird_47829435.wav"),
    os.path.join(base, "Eminem_-_Not_Afraid_47965669.wav"),
    os.path.join(base, "Eminem_-_The_Real_Slim_Shady_47829433.wav")
]

current = 0
playing = False

def play():
    pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill((0,0,0))

    name = os.path.basename(playlist[current])
    text = font.render(f"Track: {name}", True, (255,255,255))
    screen.blit(text, (20, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
                playing = True

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

            if event.key == pygame.K_n:
                current = (current + 1) % len(playlist)
                play()

            if event.key == pygame.K_b:
                current = (current - 1) % len(playlist)
                play()

            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()