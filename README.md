# Sistem Manajemen Tugas Kuliah

## Deskripsi

Sistem Manajemen Tugas Kuliah adalah aplikasi berbasis Python yang digunakan untuk mengelola data tugas mahasiswa. Program ini mendukung operasi CRUD (Create, Read, Update, Delete), pencarian data (Searching), pengurutan data (Sorting), serta penyimpanan data menggunakan file CSV.

## Struktur Data yang Digunakan

### Linked List

Digunakan sebagai struktur utama untuk menyimpan dan menampilkan data tugas.

### Queue (Deque)

Digunakan untuk mengelola urutan tugas yang ditambahkan ke dalam sistem.

### Hash Map (Dictionary)

Digunakan untuk mempercepat akses data berdasarkan ID tugas.

## Fitur Program

* Tambah Tugas (Create)
* Lihat Semua Tugas (Read)
* Update Tugas (Update)
* Hapus Tugas (Delete)
* Cari Tugas berdasarkan nama
* Urutkan tugas berdasarkan deadline
* Lihat Antrian Tugas
* Lihat Representasi Linked List

## Database

Program menggunakan file CSV sebagai media penyimpanan data.

**Nama file database:** `tugas.csv`

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka terminal pada folder project.
3. Jalankan perintah berikut:

```bash
python crud_tugas_kuliah.py
```

atau

```bash
py crud_tugas_kuliah.py
```

## Struktur Folder

```text
UAS_Struktur_Data_Mohammad_Fazril_Ibrahim/
│
├── crud_tugas_kuliah.py
├── tugas.csv
├── flowchart_program_csv.png
└── README.md
```

## Author

**Nama:** Mohammad Fazril Ibrahim

**Mata Kuliah:** Struktur Data

**Universitas:** Universitas Buana Perjuangan Karawang
