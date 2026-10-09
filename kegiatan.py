seminar = True
lomba = False

# Model logika
pilihan = seminar ^ lomba

# Output hasil
if pilihan:
    print("Pilihan valid")
else:
    print("Pilihan invalid")