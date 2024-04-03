import pygame
from constants import Constants
from letter_box import LetterBox
from word import *


def generate_rects() -> list[LetterBox] :
    rects = []
    for row in range(6):
        for letter_index in range(Constants.WORD_LENGTH):
            box = LetterBox((60+90*letter_index, 60+100*row))
            rects.append(box)
    return rects

class Game():
    def __init__(self, screen: pygame.Surface) -> None:
        self.word = generate_word()
        self.letter_list = format_word(self.word)
        print(self.word)
        self.words_inserted = 0
        self.boxes: list[LetterBox] = generate_rects()
        self.current_word = []
        self.finished = False
        self.screen = screen
        self.pause_frames = 0

    def letter_inserted(self, letter: str) -> None:
        if len(letter) > 1:
            raise ValueError("This is not a single character")
        if "a" > letter or "z" < letter or len(self.current_word) >= Constants.WORD_LENGTH:
            return
        self.boxes[Constants.WORD_LENGTH*self.words_inserted+len(self.current_word)].set_letter(letter)
        self.current_word.append(letter)
    
    def letter_deleted(self) -> None:
        if self.current_word == []:
            return
        self.boxes[Constants.WORD_LENGTH*self.words_inserted+len(self.current_word)-1].set_letter("")
        self.current_word.pop()


    def word_inserted(self) -> None:
        if len(self.current_word) < Constants.WORD_LENGTH:
            print("Not full word")
            return
        word = ''.join(self.current_word)
        if not check_if_exists(word):
            self.word_doesnt_exist()
            return            

        for letter_index, letter in enumerate(word):
            if self.letter_list.get(letter) is None:
                self.boxes[Constants.WORD_LENGTH*self.words_inserted+letter_index].make_grey()
            elif letter_index in self.letter_list[letter]:
                self.boxes[Constants.WORD_LENGTH*self.words_inserted+letter_index].make_green()
            else:
                self.boxes[Constants.WORD_LENGTH*self.words_inserted+letter_index].make_orange()
        if word == self.word:
            self.finished = True
        self.current_word = []
        self.words_inserted += 1
        return

    def word_doesnt_exist(self) -> None:
        self.pause_frames = 10
        for i in range(Constants.WORD_LENGTH):
            self.boxes[self.words_inserted*Constants.WORD_LENGTH+i].set_letter("")
        self.current_word = []


    def draw(self) -> None:
        for box_index, box in enumerate(self.boxes):
            if self.pause_frames > 0:
                if box_index//Constants.WORD_LENGTH == self.words_inserted:
                    box.draw_false(self.screen)
                    self.pause_frames -= 1
                    continue
            if box_index == Constants.WORD_LENGTH*self.words_inserted+len(self.current_word) and len(self.current_word) < Constants.WORD_LENGTH:
                box.draw_current(self.screen)
            else:
                box.draw(self.screen)
        if self.finished:
            game_finished(self.screen)
        return
    
pygame.font.init()
font = pygame.font.SysFont(None, 36)

def game_finished(screen: pygame.Surface):
    letter_surface = font.render("You won!!", True, Constants.BLACK)
    letter_rect = letter_surface.get_rect()
    letter_rect.center = (400,620)

    screen.blit(letter_surface, letter_rect)
    

