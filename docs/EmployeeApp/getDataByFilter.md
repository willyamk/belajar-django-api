# Cara Menggunakan Script untuk Mengambil Data berdasarkan Filter

Dokumentasi ini menjelaskan cara mengambil data berdasarkan filter menggunakan Postman atau alat sejenis dengan metode GET.

## Mengambil Data Department berdasarkan Nama Departemen

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL tanpa ID: `http://127.0.0.1:8000/department`.
4. Klik tab `Params` di bawah URL.
5. Masukkan Key dengan nama `search` dengan Value berdasarkan `DepartmentName`.
6. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Data Ditemukan
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data has been retrieved successfully",
    "path": "/department/",
    "timestamp": "2024-06-26T12:32:47.846292+00:00",
    "datas": [
        {
            "DepartmentId": 1,
            "DepartmentName": "Human Resource"
        },
        {
            "DepartmentId": 3,
            "DepartmentName": "Marketing"
        }
    ],
    "search": "ma"
}
```

#### Jika Data Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/department/",
    "timestamp": "2024-06-26T12:33:17.855315+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    },
    "search": "test"
}
```

## Mengambil Data Employee berdasarkan Nama Pegawai

### Langkah-langkah:
1. Buka Postman atau aplikasi sejenis.
2. Pilih metode `GET`.
3. Masukkan URL tanpa ID: `http://127.0.0.1:8000/employee`.
4. Klik tab `Params` di bawah URL.
5. Masukkan Key dengan nama `search` dengan Value berdasarkan `EmployeeName`.
6. Klik `Send`.

### Hasil yang Diharapkan

#### Jika Data Ditemukan
Respon akan berupa:
```json
{
    "status": "success",
    "status_code": 200,
    "message": "Data has been retrieved successfully",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:34:36.105004+00:00",
    "datas": [
        {
            "EmployeeId": "965fd8e7-67ac-43d6-980b-094a8a8cca7c",
            "EmployeeName": "William Amiko",
            "DepartmentId": 1,
            "DateOfJoining": "2024-06-20",
            "PhotoFileName": "william_amiko.jpg"
        },
        {
            "EmployeeId": "fbb1de15-9f82-4a63-9d93-873430bb6246",
            "EmployeeName": "Williams Hanna",
            "DepartmentId": 2,
            "DateOfJoining": "2024-05-04",
            "PhotoFileName": "hanna.jpg"
        }
    ],
    "search": "william"
}
```

#### Jika Data Tidak Ditemukan
Respon akan berupa:
```json
{
    "status": "error",
    "status_code": 404,
    "message": "The requested resource was not found",
    "path": "/employee/",
    "timestamp": "2024-06-26T12:34:22.305993+00:00",
    "errors": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "No records found."
    },
    "search": "test"
}
```