# Cara Menggunakan Script untuk Mengambil Data berdasarkan ID

Dokumentasi ini menjelaskan cara mengambil data berdasarkan ID menggunakan Postman atau alat sejenis dengan metode GET.

## Mengambil Data Department berdasarkan ID

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL dengan ID yang sesuai: `http://127.0.0.1:8000/department/:id/` (gunakan ID yang sesuai dengan format integer).
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data with ID = '3' has been retrieved successfully",
    "path": "/department/3/",
    "timestamp": "2024-06-26T12:29:03.587201+00:00",
    "datas": {
        "DepartmentId": 3,
        "DepartmentName": "Marketing"
    }
}
```

#### Jika ID Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/department/6/",
    "timestamp": "2024-06-26T12:29:16.790934+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "The item with ID = '6' does not exist in our records."
    }
}
```

## Mengambil Data Employee berdasarkan ID

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL dengan ID yang sesuai: `http://127.0.0.1:8000/employee/:id/` (gunakan ID yang sesuai dengan format string UUID).
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data with ID = '965fd8e7-67ac-43d6-980b-094a8a8cca7c' has been retrieved successfully",
    "path": "/employee/965fd8e7-67ac-43d6-980b-094a8a8cca7c/",
    "timestamp": "2024-06-26T12:30:04.306511+00:00",
    "datas": {
        "EmployeeId": "965fd8e7-67ac-43d6-980b-094a8a8cca7c",
        "EmployeeName": "William Amiko",
        "DepartmentId": 1,
        "DateOfJoining": "2024-06-20",
        "PhotoFileName": "william_amiko.jpg"
    }
}
```

#### Jika ID Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/employee/05456d07-c0c6-402d-b647-040a994f3aae/",
    "timestamp": "2024-06-26T12:31:06.295626+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "The item with ID = '05456d07-c0c6-402d-b647-040a994f3aae' does not exist in our records."
    }
}
```