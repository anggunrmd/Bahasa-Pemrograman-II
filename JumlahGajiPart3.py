print("===KALKULATOR HITUNG JUMLAH GAJI TOTAL===")

# Daftar status dan golongan
status_list = ["Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

# Data gaji dan bonus berdasarkan status dan golongan
gaji_dict = {
    "Tetap": {"A": (1_000_000, 200_000), "B": (1_000_000, 400_000), "C": (1_000_000, 550_000)},
    "Honor": {"A": (750_000, 150_000), "B": (750_000, 275_000), "C": (750_000, 480_000)}
}

# Input data pegawai
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

for s in status_list:
    for g in golongan_list:
        if status == s and golongan == g:
            gaji, bonus = gaji_dict[s][g]
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