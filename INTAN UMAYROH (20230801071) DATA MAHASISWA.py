# Fungsi untuk menginput data mahasiswa
def input_mahasiswa():
    mahasiswa = []
    while True:
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        prodi = input("Masukkan prodi mahasiswa: ")
        
        while True:
            try:
                nilai = float(input("Masukkan nilai mahasiswa: "))
                break
            except ValueError:
                print("Nilai harus berupa angka.")
        
        mahasiswa.append({
            "nama": nama,
            "nim": nim,
            "prodi": prodi,
            "nilai": nilai
        })
        
        jawab = input("Apakah Anda ingin memasukkan data mahasiswa lain? (y/n): ")
        if jawab.lower() != 'y':
            break
    
    return mahasiswa

# Fungsi untuk menampilkan data mahasiswa
def show_mahasiswa(mahasiswa):
    print("\n" + "=" * 50)
    print(" " * 20 + "Data Mahasiswa:")
    print("=" * 50)
    for i, mhs in enumerate(mahasiswa, 1):
        print(f"{i}. Nama: {mhs['nama']}, NIM: {mhs['nim']}, Prodi: {mhs['prodi']}, Nilai: {mhs['nilai']:.2f}")
    print("=" * 50)

# Fungsi untuk menghitung dan menampilkan rata-rata nilai mahasiswa
def hitung_rata_rata(mahasiswa):
    total = sum(mhs['nilai'] for mhs in mahasiswa)
    rata_rata = total / len(mahasiswa)
    print("\n" + "=" * 50)
    print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")
    print("=" * 50)

# Fungsi untuk mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah
def cari_mahasiswa(mahasiswa):
    mahasiswa_tertinggi = max(mahasiswa, key=lambda x: x['nilai'])
    mahasiswa_terendah = min(mahasiswa, key=lambda x: x['nilai'])
    print("\n" + "=" * 50)
    print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi['nama']}, Nilai: {mahasiswa_tertinggi['nilai']:.2f}")
    print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terendah['nama']}, Nilai: {mahasiswa_terendah['nilai']:.2f}")
    print("=" * 50)

# Jalankan program
mahasiswa = input_mahasiswa()
show_mahasiswa(mahasiswa)
hitung_rata_rata(mahasiswa)
cari_mahasiswa(mahasiswa)
