from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework.parsers import JSONParser
from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer


# Fungsi untuk menghasilkan respons JSON standar
def generate_response(
    status, status_code, message, path, data=None, errors=None, search=None
):
    response = {
        "status": status,
        "status_code": status_code,
        "message": message,
        "path": path,
        "timestamp": timezone.now().isoformat(),
    }
    if data is not None:
        response["datas"] = data
    if errors is not None:
        response["errors"] = errors
    if search is not None:
        response["search"] = search
    return response


# Fungsi untuk menangani permintaan GET
def handle_get_request(queryset, serializer_class, id, request):
    """
    Menghandle permintaan GET terhadap objek dari queryset.

    Args:
    - queryset: QuerySet Django yang digunakan untuk melakukan pencarian data.
    - serializer_class: Kelas serializer yang digunakan untuk mengubah objek Django model menjadi JSON.
    - id: ID dari objek yang ingin dicari atau 0 jika tidak ada ID spesifik yang diminta.
    - request: Objek permintaan HTTP dari client.

    Returns:
    - JsonResponse: JSON response berisi hasil dari permintaan GET, baik berhasil atau gagal.

    Explanation:
    - Jika `id` tidak sama dengan 0, mencoba untuk mendapatkan objek dari `queryset` dengan primary key `id`.
      Jika berhasil, objek di-serialize menggunakan `serializer_class` dan dikembalikan sebagai respons JSON sukses.
      Jika tidak ditemukan, respons JSON error dikembalikan dengan kode 404 dan pesan bahwa sumber daya yang diminta tidak ditemukan.
    - Jika `id` sama dengan 0, mencari berdasarkan `search` yang diperoleh dari parameter GET dalam `request`.
      Menentukan bidang filter berdasarkan jenis model `queryset` (Departments atau Employees).
      Jika ada hasil yang ditemukan, hasilnya di-serialize sebagai list menggunakan `serializer_class` dan dikembalikan sebagai respons JSON sukses.
      Jika tidak ada hasil yang ditemukan, respons JSON error dikembalikan dengan kode 404 dan pesan bahwa sumber daya yang diminta tidak ditemukan.
    """
    if id != 0:
        # Jika ID tidak sama dengan 0, mencoba untuk mengambil objek dengan ID tersebut
        try:
            instance = queryset.get(pk=id)
            serializer = serializer_class(instance)
            # Mengembalikan respon JSON dengan data yang berhasil diambil
            return JsonResponse(
                generate_response(
                    "success",
                    200,
                    f"Data with ID = '{id}' has been retrieved successfully",
                    request.path,
                    serializer.data,
                )
            )
        except queryset.model.DoesNotExist:
            # Mengembalikan respon JSON bahwa objek tidak ditemukan
            return JsonResponse(
                generate_response(
                    "error",
                    404,
                    "The requested resource was not found",
                    request.path,
                    errors={
                        "code": "RESOURCE_NOT_FOUND",
                        "message": f"The item with ID = '{id}' does not exist in our records.",
                    },
                )
            )
    else:
        # Jika ID adalah 0, melakukan pencarian berdasarkan query
        search = request.GET.get("search", None)
        # Menentukan field filter berdasarkan jenis model
        filter_field = (
            "DepartmentName__icontains"
            if queryset.model == Departments
            else "EmployeeName__icontains"
        )
        # Melakukan filter atau mengambil semua item jika tidak ada query
        items = (
            queryset.filter(**{filter_field: search})
            if search
            else queryset.all()
        )
        # Jika ditemukan item, mengembalikan respon JSON dengan data yang berhasil diambil
        if items.count() > 0:
            serializer = serializer_class(items, many=True)
            return JsonResponse(
                generate_response(
                    "success",
                    200,
                    f"Data has been retrieved successfully",
                    request.path,
                    serializer.data,
                    search=search,
                )
            )
        else:
            # Jika tidak ditemukan item, mengembalikan respon JSON bahwa tidak ada record yang ditemukan
            return JsonResponse(
                generate_response(
                    "error",
                    404,
                    "The requested resource was not found",
                    request.path,
                    errors={
                        "code": "RESOURCE_NOT_FOUND",
                        "message": f"No records found.",
                    },
                    search=search,
                )
            )


