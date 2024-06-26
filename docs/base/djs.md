# Cara Menggunakan Script Bash untuk Menjalankan Perintah Django


Untuk menggunakan script Bash yang telah Anda sediakan (`djs`) untuk menjalankan perintah-perintah Django tanpa harus mengetik `python manage.py` setiap kali, berikut adalah langkah-langkahnya:

### Langkah-langkah Penggunaan

1. **Simpan Script di Lokasi Proyek Django**

   Pastikan script Bash (`djs`) disimpan di direktori proyek Django Anda. Misalnya, letakkan di root direktori proyek atau di direktori yang mudah diakses.

2. **Beri Izin Eksekusi pada Script**

   Sebelum menggunakan script, pastikan Anda memberikan izin eksekusi agar bisa dijalankan langsung dari terminal.

   ```bash
   chmod +x djs
   ```

3. **Jalankan Perintah Django**

   Setelah memberikan izin eksekusi, Anda dapat menjalankan perintah-perintah Django seperti berikut:

   ```bash
   ./djs runserver
   ./djs migrate
   ./djs makemigrations
   ./djs createsuperuser
   ./djs collectstatic
   ./djs test
   ./djs startapp nama_app_baru
   ```

   - `runserver`: Menjalankan server pengembangan Django.
   - `migrate`: Melakukan migrasi basis data.
   - `makemigrations`: Membuat file migrasi baru.
   - `createsuperuser`: Membuat superuser baru.
   - `collectstatic`: Mengumpulkan file static ke dalam satu direktori.
   - `test`: Menjalankan semua unit tes dalam aplikasi.
   - `startapp nama_app_baru`: Membuat aplikasi Django baru dengan nama yang diberikan.

4. **Menjalankan Perintah `startapp` dengan Argumen Tambahan**

   Ketika menjalankan `startapp`, Anda dapat menambahkan nama aplikasi baru setelah perintah `startapp` diikuti dengan nama aplikasi yang diinginkan:

   ```bash
   ./djs startapp nama_app_baru
   ```

   Pastikan untuk mengganti `nama_app_baru` dengan nama yang relevan untuk aplikasi yang akan Anda buat.

### Catatan Penting

- Pastikan bahwa script `djs` dan `manage.py` berada di direktori yang sama.
- Pastikan lingkungan virtual Anda aktif jika menggunakan lingkungan virtual untuk proyek Django Anda.
- Jika mengalami kesulitan atau masalah, pastikan izin eksekusi sudah diberikan (`chmod +x djs`) dan cek path ke `manage.py` dalam variabel `MANAGE_PY` di dalam script Bash.

Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan perintah-perintah Django dengan lebih efisien melalui script Bash `djs` tanpa perlu mengetik `python manage.py` secara berulang.