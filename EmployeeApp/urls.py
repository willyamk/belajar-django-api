from django.urls import path
from . import views

# Definisikan URL pattern untuk API Employee dan Department
urlpatterns = [
    # URL untuk mengakses API Employee tanpa parameter ID
    path("employee/", views.employeeApi, name="employee_api"),
    # URL untuk mengakses API Employee dengan parameter ID
    path("employee/<str:id>/", views.employeeApi, name="employee_api"),
    # URL untuk mengakses API Department tanpa parameter ID
    path("department/", views.departmentApi, name="department_api"),
    # URL untuk mengakses API Department dengan parameter ID
    path("department/<int:id>/", views.departmentApi, name="department_api"),
]
