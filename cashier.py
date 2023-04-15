from dataclasses import dataclass
from transaction import Transaction


@dataclass
class Cashier:
    """
    Kelas ini dapat diibaratkan seperti kasir, ataupun hasil implementasi dari
    method-method yang ada di kelas Transaction.
    """
    condition: bool
    
    def action(self):
        """
        Method untuk menampilkan menu dan meminta input dari user.

            Jika 1 maka akan meng-inputkan item belanjaan
            Jika 2 maka meng-update item
            Jika 3 maka menampilkan list item
            Jika 4 maka menghapus item
            Jika 5 maka menghapus semua item atau me-reset transaksi
            Jika 6 maka memerika belanjaan sudah seusai atau belum
            Jika 7 maka akan menghitung total belanjaan dan menghitung diskon
        """
        while self.condition:

            print(f"1. Input List Item")
            print(f"2. Update List Item")
            print(f"3. List Items")
            print(f"4. Delete Item")
            print(f"5. Reset Transaction")
            print(f"6. Check order")
            print(f"7. Total Price")
            
            userInput = input("Masukan pilihan disini : ")

            if userInput == "1":
                print()
                Transaction.add_item()
            elif userInput == "2":
                print()
                Transaction.update_item()
            elif userInput == "3":
                print()
                Transaction.list_items()  
            elif userInput == "4":
                print()
                Transaction.delete_item()   
            elif userInput == "5":
                print()
                Transaction.reset_transaction()
            elif userInput == "6":
                print("Pemesanan sudah benar")
                Transaction.check_list_item()  
            elif userInput == "7":
                Transaction.total_price()                    
            else:
                print()
                print("Tolong masukan nomor yang sesuai")
                self.action()
