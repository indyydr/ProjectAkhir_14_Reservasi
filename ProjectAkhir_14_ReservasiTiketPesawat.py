penerbangan = []
reservasi = []

admin_username = "admin"
admin_password = "admin678"

def tambah_penerbangan_manual():
    penerbangan.append({'nomor_penerbangan': '12324', 'tujuan': 'Jakarta', 'waktu_keberangkatan': '2024-12-09 11:20', 'jumlah_kursi': 1, 'harga_tiket': 785000.0})
    penerbangan.append({'nomor_penerbangan': '12325', 'tujuan': 'Bali', 'waktu_keberangkatan': '2024-12-10 12:00', 'jumlah_kursi': 2, 'harga_tiket': 950000.0})
    penerbangan.append({'nomor_penerbangan': '12326', 'tujuan': 'Surabaya', 'waktu_keberangkatan': '2024-12-11 13:30', 'jumlah_kursi': 3, 'harga_tiket': 650000.0})
    penerbangan.append({'nomor_penerbangan': '12327', 'tujuan': 'Yogyakarta', 'waktu_keberangkatan': '2024-12-12 14:45', 'jumlah_kursi': 2, 'harga_tiket': 700000.0})
    penerbangan.append({'nomor_penerbangan': '12328', 'tujuan': 'Medan', 'waktu_keberangkatan': '2024-12-13 15:15', 'jumlah_kursi': 1, 'harga_tiket': 800000.0})
    penerbangan.append({'nomor_penerbangan': '12329', 'tujuan': 'Makassar', 'waktu_keberangkatan': '2024-12-14 16:00', 'jumlah_kursi': 3, 'harga_tiket': 900000.0})

def login_admin():
    print("\nMohon Verifikasi Terlebih Dahulu.")
    for i in range(3):
        username = input("Username: ")
        password = input("Password: ")
        if username == admin_username and password == admin_password:
            return True
        print(f"Login gagal. Percobaan {i + 1} dari 3.")
    return False

def validasi_nomor_penerbangan():
    while True:
        nomor_penerbangan = input("Nomor Penerbangan: ")
        if nomor_penerbangan == "":
            print("Nomor penerbangan tidak boleh kosong. Coba lagi.")
        elif not nomor_penerbangan.isdigit():  
            print("Nomor penerbangan hanya boleh berupa angka. Coba lagi.")
        else:
            return nomor_penerbangan

def validasi_input_nomor_penerbangan(pesan):
    while True:
        nomor_penerbangan_input = input(pesan)
        
        if nomor_penerbangan_input == "":
            return None
        
        if nomor_penerbangan_input.isdigit():
            nomor_penerbangan = int(nomor_penerbangan_input) - 1
            
            if 0 <= nomor_penerbangan < len(penerbangan):
                return nomor_penerbangan
            else:
                print("Nomor penerbangan tidak valid. Silakan coba lagi.")
        else:
            print("Masukkan nomor penerbangan yang valid atau tekan Enter untuk kembali.")

def validasi_tujuan():
    while True:
        tujuan = input("Tujuan: ")
        if tujuan == "":
            print("Tujuan tidak boleh kosong. Coba lagi.")
        elif tujuan.isdigit(): 
            print("Tujuan hanya boleh berupa huruf. Coba lagi.")
        else:
            return tujuan

