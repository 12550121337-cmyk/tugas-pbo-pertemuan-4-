while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        hasil = angka1 + angka2
        print("Hasil:", hasil)

    except ValueError:
        print("Input harus angka, coba lagi!")

    lagi = input("Hitung lagi? (y/n): ")
    if lagi.lower() != 'y':
        break