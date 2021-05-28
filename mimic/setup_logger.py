import logging

logging.basicConfig(
    filename="mimic.log",
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("mimiclog")
