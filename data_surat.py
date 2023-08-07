def tambah_surat ():
    nama = input("nama penerima :")
    alamat = input("alamat penerima :")
    tanggal = input("tanggal surat dd/mm/yyyy :")
    jenis = input("jenis surat :")

    with open ("data_surat.txt", "a" ) as file:
        file.write(nama + "|" + alamat + "|" + tanggal + "|" + jenis + "\n")
    print("data surat berhasil ditambahkan")

def lihat_surat():
    try:
        with open ("data_surat.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                print("Nama:" + data[0])
                print("Alamat:" + data[1])
                print("tanggal:" + data[2])
                print("Jenis:" + data[3])
                print("----------------------")
    except FileNotFoundError:
        print("tidak ada data surat yang tersedia")

def main_menu():
    while True: 
        print("==aplikasi penyimpanan data surat==")
        print("1. Tambah data surat")
        print("2. Lihat data surat")
        print("3. Keluar")

        pilihan = input("Masukan pilihan 1/2/3 =")

        if pilihan == '1':
            tambah_surat()
        elif pilihan == '2':
            lihat_surat()
        elif pilihan == '3':
            print("Anda telah keluar dari aplikasi data surat")
            break
        else :
            print("Pilihan yang anda masukan tidak valid. silahan coba lagi.")
