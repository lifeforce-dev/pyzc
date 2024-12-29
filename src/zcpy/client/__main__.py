import logging
from zcpy.client.game import Game
from zcpy.common.logging import setup_logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    setup_logging(log_level=logging.INFO)

    logger.info("Client: Starting Game")
    game = Game()
    game.run()