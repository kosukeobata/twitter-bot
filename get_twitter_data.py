# -*- coding:utf-8 -*-
import json, requests, sqlite3, config, db_access
from requests_oauthlib import OAuth1Session
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

TWITTER_API_URL = "https://api.twitter.com/1.1/search/tweets.json"
SLACK_WEB_HOOK_URL = "https://hooks.slack.com/services/" + config.WEB_HOOK_KEY
LAST_UPDATE_ID = db_access.find()

params = {
  'q' : config.SEARCH_KEYWORD,
  'lang' : 'ja',
  'result_type' : 'mixed',
  'since_id' : LAST_UPDATE_ID
}

req = twitter.get(TWITTER_API_URL, params = params)

if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline['statuses']:
        requests.post(SLACK_WEB_HOOK_URL, data = json.dumps({
            'text': 'https://twitter.com/'+tweet['user']['screen_name']+'/status/'+str(tweet['id']),
            'username': 'コウペンちゃん',
            'channel' : config.CHANNEL_NAME,
            'icon_url' : 'http://spiralcute.com/characters/HP%E3%82%B3%E3%82%A6%E3%83%9A%E3%83%B38.png',
            'link_names': 1,
        }))

    row_num = len(timeline['statuses'])

    if row_num > 0:
        recent_last_id = timeline['statuses'][0]['id']
        db_access.update(recent_last_id)


else:
    print("ERROR: %d" % req.status_code)
