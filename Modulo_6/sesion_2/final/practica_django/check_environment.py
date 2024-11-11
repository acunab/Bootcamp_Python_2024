import sys
import django
import os

def check_python_version():
    print("Python version:", sys.version)

def check_django_version():
    try:
        print("Django version:", django.get_version())
    except ImportError:
        print("Django is not installed. Please install Django with `pip3 install django`.")

def check_virtual_environment():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Virtual environment detected.")
    else:
        print("No virtual environment detected. It's recommended to use a virtual environment for Django projects.")

def check_project_structure():
    project_files = ['manage.py', 'site_django/settings.py']
    for file in project_files:
        if not os.path.isfile(file):
            print(f"Warning: {file} not found. Make sure you're in the project root directory.")
        else:
            print(f"{file} found.")

def main():
    print("Checking Python environment configuration...\n")
    check_python_version()
    check_django_version()
    check_virtual_environment()
    check_project_structure()

if __name__ == "__main__":
    main()