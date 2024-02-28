from Car import Car
from Motorcycle import Motorcycle
from ParkingSpot import ParkingSpot

def main():
    print("Selamat Datang di Program Manajemen Parkir Kendaraan!\n")

    # Tempat Parkir Pertama
    garasi_budi = ParkingSpot("Garasi Rumah Budi", "Garasi", 200, 5, 0)

    print("==================================================")
    print("Data Tempat Parkir 1:")
    print(f"Nama: {garasi_budi.get_nama_ps()}")
    print(f"Jenis: {garasi_budi.get_jenis_ps()}")
    print(f"Luas: {garasi_budi.get_luas_ps()} m2")
    print(f"Kapasitas: {garasi_budi.get_kapasitas()} kendaraan")
    print(f"Jumlah Kendaraan Saat Ini: {garasi_budi.get_jumlah_kendaraan()}")
    print("==================================================")

    daftar_kendaraan = [
        Car("D 420 BE", "Toyota", 2020, "Hitam", 5, 4),
        Motorcycle("B 5678 EF", "Honda", 2019, "Merah", "Skuter", 10),
        Car("D 1 ANA", "Nissan", 2018, "Putih", 4, 4),
        Motorcycle("B 5432 GH", "Yamaha", 2021, "Biru", "Sport", 15),
        Car("D 1234 XD", "Pontiac", 2006, "Hijau", 2, 4),
        Motorcycle("B 2233 HJ", "Suzuki", 2011, "Kuning", "Bebek", 15)
    ]

    if len(garasi_budi.get_daftar_kendaraan()) < garasi_budi.get_kapasitas():
        for kendaraan in daftar_kendaraan:
            if isinstance(kendaraan, Car):
                garasi_budi.get_daftar_kendaraan().append(kendaraan)
                garasi_budi.set_jumlah_kendaraan(garasi_budi.get_jumlah_kendaraan() + 1)
                print(f"{kendaraan.get_merek()} dengan plat nomor {kendaraan.get_plat_nomor()} berhasil ditambahkan ke dalam garasi.")
        for kendaraan in daftar_kendaraan:
            if isinstance(kendaraan, Motorcycle):
                if len(garasi_budi.get_daftar_kendaraan()) < garasi_budi.get_kapasitas():
                    garasi_budi.get_daftar_kendaraan().append(kendaraan)
                    garasi_budi.set_jumlah_kendaraan(garasi_budi.get_jumlah_kendaraan() + 1)
                    print(f"{kendaraan.get_merek()} dengan plat nomor {kendaraan.get_plat_nomor()} berhasil ditambahkan ke dalam garasi.")
                else:
                    print("Garasi sudah penuh. Tidak dapat menambahkan kendaraan.")
                    break
    else:
        print("Garasi sudah penuh. Tidak dapat menambahkan kendaraan.")
    

    print("==================================================")
    print("Daftar Kendaraan:")
    for kendaraan in garasi_budi.get_daftar_kendaraan():
        if isinstance(kendaraan, Car):
            print(f"Car: {kendaraan.get_merek()} | Plat Nomor: {kendaraan.get_plat_nomor()} | Tahun Produksi: {kendaraan.get_tahun_prod()} | Warna: {kendaraan.get_warna()} | Jumlah Kursi: {kendaraan.get_jumlah_kursi()}")
    for kendaraan in garasi_budi.get_daftar_kendaraan():
        if isinstance(kendaraan, Motorcycle):
            print(f"Motorcycle: {kendaraan.get_merek()} | Plat Nomor: {kendaraan.get_plat_nomor()} | Tahun Produksi: {kendaraan.get_tahun_prod()} | Warna: {kendaraan.get_warna()} | Jenis Motor: {kendaraan.get_jenis_motor()}")
    print("==================================================\n")

    # Tempat Parkir Kedua
    parkir_alfamart = ParkingSpot("Parkiran Alfamart Gerlong", "Lapang Parkiran", 400, 12, 0)
    
    print("==================================================")
    print("Data Tempat Parkir 2:")
    print(f"Nama: {parkir_alfamart.get_nama_ps()}")
    print(f"Jenis: {parkir_alfamart.get_jenis_ps()}")
    print(f"Luas: {parkir_alfamart.get_luas_ps()} m2")
    print(f"Kapasitas: {parkir_alfamart.get_kapasitas()} kendaraan")
    print(f"Jumlah Kendaraan Saat Ini: {parkir_alfamart.get_jumlah_kendaraan()}")
    print("==================================================")

    daftar_kendaraan = [
        Car("D 1234 AB", "Lexus", 2010, "Merah", 3, 2),
        Motorcycle("F 9876 ZY", "Triumph", 2016, "Jingga", "Touring", 20),
        Car("D 2345 BC", "De Tomaso", 2011, "Kuning", 3, 2),
        Motorcycle("F 8765 YX", "Ducati", 2017, "Hijau Muda", "Naked", 25),
        Car("D 3456 CD", "Pagani", 2012, "Hijau", 3, 2),
        Motorcycle("F 7654 XW", "Yamaha", 2018, "Pirus", "Dual-Sport", 30),
        Car("D 4567 DE", "TVR", 2013, "Biru Muda", 3, 2),
        Motorcycle("F 6543 WV", "Honda", 2019, "Biru", "Skuter", 35),
        Car("D 5678 EF", "Lada", 2014, "Ungu", 5, 4),
        Motorcycle("F 5432 VU", "Suzuki", 2020, "Magenta", "Cruiser", 40),
        Car("D 6789 FG", "Chery", 2015, "Marun", 5, 4),
        Motorcycle("F 4321 UT", "Aprilia", 2011, "Merah Muda", "Sport", 45)
    ]

    if len(parkir_alfamart.get_daftar_kendaraan()) < parkir_alfamart.get_kapasitas():
        for kendaraan in daftar_kendaraan:
            if isinstance(kendaraan, Car):
                parkir_alfamart.get_daftar_kendaraan().append(kendaraan)
                parkir_alfamart.set_jumlah_kendaraan(parkir_alfamart.get_jumlah_kendaraan() + 1)
                print(f"{kendaraan.get_merek()} dengan plat nomor {kendaraan.get_plat_nomor()} berhasil ditambahkan ke dalam garasi.")
        for kendaraan in daftar_kendaraan:
            if isinstance(kendaraan, Motorcycle):
                if len(parkir_alfamart.get_daftar_kendaraan()) < parkir_alfamart.get_kapasitas():
                    parkir_alfamart.get_daftar_kendaraan().append(kendaraan)
                    parkir_alfamart.set_jumlah_kendaraan(parkir_alfamart.get_jumlah_kendaraan() + 1)
                    print(f"{kendaraan.get_merek()} dengan plat nomor {kendaraan.get_plat_nomor()} berhasil ditambahkan ke dalam garasi.")
                else:
                    print("Garasi sudah penuh. Tidak dapat menambahkan kendaraan.")
                    break
    else:
        print("Garasi sudah penuh. Tidak dapat menambahkan kendaraan.")
    

    print("==================================================")
    print("Daftar Kendaraan:")
    for kendaraan in parkir_alfamart.get_daftar_kendaraan():
        if isinstance(kendaraan, Car):
            print(f"Car: {kendaraan.get_merek()} | Plat Nomor: {kendaraan.get_plat_nomor()} | Tahun Produksi: {kendaraan.get_tahun_prod()} | Warna: {kendaraan.get_warna()} | Jumlah Kursi: {kendaraan.get_jumlah_kursi()}")
    for kendaraan in parkir_alfamart.get_daftar_kendaraan():
        if isinstance(kendaraan, Motorcycle):
            print(f"Motorcycle: {kendaraan.get_merek()} | Plat Nomor: {kendaraan.get_plat_nomor()} | Tahun Produksi: {kendaraan.get_tahun_prod()} | Warna: {kendaraan.get_warna()} | Jenis Motor: {kendaraan.get_jenis_motor()}")
    print("==================================================")


if __name__ == "__main__":
    main()
