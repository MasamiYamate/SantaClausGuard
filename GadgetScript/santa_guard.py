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

    # サンタクロースの追跡開始時のタスク
    def on_custom_santaradar_start(self):
        self.is_persistence_run = True

        # セッションの永続化を開始する
        self.session_persistence_thread = threading.Thread(target=self.session_persistence)
        self.session_persistence_thread.start()

        # サンタクロースの追跡を開始する
        self.santaradar_thread = threading.Thread(target=self.santa_radar)
        self.santaradar_thread.start()

    # サンタクロース追跡終了時のタスク
    def on_custom_santaradar_end(self):
        self.is_persistence_run = False

        self.session_persistence_thread.clear()
        self.santaradar_thread.clear()

    # サンタクロースの追跡を行う定期タスク
    def santa_radar(self):
        while self.is_persistence_run:
            tweets = tweet_getter.get_tweets()
            tweet = tweets[-1]

            cities = cities.get_list()
            tokens = morphological.morphological(tweet)
            is_match_japan = morphological.match_japan(tokens)
            cityName = morphological.match_city(tokens, cities)

            # サンタが日本に来ているか判別する
            if is_match_japan and city_name != None:
                # サンタが日本に来ている場合
                payload = {'city_ame': city_name }
                self.send_custom_event(
                    'Custom.SantaGuard', 'SkillHandler', payload)

            # レートリミットに当たるのを回避するために単純に2分間隔でリクエストする
            time.sleep(120)

    # セッションを永続化する処理 30秒おきにAlexaにSendする
    def session_persistence(self):
        while self.is_persistence_run:
            self.send_custom_event(
                'Custom.SantaGuard', 'SkillHandler', {})
            time.sleep(30)


if __name__ == '__main__':
    try:
        SantaGuard().main()
    finally:
        logger.info("")