import pygame
from constants import Constants

pygame.font.init()
font = pygame.font.SysFont(None, 36)

class LetterBox:
    def __init__(self, position: tuple[int, int]):
        self.rect = pygame.Rect((0,0),(80,80))
        self.rect.center = position
        self.color = Constants.WHITE
        self.letter = ""

    def set_letter(self, letter: str) -> None:
        self.letter = letter

    def make_green(self) -> None:
        self.color = Constants.GREEN

    def make_orange(self) -> None:
        self.color = Constants.ORANGE
    
    def make_grey(self) -> None:
        self.color = Constants.GREY
    
    def draw(self, screen: pygame.Surface) -> None:
        letter_surface = font.render(self.letter, True, Constants.BLACK)
        letter_rect = letter_surface.get_rect()
        letter_rect.center = self.rect.center

        pygame.draw.rect(screen, self.color, self.rect)

        screen.blit(letter_surface, letter_rect)

        return
    
    def draw_current(self, screen: pygame.Surface) -> None:
        letter_surface = font.render(self.letter, True, Constants.BLACK)
        letter_rect = letter_surface.get_rect()
        letter_rect.center = self.rect.center

        pygame.draw.rect(screen, Constants.BLACK, self.rect.scale_by(1.1))
        pygame.draw.rect(screen, self.color, self.rect)

        screen.blit(letter_surface, letter_rect)

    def draw_false(self, screen) -> None:
        letter_surface = font.render(self.letter, True, Constants.BLACK)
        letter_rect = letter_surface.get_rect()
        letter_rect.center = self.rect.center

        pygame.draw.rect(screen, Constants.RED, self.rect.scale_by(1.1))
        pygame.draw.rect(screen, self.color, self.rect)

        screen.blit(letter_surface, letter_rect)
