#pragma once

#include "Libraries.hh"

class Vehicle {
private:
    string plat_nomor;
    string merek;
    int tahun_prod;
    string warna;

public:
    Vehicle(string plat_nomor, string merek, int tahun_prod, string warna) : plat_nomor(plat_nomor), merek(merek), tahun_prod(tahun_prod), warna(warna) {}

    string get_plat_nomor() {
        return plat_nomor;
    }

    void set_plat_nomor(string plat_nomor) {
        this->plat_nomor = plat_nomor;
    }

    string get_merek() {
        return merek;
    }

    void set_merek(string merek) {
        this->merek = merek;
    }

    int get_tahun_prod() {
        return tahun_prod;
    }

    void set_tahun_prod(int tahun_prod) {
        this->tahun_prod = tahun_prod;
    }

    string get_warna() {
        return warna;
    }

    void set_warna(string warna) {
        this->warna = warna;
    }
};
