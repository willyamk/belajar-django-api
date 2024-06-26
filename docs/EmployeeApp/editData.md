# Dokumentasi Penggunaan Script untuk Mengubah Data dengan Postman

## Pendahuluan

Dokumentasi ini menjelaskan cara menggunakan Postman atau alat serupa untuk mengubah data dalam sistem menggunakan metode PATCH. Ada dua jenis data yang dapat diubah, yaitu data departemen dan data karyawan.

## Mengubah Data Departemen

### Langkah 1: Buka Postman
1. Buka aplikasi Postman.

### Langkah 2: Buat Request Baru
1. Klik tombol **New** atau **Request**.
2. Pilih **PATCH** sebagai metode.
3. Masukkan URL dengan menyertakan ID departemen yang ingin diubah `http://127.0.0.1:8000/department/:id/` (gunakan ID yang sesuai dengan format integer).

### Langkah 3: Masukkan Data
1. Pilih tab **Body**.
2. Pilih **raw**.
3. Pilih format **JSON**.
4. Masukkan data departemen yang ingin diubah dalam format JSON seperti berikut:
    ```json
    {
        "DepartmentName": "IT"
    }
    ```

### Langkah 4: Kirim Request
1. Klik tombol **Send**.

### Hasil yang Diharapkan
- **Jika Berhasil**:
    ```json
    {
        "status": "success",
        "status_code": 200,
        "message": "Data has been updated successfully",
        "path": "/department/1/",
        "timestamp": "2024-06-26T12:12:57.546346+00:00",
        "datas": {
            "DepartmentId": 1,
            "DepartmentName": "IT"
        }
    }
    ```

- **Jika Gagal karena Validasi**:
    ```json
    {
        "status": "error",
        "status_code": 400,
        "message": "The request was invalid or cannot be served",
        "path": "/department/1/",
        "timestamp": "2024-06-26T12:13:10.320279+00:00",
        "errors": {
            "code": "BAD_REQUEST",
            "message": {
                "DepartmentName": [
                    "This field may not be blank."
                ]
            }
        }
    }
    ```

- **Jika Gagal karena ID Tidak Ditemukan**:
    ```json
    {
        "status": "error",
        "status_code": 404,
        "message": "The requested resource was not found",
        "path": "/department/6/",
        "timestamp": "2024-06-26T12:13:35.482729+00:00",
        "errors": {
            "code": "RESOURCE_NOT_FOUND",
            "message": "The item with ID = '6' does not exist in our records."
        }
    }
    ```

## Mengubah Data Karyawan

### Catatan
Pastikan ID karyawan yang ingin diubah sudah ada dalam sistem.

### Langkah 1: Buka Postman
1. Buka aplikasi Postman.

### Langkah 2: Buat Request Baru
1. Klik tombol **New** atau **Request**.
2. Pilih **PATCH** sebagai metode.
3. Masukkan URL dengan menyertakan ID karyawan yang ingin diubah `http://127.0.0.1:8000/employee/:id/` (gunakan ID yang sesuai dengan format string UUID).

### Langkah 3: Masukkan Data
1. Pilih tab **Body**.
2. Pilih **raw**.
3. Pilih format **JSON**.
4. Masukkan data karyawan yang ingin diubah dalam format JSON seperti berikut:
    ```json
    {
        "EmployeeName": "William",
        "DepartmentId": 2,
        "DateOfJoining": "2024-06-26",
        "PhotoFileName": "edit_william.jpg"
    }
    ```

### Langkah 4: Kirim Request
1. Klik tombol **Send**.

### Hasil yang Diharapkan
- **Jika Berhasil**:
    ```json
    {
        "status": "success",
        "status_code": 200,
        "message": "Data has been updated successfully",
        "path": "/employee/965fd8e7-67ac-43d6-980b-094a8a8cca7c/",
        "timestamp": "2024-06-26T12:15:26.952894+00:00",
        "datas": {
            "EmployeeId": "965fd8e7-67ac-43d6-980b-094a8a8cca7c",
            "EmployeeName": "William",
            "DepartmentId": 2,
            "DateOfJoining": "2024-06-26",
            "PhotoFileName": "edit_william.jpg"
        }
    }
    ```

- **Jika Gagal karena Validasi**:
    ```json
    {
        "status": "error",
        "status_code": 400,
        "message": "The request was invalid or cannot be served",
        "path": "/employee/965fd8e7-67ac-43d6-980b-094a8a8cca7c/",
        "timestamp": "2024-06-26T12:15:49.724729+00:00",
        "errors": {
            "code": "BAD_REQUEST",
            "message": {
                "EmployeeName": [
                    "This field may not be blank."
                ],
                "DepartmentId": [
                    "Invalid pk \"6\" - object does not exist."
                ],
                "DateOfJoining": [
                    "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
                ],
                "PhotoFileName": [
                    "This field may not be blank."
                ]
            }
        }
    }
    ```

- **Jika Gagal karena ID Tidak Ditemukan**:
    ```json
    {
        "status": "error",
        "status_code": 404,
        "message": "The requested resource was not found",
        "path": "/employee/05456d07-c0c6-402d-b647-040a994f3aae/",
        "timestamp": "2024-06-26T12:16:35.626213+00:00",
        "errors": {
            "code": "RESOURCE_NOT_FOUND",
            "message": "The item with ID = '05456d07-c0c6-402d-b647-040a994f3aae' does not exist in our records."
        }
    }
    ```