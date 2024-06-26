# Cara Menggunakan Script untuk Menghapus Data berdasarkan ID

Dokumentasi ini menjelaskan cara menghapus data menggunakan Postman atau alat sejenis dengan metode DELETE.

## Menghapus Data Department

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `DELETE`.
3. Masukkan URL dengan ID yang sesuai, contoh: `http://127.0.0.1:8000/department/:id/`(gunakan ID yang sesuai dengan format integer).
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 204,
    "message": "Data with ID = '5' has been deleted successfully",
    "path": "/department/5/",
    "timestamp": "2024-06-26T12:35:12.177055+00:00",
    "datas": {
        "DepartmentId": 5,
        "DepartmentName": "Sales"
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
    "timestamp": "2024-06-26T12:36:25.398841+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "The item with ID = '6' does not exist in our records."
    }
}
```

## Menghapus Data Employee

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `DELETE`.
3. Masukkan URL dengan ID yang sesuai `http://127.0.0.1:8000/employee/:id/` (gunakan ID yang sesuai dengan format string UUID).
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 204,
    "message": "Data with ID = 'c51de3e6-63d7-45a7-93fd-dfc91e3fd0a9' has been deleted successfully",
    "path": "/employee/c51de3e6-63d7-45a7-93fd-dfc91e3fd0a9/",
    "timestamp": "2024-06-26T12:37:11.369833+00:00",
    "datas": {
        "EmployeeId": "c51de3e6-63d7-45a7-93fd-dfc91e3fd0a9",
        "EmployeeName": "Thomas",
        "DepartmentId": 4,
        "DateOfJoining": "2024-06-04",
        "PhotoFileName": "thomas.jpg"
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
    "timestamp": "2024-06-26T12:38:01.352972+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "The item with ID = '05456d07-c0c6-402d-b647-040a994f3aae' does not exist in our records."
    }
}
```