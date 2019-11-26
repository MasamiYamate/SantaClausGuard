import json, csv, re
import configparser
from requests_oauthlib import OAuth1Session

CONFIG_FILE_PATH = 'santa_guard.ini'

REQUEST_ENDPOINT = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH, 'UTF-8')

CK = config['Twitter']['ConsumerKey']
CS = config['Twitter']['ConsumerSecret']
AT = config['Twitter']['AccessToken']
ATS = config['Twitter']['AccessSecretToken']

# Tweetを取得します
def get_tweets ():
    # OAuth認証準備
    twitter = OAuth1Session(CK ,CS , AT , ATS)
    search_parameter = {'screen_name': "NoradSanta"}
    req = twitter.get(REQUEST_ENDPOINT , params = search_parameter)
    if req.status_code == 200:
        tweets = json.loads(req.text)
        print(tweets)

# 保存済みの最新のTweetIDを保存します
def get_latest_tweet_id ():
    file = open("./parms/latest_tweet_id.txt")
    latest_id = file.read()
    file.close()
    return latest_id
    
# 取得済みの最新のTweetIDを保存する
def update_latest_tweet_id (latest_id):
    file = open("./parms/latest_tweet_id.txt")
    file.write(latest_id)
    file.close()
    print('latest id update' + latestid)

if __name__ == '__main__':
    get_tweets()