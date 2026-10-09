kartu_mahasiswa = True
kartu_anggota = False

# Model logika
akses = kartu_mahasiswa or kartu_anggota

# Output hasil
if akses:
    print("Boleh memasuki perpustakaan")
else:
    print("tidak Boleh memasuki perpustakaan")