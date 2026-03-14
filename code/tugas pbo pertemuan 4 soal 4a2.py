print("Masukkan nama tamu. Ketik 'q' untuk keluar.")

with open("guest_book.txt", "a") as file:
    while True:
        name = input("Nama: ")

        if name == 'q':
            break

        file.write(name + "\n")
        print("Nama ditambahkan.")