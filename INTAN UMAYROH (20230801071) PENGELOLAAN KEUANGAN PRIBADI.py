# Fungsi untuk menginput transaksi
def input_transaksi():
    transaksi = []
    while True:
        print("\n" + "=" * 60)
        jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
        if jenis not in ["pemasukan", "pengeluaran"]:
            print("Jenis transaksi harus 'pemasukan' atau 'pengeluaran'.")
            continue
        
        deskripsi = input("Masukkan deskripsi transaksi: ")
        
        while True:
            try:
                jumlah = float(input("Masukkan jumlah transaksi: "))
                break
            except ValueError:
                print("Jumlah harus berupa angka.")
        
        transaksi.append({"jenis": jenis, "deskripsi": deskripsi, "jumlah": jumlah})
        
        if input("Apakah Anda ingin memasukkan transaksi lain? (y/n): ").lower() != 'y':
            break
    return transaksi

# Fungsi untuk menampilkan semua transaksi
def show_transaksi(transaksi):
    print("\nDaftar Transaksi:\n" + "=" * 60)
    for i, tr in enumerate(transaksi, 1):
        print(f"{i}. Jenis: {tr['jenis'].capitalize()}, Deskripsi: {tr['deskripsi']}, Jumlah: {tr['jumlah']}")
    print("=" * 60)

# Fungsi untuk menghitung dan menampilkan total
def total(transaksi, jenis):
    total = sum(tr['jumlah'] for tr in transaksi if tr['jenis'] == jenis)
    print(f"\nTotal {jenis.capitalize()}: {total:.2f}\n" + "=" * 60)

# Fungsi untuk menghitung dan menampilkan saldo akhir
def saldo_akhir(transaksi):
    total_pemasukan = sum(tr['jumlah'] for tr in transaksi if tr['jenis'] == 'pemasukan')
    total_pengeluaran = sum(tr['jumlah'] for tr in transaksi if tr['jenis'] == 'pengeluaran')
    saldo = total_pemasukan - total_pengeluaran
    print(f"\nSaldo Akhir: {saldo:.2f}\n" + "=" * 60)

# Fungsi utama untuk menjalankan program
def main():
    transaksi = input_transaksi()
    menu = {
        '1': show_transaksi,
        '2': lambda t: total(t, 'pemasukan'),
        '3': lambda t: total(t, 'pengeluaran'),
        '4': saldo_akhir
    }
    
    while True:
        print("\n" + "=" * 60)
        print(" " * 25 + "Daftar Menu")
        print("=" * 60)
        print("1. Tampilkan semua transaksi")
        print("2. Hitung dan tampilkan total pemasukan")
        print("3. Hitung dan tampilkan total pengeluaran")
        print("4. Hitung dan tampilkan saldo akhir")
        print("5. Keluar")
        print("=" * 60)
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan in menu:
            menu[pilihan](transaksi)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
