# -*- coding:utf-8 -*-
import json
import logging
import sys
import threading
import signal
import time
import cities
import tweet_getter
import morphological

from agt import AlexaGadget

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class SantaGuard(AlexaGadget):
    def __init__(self):
        super().__init__()
        self.santa_radar(self)

    def santa_radar(self):
        tweets = tweet_getter.get_tweets()
        tweet = tweets[-1]

        cities = cities.get_list()
        tokens = morphological.morphological(tweet)
        isMatchTokyo = morphological.match_tokyo(tokens)
        cityName = morphological.match_city(tokens, cities)

if __name__ == '__main__':
    try:
        SantaGuard().main()
    finally:
        logger.info("")