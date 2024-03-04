import os
os.system('cls')
from prettytable import PrettyTable

class ProdukRoti:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Node:
    def __init__(self, produk_roti):
        self.produk_roti = produk_roti
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_produk_roti(self, produk_roti, pos=None):
        new_node = Node(produk_roti)

        if pos == "awal":
            new_node.next = self.head
            self.head = new_node
        elif pos == "akhir":
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menambah di antara.")
                return

            nama_sebelum = input("Masukkan nama produk roti sebelum posisi baru: ")
            current = self.head
            while current.next and current.next.produk_roti.nama != nama_sebelum:
                current = current.next

            if current.next:
                new_node.next = current.next
                current.next = new_node
            else:
                print(f"Produk Roti dengan nama {nama_sebelum} tidak ditemukan.")
        else:
            print("Posisi tidak valid.")

    def hapus_produk_roti(self, pos=None, nama=None):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dapat dihapus.")
            return False

        if pos == "awal":
            self.head = self.head.next
        elif pos == "akhir":
            current = self.head
            if not current.next:
                self.head = None
                return True
            while current.next.next:
                current = current.next
            current.next = None
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menghapus di antara.")
                return False

            if not nama:
                print("Nama produk roti tidak boleh kosong.")
                return False

            nama_sebelum = input("Masukkan nama produk roti sebelum posisi yang ingin dihapus: ")
            current = self.head

            # Menangani kasus penghapusan di awal
            if current.produk_roti.nama == nama_sebelum:
                self.head = self.head.next
                return True

            while current.next and current.next.produk_roti.nama != nama_sebelum:
                current = current.next

            if current.next:
                current.next = current.next.next
                return True
            else:
                print(f"Produk Roti dengan nama {nama_sebelum} tidak ditemukan.")
                return False
        else:
            print("Posisi tidak valid.")
            return False

    def tampilkan_produk_roti(self):
        table = PrettyTable(["Nama", "Harga", "Stok"])
        current = self.head
        while current:
            table.add_row([current.produk_roti.nama, current.produk_roti.harga, current.produk_roti.stok])
            current = current.next
        return str(table)

    def ubah_produk_roti(self, nama, harga_baru, stok_baru):
        current = self.head
        while current:
            if current.produk_roti.nama == nama:
                current.produk_roti.harga = harga_baru
                current.produk_roti.stok = stok_baru
                return True
            current = current.next
        return False

# Contoh penggunaan
produk_roti_list = LinkedList()

while True:
    print("Menu:")
    print("1. Tambah Produk Roti")
    print("2. Tampilkan Produk Roti")
    print("3. Ubah Produk Roti")
    print("4. Hapus Produk Roti")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama = input("Masukkan nama produk roti: ")
        harga = float(input("Masukkan harga produk roti: "))
        stok = int(input("Masukkan stok produk roti: "))
        # Tampilkan opsi untuk menentukan posisi
        print("Pilih posisi tambahan:")
        print("1. Di Awal")
        print("2. Di Akhir")
        print("3. Di Antara")
        posisi_pilihan = input("Pilih posisi (1-3): ")

        if posisi_pilihan == '1':
            produk_roti_list.tambah_produk_roti(ProdukRoti(nama, harga, stok), pos="awal")
            print("Produk Roti berhasil ditambahkan di awal.")
        elif posisi_pilihan == '2':
            produk_roti_list.tambah_produk_roti(ProdukRoti(nama, harga, stok), pos="akhir")
            print("Produk Roti berhasil ditambahkan di akhir.")
        elif posisi_pilihan == '3':
            produk_roti_list.tambah_produk_roti(ProdukRoti(nama, harga, stok), pos="antara")
            print("Produk Roti berhasil ditambahkan di antara.")
        else:
            print("Pilihan posisi tidak valid.")
    elif pilihan == '2':
        print(produk_roti_list.tampilkan_produk_roti())
    elif pilihan == '3':
        nama = input("Masukkan nama produk roti yang ingin diubah: ")
        harga_baru = float(input("Masukkan harga baru produk roti: "))
        stok_baru = int(input("Masukkan stok baru produk roti: "))
        if produk_roti_list.ubah_produk_roti(nama, harga_baru, stok_baru):
            print("Produk Roti berhasil diubah.")
        else:
            print(f"Produk Roti dengan nama {nama} tidak ditemukan.")
    elif pilihan == '4':
        # Tampilkan opsi untuk menentukan posisi penghapusan
        print("Pilih posisi penghapusan:")
        print("1. Di Awal")
        print("2. Di Akhir")
        print("3. Di Antara")
        posisi_pilihan_hapus = input("Pilih posisi (1-3): ")
        
        if posisi_pilihan_hapus == '1':
            if produk_roti_list.hapus_produk_roti(pos="awal"):
                print("Produk Roti di awal berhasil dihapus.")
            else:
                print("Produk Roti di awal tidak ditemukan atau tidak dapat dihapus.")
        elif posisi_pilihan_hapus == '2':
            if produk_roti_list.hapus_produk_roti(pos="akhir"):
                print("Produk Roti di akhir berhasil dihapus.")
            else:
                print("Produk Roti di akhir tidak ditemukan atau tidak dapat dihapus.")
        elif posisi_pilihan_hapus == '3':
            nama_hapus = input("Masukkan nama produk roti yang ingin dihapus: ")
            if produk_roti_list.hapus_produk_roti(pos="antara", nama=nama_hapus):
                print(f"Produk Roti dengan nama {nama_hapus} berhasil dihapus.")
            else:
                print(f"Produk Roti dengan nama {nama_hapus} tidak ditemukan atau tidak dapat dihapus.")
        else:
            print("Pilihan posisi tidak valid.")
    elif pilihan == '5':
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")
