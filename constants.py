from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    WORD_LENGTH = 5

    FPS = 15

    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    GREY = (128,128,128)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    ORANGE = (255,128,0)
