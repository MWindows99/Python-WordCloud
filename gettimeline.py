import json
import config
from requests_oauthlib import OAuth1Session
from time import sleep
import emoji

# 絵文字を除去
def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

# APIキー設定 (CONFIGファイルを参照)
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# Twitter API 認証処理
twitter = OAuth1Session(CK, CS, AT, ATS)

# タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# パラメータ定義 (Screen Nameに"@"以降のTwitter IDを入れる)
params = {'screen_name': 'MWindows99',
          'exclude_replies': True,
          'include_rts': False,
          'count': 200}

# 出力先ファイル
f_out = open('./output/tweet_data', 'w')

for j in range(100):
    res = twitter.get(url, params=params)
    if res.status_code == 200:
        # API残り回数を表示
        limit = res.headers['x-rate-limit-remaining']
        print("API remain: " + limit)
        if limit == 1:
            sleep(60*15)

        n = 0
        timeline = json.loads(res.text)
        # 各ツイートの本文を表示
        for i in range(len(timeline)):
            if i != len(timeline)-1:
                f_out.write(remove_emoji(timeline[i]['text']) + '\n')
            else:
                f_out.write(remove_emoji(timeline[i]['text']) + '\n')
                # 一番最後のツイートIDをパラメータmax_idに追加
                params['max_id'] = timeline[i]['id']-1

f_out.close()
