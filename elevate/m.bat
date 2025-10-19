@echo off
cd /d "C:\Users\alawodddin\Desktop\Django\django\elevate"

:: Activate virtual environment if exists (.venv, venv, or env)
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist "env\Scripts\activate.bat" (
    call env\Scripts\activate.bat
) else (
    echo No virtual environment found. Using system Python.
)

echo ===========================
echo Running makemigrations...
echo ===========================
python manage.py makemigrations

echo ===========================
echo Applying migrations...
echo ===========================
python manage.py migrate

echo ===========================
echo Starting Django Server...
echo Press CTRL + C to stop server.
echo ===========================
python manage.py runserver

pause
