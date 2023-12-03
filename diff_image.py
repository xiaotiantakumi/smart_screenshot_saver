import sys
import cv2
from PIL import Image, ImageChops
import numpy as np

def calculate_similarity(img1, img2) -> float:
    # 画像を同じサイズにする
    img1 = img1.resize(img2.size)

    # 画像をnumpy配列に変換
    img1_np = np.array(img1)
    img2_np = np.array(img2)

    # 差分を計算
    diff = np.abs(img1_np - img2_np)

    # 差分の合計を最大可能差分で割って、類似度を計算
    max_diff = np.prod(diff.shape) * 255
    similarity = (1 - np.sum(diff) / max_diff) * 100

    return similarity

def diff_images(img1, img2, output_path):
    # 画像を同じサイズにする
    img1 = img1.resize(img2.size)

    # PILで差分を計算
    diff = ImageChops.difference(img1, img2)

    # 差分を保存
    diff.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff-image.py <image1> <image2>")
        sys.exit(1)

    # 画像を読み込む
    img1 = Image.open(sys.argv[1])
    img2 = Image.open(sys.argv[2])
    # diff_images(img1, img2, "diff_output.jpg")
    similarity_val = calculate_similarity(img1, img2)
    print(f"Similarity: {similarity_val:.1f}%")
