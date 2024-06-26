#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "belajar_django_api.settings")

    try:
        from django.core.management import execute_from_command_line
        from django.db import connections
        from django.db.utils import OperationalError

        if "runserver" in sys.argv and not os.environ.get("RUN_MAIN"):
            # Check database connection
            db_conn = connections["default"]
            try:
                db_conn.cursor()
                print("Database connection successful!")
            except OperationalError:
                print("Database connection failed")
                sys.exit(1)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
