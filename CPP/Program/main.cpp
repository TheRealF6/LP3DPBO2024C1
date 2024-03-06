#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "ParkingSpot.cpp"
#include "Libraries.hh"

int main() {
    cout << "\nSelamat Datang di Program Manajemen Parkir Kendaraan!" << endl;

    Car car("D 420 BE", "Toyota", 2020, "Hitam", 5, 4);
    Motorcycle motor("B 5678 EF", "Honda", 2019, "Merah", "Skuter", 10);

    // Tempat Parkir Pertama
    ParkingSpot garasi_budi("Garasi Rumah Budi", "Garasi", 200, 5, 0, car, motor);

    cout << "==================================================" << endl;
    cout << "Data Tempat Parkir 1:" << endl;
    cout << "Nama: " << garasi_budi.get_nama_ps() << endl;
    cout << "Jenis: " << garasi_budi.get_jenis_ps() << endl;
    cout << "Luas: " << garasi_budi.get_luas_ps() << " m2" << endl;
    cout << "Kapasitas: " << garasi_budi.get_kapasitas() << " kendaraan" << endl;
    cout << "Jumlah Kendaraan Saat Ini: " << garasi_budi.get_jumlah_kendaraan() << endl;

    // Display details of the car
    cout << "\nDetail Mobil Parkir:" << endl;
    cout << "Plat Nomor: " << car.get_plat_nomor() << endl;
    cout << "Merek: " << car.get_merek() << endl;
    cout << "Tahun Produksi: " << car.get_tahun_prod() << endl;
    cout << "Warna: " << car.get_warna() << endl;
    cout << "Jumlah Kursi: " << car.get_jumlah_kursi() << endl;

    // Display details of the motorcycle
    cout << "\nDetail Motor Parkir:" << endl;
    cout << "Plat Nomor: " << motor.get_plat_nomor() << endl;
    cout << "Merek: " << motor.get_merek() << endl;
    cout << "Tahun Produksi: " << motor.get_tahun_prod() << endl;
    cout << "Warna: " << motor.get_warna() << endl;
    cout << "Jenis Motor: " << motor.get_jenis_motor() << endl;

    cout << "==================================================" << endl;

    return 0;
}
