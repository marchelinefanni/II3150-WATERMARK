import cv2
import shutil
import numpy as np

def watermark(image_path, k, seed):
    # processing the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.array(image, dtype=np.int16)
    width, height = image.shape[:2]
    # creating watermark
    np.random.seed(seed)
    watermark = np.random.randint(2, size=(width, height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1
    watermark = watermark * k 
    return watermark

def watermarked(image_path, watermark, k):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    watermarked = image + k * watermark
    watermarked = np.clip(watermarked, 0, 255)
    return watermarked.astype(np.int16)

def watermarking(result_image, image_path, k, seed):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.array(image, dtype=np.int16)
    wm = watermark(image_path, k, seed)
    watermarked = cv2.add(image, wm)
    cv2.imwrite(result_image + ".png", watermarked)
    shutil.move(result_image + ".png", "output")
    print("Hasil telah tersimpan pada folder output!")

