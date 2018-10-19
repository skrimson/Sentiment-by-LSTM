import json, config
import pandas as pd
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/search/tweets.json"

print("search term:")
keyword = input('>> ') + " -rt"
print('-------------------------------------')

#search term and number of tweets to retrieve
params = {'q': keyword, 'count': 100, 'lang':'en'}

req = twitter.get(url, params = params)

#prepare pandas DataFrame
df = pd.DataFrame(columns=["Datatime", "User", "Text"])

if req.status_code == 200:
    search_timeline = json.loads(req.text)
    for tweet in search_timeline['statuses']:
        #not allow mention tweets
        if tweet['entities']['user_mentions']:
            continue
        created_at = (tweet["created_at"])
        User = (tweet["user"]["screen_name"])
        Text = (tweet["text"])
        tmp_df = pd.Series([created_at, User, Text], index=df.columns)

        #append to dataframe
        df = df.append(tmp_df, ignore_index=True)
    df.to_csv('../tweet_data.csv')

else:
    print("ERROR: %d" % req.status_code)
