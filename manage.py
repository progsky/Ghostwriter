#!/usr/bin/env python

# Standard Libraries
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line  # noqa isort:skip
    except ImportError as e:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        if e.name == "django":
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    # This allows easy placement of apps within the interior ghostwriter directory
    sys.path.append(os.path.join(os.path.dirname(__file__), "ghostwriter"))

    execute_from_command_line(sys.argv)
