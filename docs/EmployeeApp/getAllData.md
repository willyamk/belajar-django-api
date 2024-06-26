# Cara Menggunakan Script untuk Mengambil Semua Data

Dokumentasi ini menjelaskan cara mengambil semua data menggunakan Postman atau alat sejenis dengan metode GET.

## Mengambil Semua Data Department

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL: `http://127.0.0.1:8000/department/`.
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data has been retrieved successfully",
    "path": "/department/",
    "timestamp": "2024-06-26T12:26:08.151031+00:00",
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
        },
        {
            "DepartmentId": 5,
            "DepartmentName": "Sales"
        }
    ]
}
```

#### Jika Tidak Ada Data
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/department/",
    "timestamp": "2024-06-26T12:47:01.544186+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    }
}
```

## Mengambil Semua Data Employee

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL: `http://127.0.0.1:8000/employee/`.
4. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Sukses
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data has been retrieved successfully",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:27:04.318636+00:00",
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
            "EmployeeId": "c51de3e6-63d7-45a7-93fd-dfc91e3fd0a9",
            "EmployeeName": "Thomas",
            "DepartmentId": 4,
            "DateOfJoining": "2024-06-04",
            "PhotoFileName": "thomas.jpg"
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

#### Jika Tidak Ada Data
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:46:33.360437+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    }
}
```