def validasi_waktu_keberangkatan():
    while True:
        waktu_keberangkatan = input("Tanggal dan Waktu Keberangkatan (YYYY-MM-DD HH:MM): ")
        if len(waktu_keberangkatan) == 16:
            if (waktu_keberangkatan[4] == '-' and 
                waktu_keberangkatan[7] == '-' and 
                waktu_keberangkatan[10] == ' ' and 
                waktu_keberangkatan[13] == ':'):
                
                tanggal_oke = True
                for i in range(4):  # Tahun (YYYY)
                    if waktu_keberangkatan[i] < '0' or waktu_keberangkatan[i] > '9':
                        tanggal_oke = False
                        break
                for i in range(5, 7):  # Bulan (MM)
                    if waktu_keberangkatan[i] < '0' or waktu_keberangkatan[i] > '9':
                        tanggal_oke = False
                        break
                for i in range(8, 10):  # Hari (DD)
                    if waktu_keberangkatan[i] < '0' or waktu_keberangkatan[i] > '9':
                        tanggal_oke = False
                        break
                for i in range(11, 13):  # Jam (HH)
                    if waktu_keberangkatan[i] < '0' or waktu_keberangkatan[i] > '9':
                        tanggal_oke = False
                        break
                for i in range(14, 16):  # Menit (MM)
                    if waktu_keberangkatan[i] < '0' or waktu_keberangkatan[i] > '9':
                        tanggal_oke = False
                        break
                if tanggal_oke:
                    return waktu_keberangkatan
                else:
                    print("Format waktu salah. Harap masukkan angka yang valid di tanggal dan waktu.")
            else:
                print("Format waktu salah. Harap masukkan dalam format YYYY-MM-DD HH:MM.")
        else:
            print("Format waktu salah. Harap masukkan dalam format YYYY-MM-DD HH:MM.")

def validasi_jumlah_kursi():
    while True:
        jumlah_kursi = input("Jumlah Kursi: ")
        if jumlah_kursi == "":
            print("Jumlah kursi tidak boleh kosong. Coba lagi.")
        elif not jumlah_kursi.isdigit() or int(jumlah_kursi) <= 0:
            print("Jumlah kursi harus berupa angka dan lebih besar dari 0. Coba lagi.")
        else:
            return int(jumlah_kursi)

def validasi_harga_tiket():
    while True:
        harga_tiket = input("Harga Tiket: ")    
        if harga_tiket == "":
            print("Harga tiket tidak boleh kosong. Coba lagi.")
        elif harga_tiket.replace('.', '', 1).isdigit():  
            harga = float(harga_tiket)
            if harga > 0:
                return harga
            else:
                print("Harga tiket harus lebih besar dari 0. Coba lagi.")
        else:
            print("Harga tiket harus berupa angka. Coba lagi.")

def validasi_nama_penumpang():
    while True:
        nama_penumpang = input("Masukkan nama penumpang: ").strip()
        if nama_penumpang:  
            return nama_penumpang
        else:
            print("Nama penumpang tidak boleh kosong. Silakan masukkan nama yang valid.")

def validasi_umur():
    while True:
        umur_input = input("Umur Penumpang: ")
        if umur_input.isdigit():
            umur = int(umur_input)
            if 0 <= umur <= 120:
                return umur
            else:
                print("Umur harus antara 0 dan 120.")
        else:
            print("Silakan masukkan angka yang valid untuk umur.")

def validasi_nomor_identitas():
    while True:
        nomor_identitas = input("Nomor Identitas (KTP/Paspor): ")
        if nomor_identitas.isdigit() and len(nomor_identitas) == 10:  
            return nomor_identitas
        else:
            print("Nomor identitas harus terdiri dari 10 digit dan hanya mengandung angka.")

def tambah_penerbangan():
    nomor_penerbangan = validasi_nomor_penerbangan()
    tujuan = validasi_tujuan()
    waktu_keberangkatan = validasi_waktu_keberangkatan()
    jumlah_kursi = validasi_jumlah_kursi()
    harga_tiket = validasi_harga_tiket()
    
    penerbangan_baru = {
        'nomor_penerbangan': nomor_penerbangan,
        'tujuan': tujuan,
        'waktu_keberangkatan': waktu_keberangkatan,
        'jumlah_kursi': jumlah_kursi,
        'harga_tiket': harga_tiket
    }
    penerbangan.append(penerbangan_baru)
    print("Penerbangan berhasil ditambahkan.")

def lihat_penerbangan():
    if not penerbangan:
        print("Tidak ada penerbangan yang tersedia.")
        return
    print("\nDaftar Penerbangan:")
    for i in range(len(penerbangan)):
        p = penerbangan[i]
        print(f"{i + 1}. {p['nomor_penerbangan']} - {p['tujuan']} - {p['waktu_keberangkatan']} - {p['jumlah_kursi']} kursi tersedia - Rp {p['harga_tiket']}")

