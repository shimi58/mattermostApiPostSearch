# mattermostApiPostSearch

    MattermostAPIを用いて、Mattermostに投稿したメッセージをテキストファイルに出力するツール


## 前提

- pythonがインストール済みであること

## 使い方

1. mattermostdriverをインストール
    - powerShellまたはコマンドプロンプトで実行

        ```cmd
        pip install mattermostdriver
        ```

1. config.iniを開き、接続先、ログイン情報、検索条件を指定

    ```config.ini
    [CONNECTION]
    # MattermostのURLを指定
    scheme = http
    url = localhost
    port = 9081

    # APIでサインインするユーザーを指定
    login_id = test
    password = Password1!

    [SEARCH]
    # 検索対象のチーム名を指定
    team_name = sample
    # 検索条件を指定
    tearms = #shimizu.osamu


    [OUTPUT]
    path = ./mattermostPost.txt
    ```

1. mattermost.pyを実行する

    ```cmd
    python mattermost.py
    ```


