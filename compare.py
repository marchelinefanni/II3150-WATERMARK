import cv2
import numpy as np 

def comparing(original_path, watermarked_path):
    original_image = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    watermarked_image = cv2.imread(watermarked_path, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(original_image, watermarked_image)
    total_diff = np.sum(diff)
    
    threshold = 100000
    if total_diff > threshold:
        return "Gambar memiliki watermark"
    else:
        return "Gambar tidak memiliki watermark"