def perbarui_penerbangan():
    lihat_penerbangan()
    nomor_penerbangan = validasi_input_nomor_penerbangan("Pilih nomor penerbangan untuk diperbarui: ")
    
    if nomor_penerbangan is None:
        print("Kembali ke Menu Admin.")
        return  
    
    p = penerbangan[nomor_penerbangan]
    while True:
        print("\nPilih bagian yang ingin diperbarui:")
        print("1. Tujuan")
        print("2. Waktu Keberangkatan")
        print("3. Jumlah Kursi yang Tersedia")
        print("4. Harga Tiket")
        print("5. Kembali ke Menu Admin")

        pilihan_update = input("Pilih opsi untuk diperbarui (1-5): ")

        if pilihan_update == '1':
            p['tujuan'] = validasi_tujuan()
            print("Tujuan berhasil diperbarui.")
            
        elif pilihan_update == '2':
            p['waktu_keberangkatan'] = validasi_waktu_keberangkatan()
            print("Waktu keberangkatan berhasil diperbarui.")
            
        elif pilihan_update == '3':
            p['jumlah_kursi'] = validasi_jumlah_kursi()
            print("Jumlah kursi berhasil diperbarui.")
            
        elif pilihan_update == '4':
            p['harga_tiket'] = validasi_harga_tiket()
            print("Harga tiket berhasil diperbarui.")
            
        elif pilihan_update == '5':
            print("Kembali ke Menu Admin.")
            return
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def hapus_penerbangan():
    lihat_penerbangan()
    nomor_penerbangan = validasi_input_nomor_penerbangan("Pilih nomor penerbangan untuk dihapus: ")
    if nomor_penerbangan is None:
        print("Kembali ke Menu Admin.")
        return  
    penerbangan.pop(nomor_penerbangan)
    print("Penerbangan berhasil dihapus.")

def buat_reservasi():
    lihat_penerbangan()
    nomor_penerbangan = validasi_input_nomor_penerbangan("Pilih nomor penerbangan untuk reservasi (atau tekan Enter untuk kembali): ")
    
    if nomor_penerbangan is None:
        print("Kembali ke Menu Pemesan.")
        return  
    
    p = penerbangan[nomor_penerbangan]
    if p['jumlah_kursi'] > 0:
        jumlah_tiket = validasi_jumlah_kursi()  
        if jumlah_tiket <= p['jumlah_kursi']:
            nama_penumpang = validasi_nama_penumpang()
            umur_penumpang = validasi_umur()  
            nomor_identitas = validasi_nomor_identitas()  
            reservasi_baru = {
                'penerbangan': p,
                'nama_penumpang': nama_penumpang,
                'umur_penumpang': umur_penumpang,
                'nomor_identitas': nomor_identitas,
                'jumlah_tiket': jumlah_tiket
            }
            reservasi.append(reservasi_baru)
            p['jumlah_kursi'] -= jumlah_tiket
            total_harga = p['harga_tiket'] * jumlah_tiket
            print(f"Reservasi berhasil untuk {jumlah_tiket} tiket. Total harga: Rp {total_harga}")
        else:
            print("Maaf, jumlah tiket yang diminta melebihi kursi yang tersedia.")
    else:
        print("Tiket belum tersedia, mohon pilih tiket penerbangan lain yang tersedia.")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Penerbangan")
        print("2. Perbarui Penerbangan")
        print("3. Hapus Penerbangan")
        print("4. Lihat Penerbangan")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            tambah_penerbangan()
        elif pilihan == '2':
            perbarui_penerbangan()
        elif pilihan == '3':
            hapus_penerbangan()
        elif pilihan == '4':
            lihat_penerbangan()
        elif pilihan == '5':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_pemesan():
    while True:
        print("\n=== Menu Pemesan ===")
        print("1. Buat Reservasi")
        print("2. Lihat Penerbangan")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == '1':
            buat_reservasi()
        elif pilihan == '2':
            lihat_penerbangan()
        elif pilihan == '3':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Login sebagai Admin")
        print("2. Menu Pemesan")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == '1':
            if login_admin():
                menu_admin()
            else:
                print("Akses ditolak. Silakan coba lagi.")
        elif pilihan == '2':
            menu_pemesan()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem reservasi penerbangan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

tambah_penerbangan_manual()
menu_utama()