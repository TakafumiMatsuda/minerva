import tweepy
import os
# coding: UTF-8


def favorite_automated(words, favs):

    # ---API key
    # #ローカルで動かす時
    # from config import config
    # # CONSUMER_KEY = config.CONSUMER_KEY
    # # CONSUMER_SECRET = config.CONSUMER_SECRET
    # # ACCESS_TOKEN = config.ACCESS_TOKEN
    # # ACCESS_SECRET = config.ACCESS_SECRET

    # #herokuで動かすとき
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN_KEY"]
    ACCESS_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    # インスタンス生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    for word in words:
        word = word+' -bot'+' -相互フォロー'+' -シド神'+' -セックス'+' -オフパコ'+' -美少女'+' -おっぱ'+' exclude:retweets'
        #word = word + '-bot -オフパコ -相互フォロー -セフレ' + ' exclude:retweets' + ' min_faves:100'
        print(word)
        search_results = api.search_tweets(q=word, count=favs)
        for result in search_results:
            tweet_id = result.id #Tweetのidを取得
            user_id = result.user._json['id'] #ユーザーのidを取得
            try:
                api.create_favorite(tweet_id) #ファボする
                # api.create_friendship(user_id) #フォローする
            except Exception as e:
                print(e)
    

if __name__ == '__main__':
    words = ['"ロジカルシンキング"', '"科学的思考"', '"科学的手法"', '"サイエンスコミュニケーター"', '"研究者志望"', '"院試"', '"ポスドク"']
    words = ['"フラーレン"', '"有機化学合成"', '"アーク放電法"', '"アルゴンガス"', '"コランニュレン"', '"ベンゼン環"']
    favs = 10
    favorite_automated(words, favs)