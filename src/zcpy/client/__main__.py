import logging
from zcpy.client.game import Game
from zcpy.common.logging import setup_logging
from zcpy.common.game_config import BuildConfigLoader

logger = logging.getLogger(__name__)
if __name__ == "__main__":
    setup_logging(log_level=logging.INFO)

    BuildConfigLoader.load()

    logger.info("Client: Starting Game")
    game = Game()
    game.run()