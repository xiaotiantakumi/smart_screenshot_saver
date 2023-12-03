import json
import os
import time
from datetime import datetime
from PIL import ImageGrab
from diff_image import calculate_similarity

# デフォルトの設定
default_interval = 3
default_limit_similarity_val = 95

# 設定ファイルの読み込み
def load_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return json.load(file)
    return {}

config = load_config()
interval = config.get('interval', default_interval)
limit_similarity_val = config.get('limit_similarity_val', default_limit_similarity_val)


def create_directory():
    # 現在の年月日時分を取得
    date_str = datetime.now().strftime("%Y%m%d%H%M")
    # 年月日時分を含むディレクトリパスを生成
    directory = f"output/{date_str}"
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_screenshot(directory, quality=10, format='JPEG') -> ImageGrab:
    # ファイル名を生成（年月日時分秒）
    filename = f"{directory}/{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"

    # スクリーンショットを取得
    screenshot = ImageGrab.grab()

    # スクリーンショットがRGBAモードの場合、RGBモードに変換
    if screenshot.mode == 'RGBA':
        screenshot = screenshot.convert('RGB')

    # スクリーンショットを指定されたフォーマットと品質で保存
    screenshot.save(filename, format=format, quality=quality)

def main():
    # ディレクトリを作成
    directory = create_directory()
    latest_screenshot = ImageGrab.grab()
    while True:
        current_screenshot = ImageGrab.grab()
        similarity_val = calculate_similarity(latest_screenshot, current_screenshot)
        if latest_screenshot is not None and similarity_val < limit_similarity_val:
            latest_screenshot = current_screenshot
            save_screenshot(directory)
        time.sleep(interval)


if __name__ == "__main__":
    main()