# Fungsi untuk menangani permintaan POST
def handle_post_request(serializer_class, request):
    """
    Menghandle permintaan POST untuk membuat data baru.

    Args:
    - serializer_class: Kelas serializer yang digunakan untuk mengubah data dari permintaan HTTP menjadi objek Django model.
    - request: Objek permintaan HTTP POST dari client.

    Returns:
    - JsonResponse: JSON response berisi hasil dari permintaan POST, baik berhasil atau gagal.

    Explanation:
    - Mengurai data dari permintaan HTTP POST menggunakan JSONParser.
    - Memvalidasi data menggunakan `serializer_class`. Jika data valid, menyimpan data baru menggunakan `serializer.save()`.
      Mengembalikan respons JSON sukses dengan kode 201 dan data yang telah disimpan.
    - Jika data tidak valid, mengembalikan respons JSON error dengan kode 400 dan pesan bahwa permintaan tidak valid,
      serta menampilkan detail kesalahan dari serializer.
    """
    data = JSONParser().parse(request)
    serializer = serializer_class(data=data)

    if serializer.is_valid():
        serializer.save()
        # Mengembalikan respon sukses jika data berhasil disimpan
        return JsonResponse(
            generate_response(
                "success",
                201,
                "Data has been created successfully",
                request.path,
                serializer.data,
            ),
            status=201,
        )
    else:
        # Mengembalikan respon dengan status 400 dan pesan kesalahan jika ada kesalahan validasi
        return JsonResponse(
            generate_response(
                "error",
                400,
                "The request was invalid or cannot be served",
                request.path,
                errors={"code": "BAD_REQUEST", "message": serializer.errors},
            ),
            status=400,
        )


# Fungsi untuk menangani permintaan PATCH
def handle_patch_request(queryset, serializer_class, id, request):
    """
    Menghandle permintaan PATCH untuk memperbarui data yang ada.

    Args:
    - queryset: QuerySet Django yang digunakan untuk melakukan pencarian data.
    - serializer_class: Kelas serializer yang digunakan untuk mengubah data dari permintaan HTTP menjadi objek Django model.
    - id: ID dari objek yang ingin diperbarui.
    - request: Objek permintaan HTTP PATCH dari client.

    Returns:
    - JsonResponse: JSON response berisi hasil dari permintaan PATCH, baik berhasil atau gagal.

    Explanation:
    - Mengurai data dari permintaan HTTP PATCH menggunakan JSONParser.
    - Mencoba untuk mendapatkan objek dari `queryset` dengan primary key `id`.
      Jika objek ditemukan, memperbarui objek menggunakan data yang diurai menggunakan `serializer_class`.
      Mengembalikan respons JSON sukses dengan kode 200 dan data yang telah diperbarui.
    - Jika objek tidak ditemukan, mengembalikan respons JSON error dengan kode 404 dan pesan bahwa sumber daya yang diminta tidak ditemukan.
    - Jika data tidak valid saat memperbarui, mengembalikan respons JSON error dengan kode 400 dan menampilkan detail kesalahan dari serializer.
    """
    data = JSONParser().parse(request)

    try:
        # Mencoba untuk mengambil objek dari database berdasarkan ID
        instance = queryset.get(pk=id)
        serializer = serializer_class(instance, data=data)

        if serializer.is_valid():
            # Jika data valid, menyimpan data yang diperbarui
            serializer.save()
            return JsonResponse(
                generate_response(
                    "success",
                    200,
                    "Data has been updated successfully",
                    request.path,
                    serializer.data,
                )
            )
        else:
            # Jika ada kesalahan validasi, mengembalikan respon dengan status 400 dan pesan kesalahan
            return JsonResponse(
                generate_response(
                    "error",
                    400,
                    "The request was invalid or cannot be served",
                    request.path,
                    errors={"code": "BAD_REQUEST", "message": serializer.errors},
                ),
                status=400,
            )

    except queryset.model.DoesNotExist:
        # Jika objek tidak ditemukan, mengembalikan respon dengan status 404
        return JsonResponse(
            generate_response(
                "error",
                404,
                "The requested resource was not found",
                request.path,
                errors={
                    "code": "RESOURCE_NOT_FOUND",
                    "message": f"The item with ID = '{id}' does not exist in our records.",
                },
            ),
            status=404,
        )


