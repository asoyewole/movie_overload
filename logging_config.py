import logging


def setup_logging():
    logging.basicConfig(
        filename='pipeline.log',
        level=logging.INFO,
        format='%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
