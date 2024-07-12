# sphinx-template


```
(ProjectRoot)/
├── .devcontainer/
│   ├── Dockerfile
│   ├── devcontainer.json
│   └── docker-compose.yml
│
├── docs/
│   ├── _build/
│   ├── _static/
│   ├── _templates/
│   ├── diagrams/
│   │   ├── class.pu
│   │   └── sequence.pu
│   ├── 1_Overview.rst
│   ├── 2_Design.rst
│   ├── 3_Others.rst
│   ├── Makefile
│   ├── README.md
│   ├── conf.py
│   ├── index.rst
│   ├── lib.rst
│   ├── make.bat
│   ├── modules.rst
│   └── myapp.rst
│
├── lib/
│   ├── __init__.py
│   ├── myclass1.py
│   └── myclass2.py
│
├── myapp.py
│
└── README.md

```

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
- [sphinx-autobuildで再ビルド、ブラウザの再リロードの手間を省いてSphinx文書をサクサク作成](sphinx-autobuildで再ビルド、ブラウザの再リロードの手間を省いてSphinx文書をサクサク作成)
