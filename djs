#!/bin/bash

# Path ke file manage.py dari proyek Django
MANAGE_PY="./manage.py"

# Daftar perintah yang didukung beserta nilai default (1)
declare -A SUPPORTED_COMMANDS=(
    [runserver]=1
    [migrate]=1
    [makemigrations]=1
    [createsuperuser]=1
    [collectstatic]=1
    [test]=1
    [startapp]=1
)

# Memeriksa apakah perintah yang diberikan ada dalam daftar perintah yang didukung
if [ ${SUPPORTED_COMMANDS[$1]+_} ]; then
    # Jika perintah adalah "startapp", menjalankan perintah dengan argumen tambahan
    if [ "$1" == "startapp" ]; then
        python "$MANAGE_PY" startapp "${@:2}"
    else
        # Menjalankan perintah menggunakan file manage.py
        python "$MANAGE_PY" "$@"
    fi
else
    # Jika perintah tidak dikenali, cetak pesan error
    echo "Command not recognized."
fi
