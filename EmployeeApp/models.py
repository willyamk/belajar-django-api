import uuid
from django.db import models


# Model untuk tabel Departments yang menyimpan data departemen
class Departments(models.Model):
    # Field untuk menyimpan ID departemen, otomatis bertambah
    DepartmentId = models.AutoField(primary_key=True)
    # Field untuk menyimpan nama departemen, dengan maksimal panjang 500 karakter
    DepartmentName = models.CharField(max_length=500)


# Model untuk tabel Employees yang menyimpan data karyawan
class Employees(models.Model):
    # Field untuk menyimpan ID karyawan, menggunakan UUID sebagai default value dan tidak bisa diubah
    EmployeeId = models.CharField(
        primary_key=True, max_length=36, default=uuid.uuid4, editable=False
    )
    # Field untuk menyimpan nama karyawan, dengan maksimal panjang 500 karakter
    EmployeeName = models.CharField(max_length=500)
    # Field untuk menyimpan ID departemen, sebagai foreign key yang menghubungkan ke tabel Departments
    DepartmentId = models.ForeignKey(Departments, on_delete=models.CASCADE)
    # Field untuk menyimpan tanggal bergabungnya karyawan
    DateOfJoining = models.DateField()
    # Field untuk menyimpan nama file foto karyawan, dengan maksimal panjang 500 karakter
    PhotoFileName = models.CharField(max_length=500)
