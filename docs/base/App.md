# Langkah-langkah Membuat Proyek Django API dengan MongoDB

Dokumentasi ini menjelaskan langkah-langkah untuk membuat proyek Django API dengan menggunakan MongoDB sebagai basis data.

> [!IMPORTANT]
> **Pastikan Anda membaca semua file yang ada dalam proyek ini dan mengikuti langkah-langkah yang ada dalam file tersebut!**

## 1. Pembuatan Proyek Django

Untuk membuat proyek Django, ikuti langkah berikut di terminal:

```bash
django-admin startproject belajar_django_api
cd belajar_django_api
```

## 2. Membuat Aplikasi EmployeeApp

Selanjutnya, buat aplikasi Django baru bernama `EmployeeApp` dengan perintah:

```bash
python manage.py startapp EmployeeApp
```
atau menggunakan alias jika sudah diatur:
```bash
./djs startapp EmployeeApp
```

## 3. Menjalankan Migrasi Model

Setelah membuat model dalam aplikasi `EmployeeApp`, buat migrasi untuk model tersebut dengan perintah:

```bash
python manage.py makemigrations EmployeeApp
```
atau dengan alias:
```bash
./djs makemigrations EmployeeApp
```

## 4. Menjalankan Migrasi Basis Data

Jalankan migrasi untuk menerapkan perubahan pada basis data MongoDB:

> [!WARNING]
> **Pastikan Anda sudah membuat basis data MongoDB dengan nama `belajar_django_api` dan collection `myCollection`**

```bash
python manage.py migrate EmployeeApp
```
atau dengan alias:
```bash
./djs migrate EmployeeApp
```

## 5. Menjalankan Server Django

Jalankan server django menggunakan perintah:

```bash
python manage.py runserver
```
atau dengan alias:
```bash
./djs runserver
```

## Konfigurasi `settings.py`

Sebelum menjalankan migrasi, pastikan untuk mengkonfigurasi `settings.py` dalam direktori proyek `belajar_django_api`.

Tambahkan konfigurasi berikut ini:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "corsheaders",
    "EmployeeApp.apps.EmployeeappConfig",
]

# Not Recommended In Production
CORS_ALLOWED_ORIGINS_ALL = True

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "CLIENT": {
            "host": "mongodb://localhost:27017/",
            "name": "belajar_django_api",
        },
    }
}
```

Pastikan untuk menginstal library `djongo` dan `dnspython` dengan perintah:

```bash
pip install djongo dnspython
```

Dengan langkah-langkah di atas, Anda sudah siap membuat proyek Django API dengan basis data MongoDB.

```

Dokumentasi di atas memberikan langkah-langkah untuk membuat proyek Django API dengan MongoDB, serta konfigurasi yang perlu dilakukan sebelum menjalankan migrasi.
```