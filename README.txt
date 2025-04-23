# Showroom Car Web App

Showroom Car Web App adalah aplikasi berbasis web untuk mengelola data mobil yang tersedia di showroom, memungkinkan admin atau staf showroom untuk menambah, menampilkan, mengelola data mobil, serta menambahkan catatan servis dan menghitung harga pokok produksi (HPP) mobil.

# Fitur Tersedia:
Menambah Mobil: Menambahkan mobil baru ke dalam daftar showroom.
- Menampilkan Semua Mobil: Menampilkan daftar semua mobil yang tersedia di showroom.
- Menampilkan Detail Mobil: Menampilkan informasi lebih lanjut tentang mobil tertentu.
- Menambah Service Mobil: Menambah informasi servis yang telah dilakukan pada mobil.
- Menghitung HPP (Harga Pokok Produksi): Fitur untuk menghitung biaya produksi mobil berdasarkan parameter yang dimasukkan.
- Menghapus Mobil: Fitur untuk menghapus mobil dari daftar showroom.

# Fitur yang belum ditampilkan:
Halaman admin (localhost:8000/admin/)masih dalam pengembangan dan tidak diaktifkan untuk saat ini.

# Instalasi di Linux
1. Persiapan, install dependensi yang dibutuhkan
`sudo apt install python3 python3-pip python3-venv git -y`
2. Clone project
`git clone https://github.com/kumiawan/car-showroom-web.git && cd showroom`
3. Bikin virtual enviroment python
`python3 -m venv showroomvenv`
4. Aktifkan showroomvenv
`source showroomvenv/bin/activate`
note : Untuk keluar dari virtual environtment, jalankan `deactivate`
5. Install dependensi semua yang diperlukan melalui file requirements.txt
pip install -r requirements.txt
6. Migrasi database, membuat struktur database yang diperlukan
`python manage.py migrate`
7. Buat Superuser (Opsional), untuk akses admin
`python manage.py cratesuperuser`
8. Jalankan server django, setelah semua langkah diatas selesai
`python manage.py runserver`

# Cara Berkontribusi:
Jika kamu ingin berkontribusi, berikut adalah langkah-langkah yang perlu dilakukan:
1. Fork repo ini.
2. Buat branch baru untuk fitur atau perbaikan (`git checkout -b feature-name`).
3. Commit perubahan kamu (`git commit -am 'Add new feature'`).
4. Push ke branch (`git push origin feature-name`).
5. Buat pull request.

# Teknologi yang Digunakan:
- Python Django digunakan sebagai backend dan mengelola data.
- CDN DaisyUi digunakan membangun UI component yang responsive dan modern, tanpa terlalu banyak konfigurasi.
