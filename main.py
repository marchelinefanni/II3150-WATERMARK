from encode import encoding
from compare import comparing 

print("WATERMARKING CITRA")
print("Selamat datang di Program Watermarking Citra!")
print("Program ini disusun oleh Marcheline Fanni Hidayat Putri (18221090)")
original_image = input("Masukkan nama file dari gambar awal dengan akhiran .jpg atau .png: ")
k = int(input("Masukkan noise intensity (k): "))
seed = int(input("Masukkan seed yang akan digunakan: "))
result_name = input("Masukkan nama file hasil watermarking yang diinginkan: ")
print("")

print("ENCODING...")
encoding(result_name, "input/" + original_image, k, seed)
compare_status = comparing("input/" + original_image, result_name + ".png")
print("STATUS: " + compare_status)

