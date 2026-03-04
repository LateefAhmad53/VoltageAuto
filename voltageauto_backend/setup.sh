#!/bin/bash

# VoltageAuto Setup Script for macOS/Linux

echo ""
echo "========================================"
echo "  VoltageAuto - Setup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

echo "[1/5] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo "[4/5] Setting up database..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error: Failed to run migrations"
    exit 1
fi

echo ""
echo "[5/5] Creating superuser account..."
echo "Please enter your superuser credentials:"
python manage.py createsuperuser

echo ""
echo "[BONUS] Populating sample products..."
python manage.py populate_products

echo ""
echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "Admin Panel: http://localhost:8000/admin"
echo "Website: http://localhost:8000"
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
