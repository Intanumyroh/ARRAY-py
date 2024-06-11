# Fungsi untuk menginput data barang
def input_barang():
    barang = []
    while True:
        nama = input("Masukkan nama barang: ")
        kode = input("Masukkan kode barang: ")
        
        while True:
            try:
                jumlah = int(input("Masukkan jumlah barang: "))
                break
            except ValueError:
                print("Jumlah harus berupa angka.")
        
        barang.append({
            "nama": nama,
            "kode": kode,
            "jumlah": jumlah
        })
        
        jawab = input("Apakah Anda ingin memasukkan data barang lain? (y/n): ").lower()
        if jawab != 'y':
            break
    return barang

# Fungsi untuk menampilkan semua barang
def show_barang(barang):
    print("\nDaftar Barang:")
    print("=" * 60)
    for i, item in enumerate(barang, 1):
        print(f"{i}. Nama: {item['nama']}, Kode: {item['kode']}, Jumlah: {item['jumlah']}")
    print("=" * 60)

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang(barang):
    kode = input("\nMasukkan kode barang yang ingin dicari: ")
    for item in barang:
        if item['kode'] == kode:
            print(f"Nama: {item['nama']}, Jumlah: {item['jumlah']}")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menghapus barang berdasarkan kode
def hapus_barang(barang):
    kode = input("\nMasukkan kode barang yang ingin dihapus: ")
    for i, item in enumerate(barang):
        if item['kode'] == kode:
            barang.pop(i)
            print("Barang berhasil dihapus.")
            return
    print("Barang tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    barang = input_barang()
    
    while True:
        print("\n" + "=" * 60)
        print(" " * 25 + "Daftar Menu")
        print("=" * 60)
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Hapus barang berdasarkan kode")
        print("4. Keluar")
        print("=" * 60)
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            show_barang(barang)
        elif pilihan == '2':
            cari_barang(barang)
        elif pilihan == '3':
            hapus_barang(barang)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
