#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    try:
        import orderable
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from django.core.management import execute_from_command_line
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
    execute_from_command_line(sys.argv)
