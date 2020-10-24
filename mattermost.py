from mattermostdriver import Driver
import configparser

# 定義読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

# Mattermostログイン
connection = Driver({
    'url': config_ini['CONNECTION']['url'],
    'login_id': config_ini['CONNECTION']['login_id'],
    'password': config_ini['CONNECTION']['password'],
    'scheme': config_ini['CONNECTION']['scheme'],
    'basepath': '/api/v4',
    'verify': True,
    'port': int(config_ini['CONNECTION']['port']),
    })
connection.login()

# チーム名からTeam IDを取得
teamId = connection.api['teams'].get_team_by_name(config_ini['SEARCH']['team_name'])['id']

# 検索条件に合致する投稿を取得
postMessage = connection.api['posts'].search_for_team_posts(teamId,options={
'terms': config_ini['SEARCH']['tearms']
})

#ファイルオープン
with open(config_ini['OUTPUT']['path'], 'w') as f:

  #検索結果を出力
  for post in postMessage['posts'].values():
    print(post['message'], file=f)
    #区切り文字
    print('====================', file=f)
