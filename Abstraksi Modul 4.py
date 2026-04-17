#Abstraksi Modul 4
# Wajib mengimpor modul ini untuk membuat Abstraksi di Python
from abc import ABC, abstractmethod

# 1. CLASS ABSTRAK (Kerangka Dasar / Konsep)
class Hewan(ABC): 
    def __init__(self, nama):
        self.nama = nama

    # 2. METHOD ABSTRAK (Aturan wajib yang harus diikuti anak-anaknya)
    @abstractmethod
    def bersuara(self):
        pass # Isinya dibiarkan kosong karena akan diisi oleh class anak
        
    # Method biasa (Boleh ada di dalam class abstrak)
    def info(self):
        print(f"Hewan ini bernama {self.nama}.")

# 3. CLASS ANAK 1
class Anjing(Hewan):
    # Wajib membuat ulang method bersuara()!
    def bersuara(self):
        return "Woof! Woof!"

# 4. CLASS ANAK 2
class Kucing(Hewan):
    # Wajib membuat ulang method bersuara()!
    def bersuara(self):
        return "Meowww!"

# --- MARI KITA UJI ---

# COBA BUKA KOMENTAR DI BAWAH INI, PASTI PROGRAM AKAN ERROR!
# hewan_gaib = Hewan("Sesuatu") 

# Ini yang benar (Mencetak dari class anak yang wujudnya jelas)
anjing_saya = Anjing("Max")
anjing_saya.info()
print("Suaranya:", anjing_saya.bersuara())

print("-" * 20)

kucing_saya = Kucing("Oyen")
kucing_saya.info()
print("Suaranya:", kucing_saya.bersuara())