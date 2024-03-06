#pragma once

#include "Libraries.hh"
#include "Vehicle.cpp"

class Car : public Vehicle {
private:
    int jumlah_kursi;
    int jumlah_pintu;

public:
    Car(string plat_nomor, string merek, int tahun_prod, string warna, int jumlah_kursi, int jumlah_pintu)
        : Vehicle(plat_nomor, merek, tahun_prod, warna), jumlah_kursi(jumlah_kursi), jumlah_pintu(jumlah_pintu) {}

    int get_jumlah_kursi() {
        return jumlah_kursi;
    }

    void set_jumlah_kursi(int jumlah_kursi) {
        this->jumlah_kursi = jumlah_kursi;
    }

    int get_jumlah_pintu() {
        return jumlah_pintu;
    }

    void set_jumlah_pintu(int jumlah_pintu) {
        this->jumlah_pintu = jumlah_pintu;
    }
};
