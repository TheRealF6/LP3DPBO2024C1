from Car import Car
from Motorcycle import Motorcycle

class ParkingSpot:
    def __init__(self, nama_ps, jenis_ps, luas_ps, kapasitas, jumlah_kendaraan):
        self.nama_ps = nama_ps
        self.jenis_ps = jenis_ps
        self.luas_ps = luas_ps
        self.kapasitas = kapasitas
        self.jumlah_kendaraan = jumlah_kendaraan
        self.daftar_kendaraan = []

    def get_nama_ps(self):
        return self.nama_ps

    def set_nama_ps(self, nama_ps):
        self.nama_ps = nama_ps

    def get_jenis_ps(self):
        return self.jenis_ps

    def set_jenis_ps(self, jenis_ps):
        self.jenis_ps = jenis_ps

    def get_luas_ps(self):
        return self.luas_ps

    def set_luas_ps(self, luas_ps):
        self.luas_ps = luas_ps

    def get_kapasitas(self):
        return self.kapasitas

    def set_kapasitas(self, kapasitas):
        self.kapasitas = kapasitas

    def get_jumlah_kendaraan(self):
        return self.jumlah_kendaraan
    
    def set_jumlah_kendaraan(self, jumlah_kendaraan):
        self.jumlah_kendaraan = jumlah_kendaraan

    def get_daftar_kendaraan(self):
        return self.daftar_kendaraan
    
    def set_daftar_kendaraan(self, daftar_kendaraan):
        self.daftar_kendaraan = daftar_kendaraan