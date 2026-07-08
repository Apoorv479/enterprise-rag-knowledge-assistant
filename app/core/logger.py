import logging
import sys


def setup_logger():
    """
    Configure application-wide logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


setup_logger()

logger = logging.getLogger("rag-backend")