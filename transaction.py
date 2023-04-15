from dataclasses import dataclass
from tabulate import tabulate


keranjang = {} # Inisialisasi dictionary kosong, untuk menampung barang belanjaan

@dataclass
class Transaction:
    """
    Kelas yang berguna untuk melakukan transaksi dengan berbagai
    macam metode yang dapat dijalankan seperti tambah barang, hapus, ubah
    barang dan lain-lain.
    """

    @staticmethod
    def add_item():
        """
        Method untuk menambahkan barang belanjaan,
        jika user tidak mengetik n maka program akan berjalan terus,
        atau user akan terus menginputkan barang belanjaan.
        Sebalikanya, jika 'n' maka program akan berhenti.
        """
        while True:
            barang = input("Masukkan barang belanjaan:\n")
            harga = int(input("Masukkan harga barang:\n"))
            jumlah = int(input("Masukkan jumlah barang:\n"))
            keranjang[barang] = [jumlah, harga] # Dictionary of lists

            selesai = input("Apakah anda ingin menambahkan barang lagi? (y/n)\n")
            if selesai.lower() == "n":
                break
        print(" ")


    @staticmethod
    def update_item():
        """
        Method untuk update item berdasarkan nama item. Nantinya akan
        menginput nama barang untuk dicari, jika barang tidak ditemukan 
        maka terdapat pilihan untuk update harga dann jumlah barang.
        """
        userUpdateInput = input("Masukkan barang apa yang ingin diupdate: ")
        if userUpdateInput not in keranjang:
            print("Barang tidak ditemukan dalam daftar belanjaan.")
            return
        print(f"Nama barang\t: {userUpdateInput}")
        print(f"Jumlah barang\t: {keranjang[userUpdateInput][0]}")
        print(f"Harga barang\t: {keranjang[userUpdateInput][1]}")
        print()

        while True:
            try:
                updateJumlah = int(input("Masukkan jumlah baru: "))
                updateHarga = int(input("Masukkan harga baru: "))
                if updateJumlah < 0 or updateHarga < 0:
                    print("Jumlah dan harga harus positif.")
                    continue
                break
            except ValueError:
                print("Jumlah dan harga harus berupa angka.")

        keranjang[userUpdateInput] = [updateJumlah, updateHarga]
        print(" ")


    @staticmethod
    def list_items():
        """
        Method untuk mencetak apapun yang telah dicetak dengan 
        masing-masing jumlah dan harga barang. 
        Untuk kolom harga barang merupakan harga per satuan barang 
        yang dikalikan dengan jumlah barang.
        """
        headers = ["No", "Nama", "Jumlah", "Harga", "Total Harga"]
        data = []
        for i, (k, v) in enumerate(keranjang.items(), start=1):
            jumlah = v[0]
            harga = v[1]
            total_harga = jumlah * harga
            row = [i, k, jumlah, harga, total_harga]
            data.append(row)
        if data:
            print(tabulate(data, headers=headers))
        else:
            print("Tidak ada barang dalam daftar belanjaan.")
        print(" ")


    @staticmethod
    def delete_item():
        """
        Method untuk menghapus barang dari list belanjaan (per item)
        """
        inputListDel = input("Item yang ingin dihapus : ")
        del keranjang[inputListDel]
        print("Delete List Item Succes")
        print(" ")


    @staticmethod
    def reset_transaction():
            """
            Method untuk menghapus seluruh barang dari list belanjaan
            atau me-reset transaksi
            """
            keranjang.clear()
            print("Transaksi berhasil di-reset")


    @staticmethod
    def check_list_item():
        """
        Method untuk memeriksa keranjang apakah jumlah elemen 
        pada item tersebut sama dengan 2. Jika iya, maka fungsi 
        akan mencetak "Data benar", tetapi jika tidak, fungsi akan 
        mencetak "Data salah". Dengan demikian, fungsi ini digunakan 
        untuk memastikan bahwa setiap item di dalam keranjang 
        memiliki jumlah elemen yang sesuai dengan format yang diharapkan.
        """
        for key, value in keranjang.items():
            if len(value) == 2:
                print("Pemesanan sudah benar")
            else:
                print("Terdapat kesalah input data")


    @staticmethod
    def total_price():
        """
        Method untuk menhitung total harga belanjaan dengan diskon sesuai ketentuan
        yang tertera pada penjelasan soal project ini.
        """
        total_harga = 0
        for key, value in keranjang.items():
            harga_barang = value[0] * value[1]
            total_harga += harga_barang

        if total_harga > 500000:
            diskon = total_harga * 0.1
        elif total_harga > 300000:
            diskon = total_harga * 0.08
        elif total_harga > 200000:
            diskon = total_harga * 0.05
        else:
            diskon = 0

        harga_akhir = total_harga - diskon
        print("Harga belanjaan anda sesudah mendapat diskon adalah : ", harga_akhir)