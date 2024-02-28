from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor, merek, tahun_prod, warna, jenis_motor, kap_tangki):
        super().__init__(plat_nomor, merek, tahun_prod, warna)
        self.jenis_motor = jenis_motor
        self.kap_tangki = kap_tangki

    def get_jenis_motor(self):
        return self.jenis_motor

    def set_jenis_motor(self, jenis_motor):
        self.jenis_motor = jenis_motor

    def get_kap_tangki(self):
        return self.kap_tangki

    def set_kap_tangki(self, kap_tangki):
        self.kap_tangki = kap_tangki
