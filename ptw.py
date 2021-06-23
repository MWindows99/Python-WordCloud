import tweepy

# 先ほど取得した各種キーを代入する
CK="XXXX"
CS="XXXX"
AT="XXXX"
AS="XXXX"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

#画像付きツイート
api.update_with_media(status = 'WordCloud', filename = 'wordcloud_sample.png')
