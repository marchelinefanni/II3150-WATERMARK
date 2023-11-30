import cv2
from encode import watermark, watermarked, watermarking
from detect import comparing, detecting

print("WATERMARKING CITRA")
print("Selamat datang di Program Watermarking Citra!")
print("Program ini disusun oleh Marcheline Fanni Hidayat Putri (18221090)\n")
original_image = input("Masukkan nama file dari gambar awal dengan akhiran .jpg atau .png: ")
k = int(input("Masukkan noise intensity (k): "))
seed = int(input("Masukkan seed yang akan digunakan: "))
result_name = input("Masukkan nama file hasil watermarking yang diinginkan: ")
print("")

print("ENCODING...")
original_path = "input/" + original_image
result_path = "output/" + result_name + ".png"
watermark = watermark(original_path, k, seed)
watermarked = watermarked(original_path, watermark, k)
watermarking(result_name, original_path, k, seed)

compare_status = comparing(original_path, result_path)
print("COMPARE: " + compare_status)
detect_status = detecting(watermarked, watermark)