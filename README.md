# Smart Screenshot Saver

Smart Screenshot Saver は、デスクトップのスクリーンショットを自動的に保存し、前回のスクリーンショットとの類似度に基づいて新しいスクリーンショットを取得する Python スクリプトです。

# Getting Started

## セットアップ

このプロジェクトを使用するには、以下の手順に従ってください。

1. リポジトリをクローンします。

   ```
   git clone https://github.com/xiaotiantakumi/smart_screenshot_saver.git
   cd smart_screenshot_saver
   ```

2. 必要な依存関係をインストールします。

   ```
   pip install -r requirements.txt
   ```

## 使用方法

```bash
# venv を有効化する
source .venv/bin/activate

# gui.py を実行する
python gui.py
```

## 機能

### 定期的にスクリーンショットを取得し、output ディレクトリに保存します。

ディレクトリ名は、実行時の日付に基づいています。
保存されるスクリーンショットのファイル名は、スクリーンショットが取得された日時に基づいています。
保存されるスクリーンショットのファイル形式は、jpg です。
定期的とありますが、これはプログラムコードで設定されています。

```
interval = 3
```

この部分を変更することで、スクリーンショットの取得間隔を変更することができます。

### スクリーンショットを保存する基準

2 つの連続するスクリーンショット間の類似度を計算し、類似度が 95%未満の場合にのみ新しいスクリーンショットを保存します。
類似度の閾値の設定は以下部分でしています。
0 から 100 の間で設定することができます。単位は %です。

```
limit_similarity_val = 95
```

## 依存関係

- Python 3
- Pillow
- NumPy
- OpenCV

## スクリプトの説明

- `smart_screenshot_saver.py`: スクリーンショットを定期的に取得し、保存するメインスクリプトです。
- `diff_image.py`: 2 つの画像間の類似度を計算するユーティリティスクリプトです。
- `smart_screenshot_saver.sh`: スクリーンショットの自動保存を開始するためのシェルスクリプトです。
- `stop_smart_screenshot_saver.sh`: スクリーンショットの自動保存を停止するためのシェルスクリプトです。

## 変更を加えた場合に requirement.txt を更新する方法

```bash
pip freeze > requirements.txt
```

## ライセンス

このプロジェクトは[ライセンス名]の下で公開されています。
