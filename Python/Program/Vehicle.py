class Vehicle:
    def __init__(self, plat_nomor, merek, tahun_prod, warna):
        self.plat_nomor = plat_nomor
        self.merek = merek
        self.tahun_prod = tahun_prod
        self.warna = warna

    def get_plat_nomor(self):
        return self.plat_nomor

    def set_plat_nomor(self, plat_nomor):
        self.plat_nomor = plat_nomor

    def get_merek(self):
        return self.merek

    def set_merek(self, merek):
        self.merek = merek

    def get_tahun_prod(self):
        return self.tahun_prod

    def set_tahun_prod(self, tahun_prod):
        self.tahun_prod = tahun_prod

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna
