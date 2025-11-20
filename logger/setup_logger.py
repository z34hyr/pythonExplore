import sys
import logging
from settings import COMMON_LOGGER_NAME

def setup_logger():
    logger = logging.getLogger(COMMON_LOGGER_NAME)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)
    formatter = logging.Formatter(
        fmt=f"%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    return logger
