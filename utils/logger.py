import logging
import os


def setup_logger():

    # Create logs folder if not exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("pytest_framework")

    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/test_execution.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger