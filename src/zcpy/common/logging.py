import logging

class LoggingAlreadyConfiguredError(Exception):
    """Raised when setup_logging is called more than once."""
    pass


def setup_logging(log_level: int=logging.INFO):

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    if getattr(setup_logging, "_is_initialized", False):
        raise LoggingAlreadyConfiguredError("Only call logging.setup_logging once.")

    log_format = (
        '%(levelname)s %(asctime)s [%(module)s] %(message)s (%(pathname)s:%(lineno)d)'
    )

    logging.basicConfig(level=log_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

    setup_logging._is_initialized = True
