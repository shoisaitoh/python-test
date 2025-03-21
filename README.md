# PYTHON_TEST

## 概要

- pythonのスクリプト集です。

## 実行環境

```shell
-> % python --version
Python 3.13.2
```

## ファイル一覧

- `making_input.py`
  - WebアプリケーションをRailsで作っている時、deviseのIDとPASSを手動で入れ替える時のスクリプトです。
- `box_auth.py`
  - [Box](https://box.com)を利用する際の認証です。configファイルとpemファイルがないと動きません。詳細は[公式サイト](https://ja.developer.box.com/guides/authentication/jwt/with-sdk/)をご参照ください。
- `add_collaboration.py`
  - `box_auth.py`を利用して、Boxのコラボレータを一括で任意のメールアドレスに付与するスクリプトです。
- `fastapi-test/`
  - FastAPIの学習用ディレクトリです。
- `streamlit-test/`
  - Streamlitの学習用ディレクトリです。
- `python-lib/`
  - Pythonの学習用ディレクトリです。[『もう一度プログラミングをはじめてみませんか？――人生を再起動するサバイバルガイド』](https://gihyo.jp/book/2025/978-4-297-14589-7)に影響を受けて、長期記憶に汎用できる構造が足りないことを補うために作られました。
以上
