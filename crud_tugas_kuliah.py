import csv
import os
from collections import deque

FILE_CSV = "tugas.csv"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        sekarang = self.head

        while sekarang.next:
            sekarang = sekarang.next

        sekarang.next = node_baru

    def tampilkan(self):
        sekarang = self.head

        while sekarang:
            yield sekarang.data
            sekarang = sekarang.next

    def hapus(self, id_tugas):
        sekarang = self.head
        sebelumnya = None

        while sekarang:

            if sekarang.data["id"] == id_tugas:

                if sebelumnya is None:
                    self.head = sekarang.next
                else:
                    sebelumnya.next = sekarang.next

                return True

            sebelumnya = sekarang
            sekarang = sekarang.next

        return False

data_tugas = {}
antrian_tugas = deque()
linked_list_tugas = LinkedList()

def buat_file_jika_belum_ada():

    if not os.path.exists(FILE_CSV):

        with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "id",
                "nama_tugas",
                "mata_kuliah",
                "deadline",
                "prioritas",
                "status"
            ])


def simpan_data():

    with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "id",
            "nama_tugas",
            "mata_kuliah",
            "deadline",
            "prioritas",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for id_tugas, data in data_tugas.items():

            writer.writerow({
                "id": id_tugas,
                "nama_tugas": data["nama_tugas"],
                "mata_kuliah": data["mata_kuliah"],
                "deadline": data["deadline"],
                "prioritas": data["prioritas"],
                "status": data["status"]
            })


