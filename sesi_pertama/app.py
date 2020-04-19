# ===========================

# ***************************
# Workshop Python Series Programs 1
# Pemateri      : Hadi Hidayat Hammurabi
# Source Code   : Hadi Hidayat Hammurabi
# Source        : Praxis Academy dan Padekopan Asa Wedomartini
# ***************************

# ***************************
# Author        : Salim Suprayogi
# Sabtu, 11 April 2020
# Pukul 10.00-12.00 WIB
# ***************************

# ===========================

# Variabel dan Tipe Data
nama = "Praxis Academy"
print(nama)
tahun = 2020
print(tahun)

# ===========================

# Operasi Aritmatika
print(1+2)
print(4+8)
a = 10
b = 20
print(a + b)

# ===========================

# Kode Alur Program - Percabangan
nilai = 80
if nilai > 75:
    print("Selamat ! kamu lulus")
else:
    print("Semangat ! semoga lain kali berhasil")

# ===========================

# Kendali Alur Program - Perulangan
# for
for angka in range(10):
    print(angka)

# while
pintar = True
while (pintar):
    print("aku pintar")
    pintar = False

# ===========================

# Struktur Data
# Struktur Data - List
nilai = [80, 90, 75]
print(nilai[0])
print(nilai[1])
print(nilai[2])

nama = ["Praxis Academy", "Hadi Hidayat Hammurabi"]
for data in nama:
    print(data)

# Struktur Data - Tuple
nilai = (80, 90, 75)
for data in nilai:
    print(data)  # tampilkan semua data
# tuple tidak bisa di ubah nilainya

# Struktur Data - Dict
data = {
    "nama": "Hadi Hidayat Hammurabi",
    "nilai": "90"
}
print(data)
print(data["nama"])
print(data["nilai"])

# perulangan
for key, value in data.items():
    print(f"{key} - {value}")

# ===========================

# Fungsi


def sapa():
    print("halo")


def panggil(nama):
    print(f"selamat datang, {nama}")


# panggil fungsi
sapa()
panggil("Hadi Hidayat Hammurabi")
sapa()

# ===========================
