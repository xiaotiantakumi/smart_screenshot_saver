import os
import time
from datetime import datetime
from PIL import ImageGrab
from diff_image import calculate_similarity

# 時間間隔(秒)
interval = 3
# 類似度の閾値
limit_similarity_val = 95

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
