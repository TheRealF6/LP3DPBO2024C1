#pragma once

#include "Libraries.hh"
#include "Car.cpp"
#include "Motorcycle.cpp"

class ParkingSpot {
private:
    string nama_ps;
    string jenis_ps;
    int luas_ps;
    int kapasitas;
    int jumlah_kendaraan;
    Car daftar_kendaraan_mobil;
    Motorcycle daftar_kendaraan_motor;

public:
    ParkingSpot(string nama_ps, string jenis_ps, int luas_ps, int kapasitas, int jumlah_kendaraan, Car daftar_kendaraan_mobil, Motorcycle daftar_kendaraan_motor)
        : nama_ps(nama_ps), jenis_ps(jenis_ps), luas_ps(luas_ps), kapasitas(kapasitas), jumlah_kendaraan(jumlah_kendaraan), daftar_kendaraan_mobil(daftar_kendaraan_mobil), daftar_kendaraan_motor(daftar_kendaraan_motor) {}

    string get_nama_ps() {
        return nama_ps;
    }

    void set_nama_ps(string nama_ps) {
        this->nama_ps = nama_ps;
    }

    string get_jenis_ps() {
        return jenis_ps;
    }

    void set_jenis_ps(string jenis_ps) {
        this->jenis_ps = jenis_ps;
    }

    int get_luas_ps() {
        return luas_ps;
    }

    void set_luas_ps(int luas_ps) {
        this->luas_ps = luas_ps;
    }

    int get_kapasitas() {
        return kapasitas;
    }

    void set_kapasitas(int kapasitas) {
        this->kapasitas = kapasitas;
    }

    int get_jumlah_kendaraan() {
        return jumlah_kendaraan;
    }

    void set_jumlah_kendaraan(int jumlah_kendaraan) {
        this->jumlah_kendaraan = jumlah_kendaraan;
    }

    Car get_daftar_kendaraan_mobil() {
        return daftar_kendaraan_mobil;
    }

    void set_daftar_kendaraan(Car daftar_kendaraan_mobil) {
        this->daftar_kendaraan_mobil = daftar_kendaraan_mobil;
    }

    Motorcycle get_daftar_kendaraan_motor() {
        return daftar_kendaraan_motor;
    }

    void set_daftar_kendaraan(Motorcycle daftar_kendaraan_motor) {
        this->daftar_kendaraan_motor = daftar_kendaraan_motor;
    }
};