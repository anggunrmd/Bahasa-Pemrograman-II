print("===KALKULATOR HITUNG JUMLAH GAJI TOTAL===")

# Daftar status dan golongan
status_list = ["Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

# Input data pegawai
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

# Validasi input menggunakan nested loop
for s in status_list:
    for g in golongan_list:
        if status == s and golongan == g:
            if s == "Tetap":
                gaji = 1_000_000
                if g == "A":
                    bonus = 200_000
                elif g == "B":
                    bonus = 400_000
                else:  # Golongan C
                    bonus = 550_000
            else:  # Pegawai Honor
                gaji = 750_000
                if g == "A":
                    bonus = 150_000
                elif g == "B":
                    bonus = 275_000
                else:  # Golongan C
                    bonus = 480_000
            
            gaji_total = gaji + bonus

            # Output hasil
            print("\n--- Data Gaji Pegawai ---")
            print(f"Nama      : {nama}")
            print(f"NIK       : {nik}")
            print(f"Status    : {status}")
            print(f"Golongan  : {golongan}")
            print(f"Gaji Pokok: Rp{gaji:,}")
            print(f"Bonus     : Rp{bonus:,}")
            print(f"Gaji Total: Rp{gaji_total:,}")

# Jika tidak ada kecocokan dalam loop, tampilkan pesan error
if status not in status_list or golongan not in golongan_list:
    print("Input status atau golongan tidak valid!")