def load_data():

    data_tugas.clear()
    antrian_tugas.clear()
    linked_list_tugas.head = None

    with open(FILE_CSV, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            id_tugas = row["id"]

            data_tugas[id_tugas] = {
                "nama_tugas": row["nama_tugas"],
                "mata_kuliah": row["mata_kuliah"],
                "deadline": row["deadline"],
                "prioritas": row["prioritas"],
                "status": row["status"]
            }

            antrian_tugas.append(id_tugas)

            linked_list_tugas.tambah({
                "id": id_tugas,
                "nama_tugas": row["nama_tugas"],
                "mata_kuliah": row["mata_kuliah"],
                "deadline": row["deadline"],
                "prioritas": row["prioritas"],
                "status": row["status"]
            })

def generate_id():

    if len(data_tugas) == 0:
        return "1"

    daftar_id = [int(i) for i in data_tugas.keys()]

    return str(max(daftar_id) + 1)

def tambah_tugas():

    print("\n=== TAMBAH TUGAS ===")

    id_tugas = generate_id()

    nama = input("Nama Tugas : ")
    mk = input("Mata Kuliah : ")
    deadline = input("Deadline (YYYY-MM-DD) : ")
    prioritas = input("Prioritas (Tinggi/Sedang/Rendah) : ")

    data_tugas[id_tugas] = {
        "nama_tugas": nama,
        "mata_kuliah": mk,
        "deadline": deadline,
        "prioritas": prioritas,
        "status": "Belum Selesai"
    }

    linked_list_tugas.tambah({
        "id": id_tugas,
        "nama_tugas": nama,
        "mata_kuliah": mk,
        "deadline": deadline,
        "prioritas": prioritas,
        "status": "Belum Selesai"
    })

    antrian_tugas.append(id_tugas)

    simpan_data()

    print("Tugas berhasil ditambahkan.")


def tampilkan_tugas():

    print("\n=== DAFTAR TUGAS ===")

    if linked_list_tugas.head is None:
        print("Belum ada data.")
        return

    for data in linked_list_tugas.tampilkan():

        print("-" * 50)
        print("ID        :", data["id"])
        print("Tugas     :", data["nama_tugas"])
        print("Matkul    :", data["mata_kuliah"])
        print("Deadline  :", data["deadline"])
        print("Prioritas :", data["prioritas"])
        print("Status    :", data["status"])


def update_tugas():

    print("\n=== UPDATE TUGAS ===")

    id_tugas = input("Masukkan ID tugas : ")

    if id_tugas not in data_tugas:
        print("ID tidak ditemukan.")
        return

    nama = input("Nama tugas baru : ")
    mk = input("Mata kuliah baru : ")
    deadline = input("Deadline baru : ")
    prioritas = input("Prioritas baru : ")
    status = input("Status baru : ")

    if nama:
        data_tugas[id_tugas]["nama_tugas"] = nama

    if mk:
        data_tugas[id_tugas]["mata_kuliah"] = mk

    if deadline:
        data_tugas[id_tugas]["deadline"] = deadline

    if prioritas:
        data_tugas[id_tugas]["prioritas"] = prioritas

    if status:
        data_tugas[id_tugas]["status"] = status

    simpan_data()
    load_data()

    print("Data berhasil diupdate.")


def hapus_tugas():

    print("\n=== HAPUS TUGAS ===")

    id_tugas = input("Masukkan ID tugas : ")

    if id_tugas not in data_tugas:
        print("ID tidak ditemukan.")
        return

    del data_tugas[id_tugas]

    linked_list_tugas.hapus(id_tugas)

    try:
        antrian_tugas.remove(id_tugas)
    except:
        pass

    simpan_data()

    print("Data berhasil dihapus.")

def cari_tugas():

    print("\n=== CARI TUGAS ===")

    keyword = input("Masukkan nama tugas : ").lower()

    ditemukan = False

    for data in linked_list_tugas.tampilkan():

        if keyword in data["nama_tugas"].lower():

            print("-" * 50)
            print("ID        :", data["id"])
            print("Tugas     :", data["nama_tugas"])
            print("Matkul    :", data["mata_kuliah"])
            print("Deadline  :", data["deadline"])
            print("Prioritas :", data["prioritas"])
            print("Status    :", data["status"])

            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")

def urutkan_deadline():

    print("\n=== SORTING DEADLINE ===")

    hasil_sort = sorted(
        linked_list_tugas.tampilkan(),
        key=lambda x: x["deadline"]
    )

    for data in hasil_sort:

        print("-" * 50)
        print("ID        :", data["id"])
        print("Tugas     :", data["nama_tugas"])
        print("Matkul    :", data["mata_kuliah"])
        print("Deadline  :", data["deadline"])
        print("Prioritas :", data["prioritas"])
        print("Status    :", data["status"])

def tampilkan_antrian():

    print("\n=== ANTRIAN TUGAS ===")

    if not antrian_tugas:
        print("Antrian kosong.")
        return

    nomor = 1

    for id_tugas in antrian_tugas:

        if id_tugas in data_tugas:

            print(
                f"{nomor}. {data_tugas[id_tugas]['nama_tugas']}"
            )

            nomor += 1

def tampilkan_linked_list():

    print("\n=== REPRESENTASI LINKED LIST ===")

    sekarang = linked_list_tugas.head

    while sekarang:

        print(
            f"[{sekarang.data['id']}] -> ",
            end=""
        )

        sekarang = sekarang.next

    print("None")

def menu():

    while True:

        print("\n")
        print("=" * 50)
        print(" SISTEM MANAJEMEN TUGAS KULIAH ")
        print("=" * 50)
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Update Tugas")
        print("4. Hapus Tugas")
        print("5. Cari Tugas")
        print("6. Urutkan Deadline")
        print("7. Lihat Antrian Tugas")
        print("8. Lihat Struktur Linked List")
        print("9. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tambah_tugas()
            
        elif pilihan == "2":
            tampilkan_tugas()

        elif pilihan == "3":
            update_tugas()

        elif pilihan == "4":
            hapus_tugas()

        elif pilihan == "5":
            cari_tugas()

        elif pilihan == "6":
            urutkan_deadline()

        elif pilihan == "7":
            tampilkan_antrian()
            
        elif pilihan == "8":
            tampilkan_linked_list()

        elif pilihan == "9":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


buat_file_jika_belum_ada()
load_data()
menu()