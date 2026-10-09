mendaftar = True
membayar = True

# Model logika
ikut_ujian = mendaftar and membayar

# Output hasil
if ikut_ujian:
    print("Boleh ikut ujian")
else:
    print("Tidak boleh ikut ujian")