from enum import Enum
from dataclasses import dataclass

class DebugColors(Enum):
    BLACK = tuple[int, int, int] = (0, 0, 0)
    WHITE = tuple[int, int, int] = (255, 255, 255)
    RED = tuple[int, int, int] = (150, 50, 50)
    DARK_GREY = tuple[int, int, int] = (50, 50, 50)
    YELLOW = tuple[int, int, int] = (255, 255, 0)

class GameEvents(Enum):
    PIECE_MOVED_EVENT: str = "piece_moved"

class GameClientDefaults():
    SCREEN_WIDTH: int = 1920
    SCREEN_HEIGHT: int = 1080
    GAME_TITLE: str = "ZC Client POC"

@dataclass
class GameClientConfig():
    screen_width: int = GameClientDefaults.SCREEN_WIDTH
    screen_height: int = GameClientDefaults.SCREEN_HEIGHT
