import pygame
from constants import Constants
from game_screen import Game

pygame.init()


SCREEN_WIDTH = Constants.SCREEN_WIDTH
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Wordle')

game = Game(screen)

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(Constants.FPS)

    screen.fill(Constants.BLUE)

    game.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = Game(screen)
            if game.finished:
                continue
            elif event.key == pygame.K_BACKSPACE:
                game.letter_deleted()
            elif event.key == pygame.K_SPACE:
                game.word_inserted()
            elif event.key in range(32, 127):
                letter = chr(event.key)
                game.letter_inserted(letter)
    
    pygame.display.update()


pygame.quit()