#pragma once

#include "Libraries.hh"
#include "Vehicle.cpp"

class Motorcycle : public Vehicle {
private:
    string jenis_motor;
    int kap_tangki;

public:
    Motorcycle(string plat_nomor, string merek, int tahun_prod, string warna, string jenis_motor, int kap_tangki)
        : Vehicle(plat_nomor, merek, tahun_prod, warna), jenis_motor(jenis_motor), kap_tangki(kap_tangki) {}

    string get_jenis_motor() {
        return jenis_motor;
    }

    void set_jenis_motor(string jenis_motor) {
        this->jenis_motor = jenis_motor;
    }

    int get_kap_tangki() {
        return kap_tangki;
    }

    void set_kap_tangki(int kap_tangki) {
        this->kap_tangki = kap_tangki;
    }
};
