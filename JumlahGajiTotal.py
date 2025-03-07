print("===KALKULATOR HITUNG JUMLAH GAJI TOTAL===")

nama = input("Masukkan Nama: ")  
nik = int(input("Masukkan NIK: "))
status = input("Masukkan Status Pegawai (Pegawai Tetap/Pegawai Honor): ")  
golongan = input("Masukkan Golongan (A/B/C): ") 

# Data gaji pokok dan bonus berdasarkan status dan golongan pegawai
gaji_tetap = 1000000 
bonus_tetap = {"A": 200000, "B": 400000, "C": 550000}  
gaji_honor = 750000  
bonus_honor = {"A": 150000, "B": 275000, "C": 480000} 

gaji_pokok = 0  # Inisialisasi gaji pokok
bonus = 0  # Inisialisasi bonus

if status.lower() == "pegawai tetap":  
    gaji_pokok = gaji_tetap  
    bonus = bonus_tetap.get(golongan.upper(), 0)  
elif status.lower() == "pegawai honor":  
    gaji_pokok = gaji_honor  
    bonus = bonus_honor.get(golongan.upper(), 0)  
    print("Status pegawai tidak valid!")  
    exit() 

# Menghitung total gaji
gaji_total = gaji_pokok + bonus  

print("\n===== Detail Gaji =====")
print(f"Nama      : {nama}")  
print(f"NIK       : {nik}") 
print(f"Status    : {status}")  
print(f"Golongan  : {golongan}") 
print(f"Gaji Pokok: Rp {gaji_pokok:,}")  
print(f"Bonus     : Rp {bonus:,}")  
print(f"Gaji Total: Rp {gaji_total:,}")  



