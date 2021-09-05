print("https://www.youtube.com/watch?v=6EhlIBzTpIw")

#print("Tanpa perulangan terlebih dahulu")
#x = 0
#x = x + int(input("Masukkan nilai: "))
#x = x + int(input("Masukkan nilai lagi: "))
#x = x + int(input("Masukkan nilai lagi: "))
#x = x + int(input("Masukkan nilai lagi: "))
#x = x + int(input("Masukkan nilai lagi: "))
#x = x / 5
#print("Rata-rata nilainya adalah: ", x)

#print("")
#input("Tekan enter untuk melanjutkan")


print("Perulangan (for) simple")
print("")
total = 0
for absen in range(1, 6):
	print("Masukkan nilai absen ke-",absen)
	total = total + int(input("Nilai: "))
total = total / 5
print("Rata-rata nilai: ", total)
print("SELESAI")

print("")
input("Tekan enter utuk melanjutkan")
print("")

print("Perulangan (while) simple")
total = 0
hitung = 1
while(hitung < 6):
	print("Input nilai ke: ", hitung)
	total = total + int(input("nilai: "))
	hitung = hitung + 1
total = total / 5
print("Nilai rata-rata nya adalah: ", total)
