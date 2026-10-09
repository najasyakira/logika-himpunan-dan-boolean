ikut_pelatihan = True
selesai_tugas = False

# Model logika
sertifikat = ikut_pelatihan and selesai_tugas

# Output hasil
if sertifikat:
    print("partisipan mendapat sertifikat")
else:
    print("partisipan tidak mendapat sertifikat")