# Fungsi untuk menangani permintaan DELETE
def handle_delete_request(queryset, serializer_class, id, request):
    """
    Menghandle permintaan DELETE untuk menghapus data.

    Args:
    - queryset: QuerySet Django yang digunakan untuk melakukan pencarian data.
    - serializer_class: Kelas serializer yang digunakan untuk mengubah objek Django model menjadi JSON.
    - id: ID dari objek yang ingin dihapus atau 0 jika ingin menghapus semua data.
    - request: Objek permintaan HTTP DELETE dari client.

    Returns:
    - JsonResponse: JSON response berisi hasil dari permintaan DELETE, baik berhasil atau gagal.

    Explanation:
    - Jika `id` sama dengan 0, menghapus semua data dalam `queryset` jika ada.
      Mengembalikan respons JSON sukses dengan kode 204 dan data yang telah dihapus.
      Jika tidak ada data untuk dihapus, mengembalikan respons JSON error dengan kode 404 dan pesan bahwa tidak ada catatan yang ditemukan.
    - Jika `id` tidak sama dengan 0, mencoba untuk mendapatkan objek dari `queryset` dengan primary key `id`.
      Jika objek ditemukan, menghapus objek tersebut dan mengembalikan respons JSON sukses dengan kode 204 serta data objek yang dihapus.
      Jika objek tidak ditemukan, mengembalikan respons JSON error dengan kode 404 dan pesan bahwa sumber daya yang diminta tidak ditemukan.
    """
    try:
        if id == 0:
            # Jika ID adalah 0, menghapus semua data dalam queryset
            if queryset.count() > 0:
                deleted_items = list(queryset.all().values())
                queryset.all().delete()
                return JsonResponse(
                    generate_response(
                        "success",
                        204,
                        "All data has been deleted successfully",
                        request.path,
                        deleted_items,
                    )
                )
            else:
                # Jika queryset kosong, mengembalikan respon dengan status 404
                return JsonResponse(
                    generate_response(
                        "error",
                        404,
                        "No data found to delete",
                        request.path,
                        errors={
                            "code": "RESOURCE_NOT_FOUND",
                            "message": "No records found.",
                        },
                    ),
                    status=404,
                )
        else:
            # Jika ID tidak sama dengan 0, mencoba untuk mengambil dan menghapus objek dengan ID tersebut
            instance = queryset.get(pk=id)
            serializer = serializer_class(instance)
            deleted_item_data = serializer.data
            instance.delete()
            return JsonResponse(
                generate_response(
                    "success",
                    204,
                    f"Data with ID = '{id}' has been deleted successfully",
                    request.path,
                    deleted_item_data,
                )
            )
    except queryset.model.DoesNotExist:
        # Jika objek dengan ID yang diminta tidak ditemukan, mengembalikan respon dengan status 404
        return JsonResponse(
            generate_response(
                "error",
                404,
                "The requested resource was not found",
                request.path,
                errors={
                    "code": "RESOURCE_NOT_FOUND",
                    "message": f"The item with ID = '{id}' does not exist in our records.",
                },
            ),
            status=404,
        )


# Fungsi untuk menangani permintaan API berdasarkan metode HTTP
def handle_api_request(queryset, serializer_class, id, request):
    try:
        if request.method == "GET":
            return handle_get_request(queryset, serializer_class, id, request)
        elif request.method == "POST":
            return handle_post_request(serializer_class, request)
        elif request.method == "PATCH":
            return handle_patch_request(queryset, serializer_class, id, request)
        elif request.method == "DELETE":
            return handle_delete_request(queryset, serializer_class, id, request)
        else:
            return JsonResponse(
                generate_response("error", 405, "Method not allowed", request.path),
                status=405,
            )
    except Exception as e:
        return JsonResponse(
            generate_response(
                "error",
                500,
                "Internal Server Error",
                request.path,
                errors={"code": "INTERNAL_SERVER_ERROR", "message": str(e)},
            ),
            status=500,
        )


# View untuk menangani permintaan API terkait Employees
@csrf_exempt
def employeeApi(request, id=0):
    return handle_api_request(Employees.objects, EmployeeSerializer, id, request)


# View untuk menangani permintaan API terkait Departments
@csrf_exempt
def departmentApi(request, id=0):
    return handle_api_request(Departments.objects, DepartmentSerializer, id, request)
