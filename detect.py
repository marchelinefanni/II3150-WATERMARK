import cv2
import warnings
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

def detecting(watermarked, watermark):
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    correlation = np.sum(watermark * watermarked) / np.sqrt(
        np.sum(watermark**2) * np.sum(watermarked**2)
    )
    detection_threshold = 6.5
    if correlation > detection_threshold:
        print(f"Watermark Terdeteksi, Korelasi = {correlation}")
    else:
        print(f"Watermark Tidak Terdeteksi, Korelasi = {correlation}")