from rest_framework import serializers
from EmployeeApp.models import Departments, Employees


# Serializer untuk model Departments
class DepartmentSerializer(serializers.ModelSerializer):
    # Meta class untuk menentukan model dan field yang akan diserialisasi
    class Meta:
        # Model yang digunakan untuk serializer ini
        model = Departments
        # Field yang akan diserialisasi
        fields = ("DepartmentId", "DepartmentName")


# Serializer untuk model Employees
class EmployeeSerializer(serializers.ModelSerializer):
    # Meta class untuk menentukan model dan field yang akan diserialisasi
    class Meta:
        # Model yang digunakan untuk serializer ini
        model = Employees
        # Field yang akan diserialisasi
        fields = (
            "EmployeeId",
            "EmployeeName",
            "DepartmentId",
            "DateOfJoining",
            "PhotoFileName",
        )
