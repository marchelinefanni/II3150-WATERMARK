import cv2
import numpy as np

def watermarking(height, width, k, seed):
    np.random.seed(seed)
    watermark = np.random.randint(2, size=(width, height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1
    watermark = watermark * k 
    return watermark


def encoding(result_image, image_path, k, seed):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.array(image, dtype=np.int16)
    image_width, image_height = image.shape[:2]
    watermark = watermarking(image_height, image_width, k, seed)
    results = cv2.add(image, watermark)
    cv2.imwrite(result_image + ".png", results)
    print("Hasil telah tersimpan di root folder!")

