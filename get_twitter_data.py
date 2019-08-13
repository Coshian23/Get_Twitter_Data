import tweepy
import datetime

def gettwitterdata(keyword,dfile):

    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = "xTjNpPAMLpjNQgHUaIJcuLVQJ"
    Consumer_secret = "o8Dziw80QpOck4ThmOaO7kQbYJQgYLKb7JeGxsKpWC0q6nksKD"
    Access_token = "1057214897946165248-xqkpkQIQQTi7AQRHjeOXrne4P9QPGk"
    Access_secret = "4VqE1WQxWpr7ysfiFgCxEplV6Ky5hMJpdVLTjs47oST0u"

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():

        #つぶやき時間がUTCのため、JSTに変換  ※デバック用のコード
        jsttime = tweet.created_at + datetime.timedelta(hours=9)
        print(jsttime)

        #つぶやきテキスト(FULL)を取得
        tweets_data.append(tweet.full_text + '\n')


    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)


if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    gettwitterdata(keyword,dfile)