from prettytable import PrettyTable

pinadmin = '12'

ps_tersedia = [
    {"jenis": "PS 2", "Harga sewa": "Rp. 4.000/jam", "jumlah": "2"},
    {"jenis": "PS 3", "Harga sewa": "Rp. 6.000/jam", "jumlah": "5"},
    {"jenis": "PS 4", "Harga sewa": "Rp. 8.000/jam", "jumlah": "6"},
    {"jenis": "PS 5", "Harga sewa": "Rp. 10.000/jam", "jumlah": "4"},
]

print("=========================================================")
print("========== Selamat Datang di High PlayStation ===========")
print("=========================================================")
print("============ Tempat Nyaman Dan Berkualitas ==============")
print("=========================================================")
print("================= Murah Dan Terpercaya ==================")
print("=========================================================")

def tabel_awal():
    tabellogin = PrettyTable()
    tabellogin.field_names = ["Opsi", "Masuk Sebagai"]
    tabellogin.add_row(["1", "Admin"])
    tabellogin.add_row(["2", "Pelanggan"])
    print(tabellogin)

def login():
    jawab = 'y'
    while jawab == 'y':
        tabel_awal()
        masuk = input("Masukkan pilihan anda: ")
        if masuk == '1':
            menu_admin()
        elif masuk == '2':
            menu_user()
        else:
            jawab = input("Pilihan salah, apakah anda ingin mengulang? (y/t): ")

def menu_admin():
    while True:
        pin = input("Masukan Pin Admin: ")
        if pin == pinadmin:
            print("===========================")
            print("===== Haii Admin Kece =====")
            print("===========================")
            print("Menu:                      ")
            print("1. Lihat list PS           ")
            print("2. Tambah list PS          ")
            print("3. Hapus list PS           ")
            print("4. Keluar                  ")
            print("===========================")
            pilih = input("Pilih opsi: ")
            
            if pilih == "1":
                list_ps()
            elif pilih == "2":
                menambah_ps()
            elif pilih == "3":
                menghapus_ps()
                break
            elif pilih == "4":
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak sesuai menu.")
        else:
            print("Pin salah, coba lagi.")

def list_ps():
    judul1 = "List PS High PlayStation"
    table = PrettyTable()
    table.title = judul1
    table.field_names = ["Jenis PS", "Harga Sewa", "Jumlah PS"]
    
    for jenis in ps_tersedia:
        table.add_row([jenis["jenis"], jenis["Harga sewa"], jenis["jumlah"]])
    print(table)

def menambah_ps():
    jenisps = input("Masukkan Jenis PS baru: ")
    harga_sewa = input("Masukkan Harga Sewa: ")
    jumlahps = input("Masukkan Jumlah tambahan PS: ")
    ps_tersedia.append({"jenis": jenisps, "Harga sewa": harga_sewa, "jumlah": jumlahps})
    print(f"Item {jenisps} berhasil ditambahkan dengan Jumlah {jumlahps}.")

def menghapus_ps():
    hapus_ps = input("Masukkan jenis PS yang ingin dihapus: ")
    for item in ps_tersedia:
        if item["jenis"] == hapus_ps:
            ps_tersedia.remove(item)
            print(f"Item {hapus_ps} berhasil dihapus.")
            return
    print(f"Item {hapus_ps} tidak ditemukan.")

def menu_user():
    print("==================================")
    print("====== Haloo Pelanggan Kece ======")
    print("==================================")
    print("Menu:                             ")
    print("1. Sewa PS                        ")
    print("2. Lihat List PS                  ")
    print("==================================")
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        sewa_ps()
    elif pilihan == '2':
        list_ps()
        us = input("kembali ke menu user (y/n): ")
        if us == 'y':
            menu_user()
        else:
            login()
    else:
        print("Menu tidak tersedia")
        login()

def sewa_ps():
    list_ps()
    jenis_ps = input("Masukkan jenis PS yang ingin anda sewa: ")
    if jenis_ps in ['PS 2', 'PS 3', 'PS 4', 'PS 5']:
        waktu = int(input("Masukan Waktu (jam): "))
        harga_perjam = 0
        if jenis_ps == 'PS 2':
            harga_perjam = 4000
        elif jenis_ps == 'PS 3':
            harga_perjam = 6000
        elif jenis_ps == 'PS 4':
            harga_perjam = 8000
        elif jenis_ps == 'PS 5':
            harga_perjam = 10000
        total = harga_perjam * waktu
        print(f"Jumlah yang harus anda bayar adalah Rp. {total}")
        print("=========================================================")
        print("===== Terimakasih Telah Menyewa DI High PlayStation =====")
        print("=========================================================")
        print("=================== Have A Nice Game ====================")
        print("=========================================================")
        print("==================== Program Selesai ====================")
        print("=========================================================")
        exit()
    else:
        print(f"PS {jenis_ps} tidak ditemukan.")

login()