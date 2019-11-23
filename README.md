## About
特定のワードが呟かれたら、Slack通知するBotのソースコードです。  
あまり綺麗ではないかもしれませんが、即席で欲しい方がいればご自由にどうぞ。  

## Technology
 - python
 - sqlite3
 - heroku
 - Twitter API
 - Slack Webhook

## Setting
configファイルにはアクセスキーなどを記載します。  
ご自身でrootディレクトリーにて作成してください。  
config.pyファイルのコピペ用。  
```
CONSUMER_KEY = "*********"
CONSUMER_SECRET = "*********"
ACCESS_TOKEN = "*********"
ACCESS_TOKEN_SECRET = "*********"
WEB_HOOK_KEY = "*********"
SEARCH_KEYWORD = "*********"
CHANNEL_NAME = "#*********"
```

その他、TwitterAPIを利用するための登録、herokuの登録などはQiitaなどを参照してみてください。
