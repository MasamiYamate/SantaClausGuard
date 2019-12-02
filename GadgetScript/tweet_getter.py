import json, csv, re
import configparser
from requests_oauthlib import OAuth1Session

CONFIG_FILE_PATH = 'santa_guard.ini'

REQUEST_ENDPOINT = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Tweetを取得します
def get_tweets ():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH, 'UTF-8')

    CK = config['Twitter']['ConsumerKey']
    CS = config['Twitter']['ConsumerSecret']
    AT = config['Twitter']['AccessToken']
    ATS = config['Twitter']['AccessSecretToken']

    # OAuth認証準備
    twitter = OAuth1Session(CK ,CS , AT , ATS)
    last_id = get_latest_tweet_id()

    search_parameter = {'screen_name': "NoradSanta" , 'since': last_id}
    print(search_parameter)
    req = twitter.get(REQUEST_ENDPOINT , params = search_parameter)
    print(req.status_code)
    if req.status_code == 200:
        user_timelines = json.loads(req.text)

        # 最新のIDを取得する
        latest_id = user_timelines[0]['id']
        update_latest_tweet_id(str(latest_id))

        # テキストを抽出
        tweets = list(map(lambda x: extraction_tweet(x), user_timelines))

        print(tweets)

        return tweets

# Tweet内容を抜き出します
def extraction_tweet (tweet):
    tweet_text = tweet['text']
    return tweet_text


# 保存済みの最新のTweetIDを保存します
def get_latest_tweet_id ():
    file = open("./parms/latest_tweet_id.txt")
    latest_id = file.read()
    file.close()
    return latest_id
    
# 取得済みの最新のTweetIDを保存する
def update_latest_tweet_id (latest_id):
    file = open("./parms/latest_tweet_id.txt", "w")
    file.write(latest_id)
    file.close()
    print('latest id update' + latest_id)

if __name__ == '__main__':
    get_tweets()