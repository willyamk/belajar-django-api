# Dokumentasi Penggunaan Script Menambah Data dengan Postman

## Pendahuluan

Dokumentasi ini menjelaskan cara menggunakan Postman atau alat serupa untuk menambah data ke dalam sistem melalui metode POST. Ada dua jenis data yang perlu ditambahkan, yaitu data departemen dan data karyawan. Data departemen harus ditambahkan terlebih dahulu karena `DepartmentId` pada data karyawan bertindak sebagai foreign key.

## Menambah Data Departemen

### Langkah 1: Buka Postman
1. Buka aplikasi Postman.

### Langkah 2: Buat Request Baru
1. Klik tombol **New** atau **Request**.
2. Pilih **POST** sebagai metode.
3. Masukkan URL: `http://127.0.0.1:8000/department/`.

### Langkah 3: Masukkan Data
1. Pilih tab **Body**.
2. Pilih **raw**.
3. Pilih format **JSON**.
4. Masukkan data departemen dalam format JSON sebagai berikut:
    ```json
    {
        "DepartmentName": "Human Resource"
    }
    ```

### Langkah 4: Kirim Request
1. Klik tombol **Send**.

### Hasil yang Diharapkan
- **Jika Berhasil**:
    ```json
    {
        "status": "success",
        "status_code": 201,
        "message": "Data has been created successfully",
        "path": "/department/",
        "timestamp": "2024-06-26T11:54:10.448448+00:00",
        "datas": {
            "DepartmentId": 1,
            "DepartmentName": "Human Resource"
        }
    }
    ```

- **Jika Gagal**:
    ```json
    {
        "status": "error",
        "status_code": 400,
        "message": "The request was invalid or cannot be served",
        "path": "/department/",
        "timestamp": "2024-06-26T11:58:44.849052+00:00",
        "errors": {
            "code": "BAD_REQUEST",
            "message": {
                "DepartmentName": [
                    "This field is required."
                ]
            }
        }
    }
    ```

## Menambah Data Karyawan

### Catatan
Pastikan data departemen telah ditambahkan terlebih dahulu karena `DepartmentId` diperlukan sebagai foreign key pada data karyawan.

### Langkah 1: Buka Postman
1. Buka aplikasi Postman.

### Langkah 2: Buat Request Baru
1. Klik tombol **New** atau **Request**.
2. Pilih **POST** sebagai metode.
3. Masukkan URL: `http://127.0.0.1:8000/employee/`.

### Langkah 3: Masukkan Data
1. Pilih tab **Body**.
2. Pilih **raw**.
3. Pilih format **JSON**.
4. Masukkan data karyawan dalam format JSON sebagai berikut:
    ```json
    {
        "EmployeeName": "William Amiko",
        "DepartmentId": 1,
        "DateOfJoining": "2024-06-20",
        "PhotoFileName": "william_amiko.jpg"
    }
    ```

### Langkah 4: Kirim Request
1. Klik tombol **Send**.

### Hasil yang Diharapkan
- **Jika Berhasil**:
    ```json
    {
        "status": "success",
        "status_code": 201,
        "message": "Data has been created successfully",
        "path": "/employee/",
        "timestamp": "2024-06-26T11:59:47.539320+00:00",
        "datas": {
            "EmployeeId": "965fd8e7-67ac-43d6-980b-094a8a8cca7c",
            "EmployeeName": "William Amiko",
            "DepartmentId": 1,
            "DateOfJoining": "2024-06-20",
            "PhotoFileName": "william_amiko.jpg"
        }
    }
    ```

- **Jika Gagal**:
    ```json
    {
        "status": "error",
        "status_code": 400,
        "message": "The request was invalid or cannot be served",
        "path": "/employee/",
        "timestamp": "2024-06-26T12:00:38.382124+00:00",
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