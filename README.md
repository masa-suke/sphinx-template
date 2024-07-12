# sphinx-template

## 概要
### 目的
小規模アプリもしくは、モデル開発コードのドキュメントテンプレートを提供すること。
詳細設計レベルのドキュメントとして、主に、以下3点をドキュメントに含めることを想定。
- 構成/動作/状態遷移図を説明するドキュメント
- その他(TIPS等)
- APIリファレンス(Pythonコード中のdocstringをSphinxで出力)

### フォルダ構成
```
(ProjectRoot)/
│
├── .devcontainer/  # Sphinx環境のコンテナ関連ファイル一色
│   ├── Dockerfile
│   ├── devcontainer.json
│   └── docker-compose.yml
│
├── docs/
│   ├── _build/         # ドキュメント出力場所
│   ├── _static/
│   ├── _templates/
│   ├── diagrams/       # ドキュメントに含めるダイアグラムの格納場所
│   │   ├── class.pu
│   │   └── sequence.pu
│   ├── 1_Overview.rst  # ドキュメント(1/3) Overview
│   ├── 2_Design.rst    # ドキュメント(2/3) Design
│   ├── 3_Others.rst    # ドキュメント(3/3) Others
│   ├── Makefile
│   ├── README.md
│   ├── conf.py         # Sphinx設定ファイル
│   ├── index.rst       # ドキュメントTopPage
│   ├── lib.rst         # lib/以下のTOC
│   ├── make.bat
│   ├── modules.rst     
│   └── myapp.rst       # myapp.pyのクロスリファレンス
│
├── lib/
│   ├── __init__.py
│   ├── myclass1.py # APIリファレンスに含めるpyファイル
│   └── myclass2.py # APIリファレンスに含めるpyファイル
├── myapp.py        # APIリファレンスに含めるpyファイル
│
└── README.md
```

## ドキュメント生成Steps
ざっくり...以下のファイルを変更する
- (ドキュメント(.rst)を追加し場合) `index.rst`を編集
- (`root`にファイル追加した場合) `modules.rst`を編集
- (`lib/`以下にファイルを追加した場合) `lib.rst`を編集
- ビルド
    ```bash
    cd docs
    make html
    ```
詳細はT.B.D

## TIPS
### autobuild
Sphinxドキュメント保存のたびに自動ビルド、ブラウザをリロードしてくれる
```
# sphinx-autobuild docs docs/_build/html
[sphinx-autobuild] Starting initial build
・・・(省略)・・・
dumping object inventory... done
build succeeded.

The HTML pages are in docs/_build/html.
[sphinx-autobuild] Serving on http://127.0.0.1:8000
[sphinx-autobuild] Waiting to detect changes...
```

## 参考
- [Sphinx](https://www.sphinx-doc.org/ja/master/)
- [Sphinx-Users.jp](https://sphinx-users.jp/gettingstarted/index.html)
- [sphinx-autobuildで再ビルド、ブラウザの再リロードの手間を省いてSphinx文書をサクサク作成](sphinx-autobuildで再ビルド、ブラウザの再リロードの手間を省いてSphinx文書をサクサク作成)
