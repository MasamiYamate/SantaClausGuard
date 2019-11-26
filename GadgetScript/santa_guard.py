import json
import logging
import sys
import threading
import signal
import time

from agt import AlexaGadget
from datetime import datetime

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class SantaGuard(AlexaGadget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    try:
        SantaGuard().main()
    finally:
        logger.info("")