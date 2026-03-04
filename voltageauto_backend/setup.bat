@echo off
REM VoltageAuto Setup Script for Windows

echo.
echo ========================================
echo   VoltageAuto - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/5] Setting up database...
python manage.py migrate
if errorlevel 1 (
    echo Error: Failed to run migrations
    pause
    exit /b 1
)

echo.
echo [5/5] Creating superuser account...
echo Please enter your superuser credentials:
python manage.py createsuperuser

echo.
echo [BONUS] Populating sample products...
python manage.py populate_products

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Admin Panel: http://localhost:8000/admin
echo Website: http://localhost:8000
echo.
echo To start the server, run:
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
pause
