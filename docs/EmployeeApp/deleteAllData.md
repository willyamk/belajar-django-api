# Cara Menggunakan Script untuk Menghapus Semua Data

Dokumentasi ini menjelaskan cara menghapus semua data menggunakan Postman atau alat sejenis dengan metode DELETE.

## Menghapus Semua Data Department

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `DELETE`.
3. Masukkan URL: `http://127.0.0.1:8000/department/`.
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 204,
    "message": "All data has been deleted successfully",
    "path": "/department/",
    "timestamp": "2024-06-26T12:41:18.809539+00:00",
    "datas": [
        {
            "DepartmentId": 1,
            "DepartmentName": "Human Resource"
        },
        {
            "DepartmentId": 2,
            "DepartmentName": "Finance"
        },
        {
            "DepartmentId": 3,
            "DepartmentName": "Marketing"
        },
        {
            "DepartmentId": 4,
            "DepartmentName": "Operations"
        }
    ]
}
```

#### Jika Data Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "No data found to delete",
    "path": "/department/",
    "timestamp": "2024-06-26T12:41:30.485709+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    }
}
```

## Menghapus Semua Data Employee

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `DELETE`.
3. Masukkan URL: `http://127.0.0.1:8000/employee/`.
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 204,
    "message": "All data has been deleted successfully",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:41:18.809539+00:00",
    "datas": [
        {
            "EmployeeId": "965fd8e7-67ac-43d6-980b-094a8a8cca7c",
            "EmployeeName": "William Amiko",
            "DepartmentId": 1,
            "DateOfJoining": "2024-06-20",
            "PhotoFileName": "william_amiko.jpg"
        },
        {
            "EmployeeId": "a897b016-ecc9-4e26-8892-473b2e3bc217",
            "EmployeeName": "Alexander",
            "DepartmentId": 3,
            "DateOfJoining": "2024-05-21",
            "PhotoFileName": "alexander.jpg"
        },
        {
            "EmployeeId": "fbb1de15-9f82-4a63-9d93-873430bb6246",
            "EmployeeName": "Williams Hanna",
            "DepartmentId": 2,
            "DateOfJoining": "2024-05-04",
            "PhotoFileName": "hanna.jpg"
        }
    ]
}
```

#### Jika Data Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "No data found to delete",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:42:02.645263+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    }
}
```