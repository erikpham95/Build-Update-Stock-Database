#!/bin/bash

# Navigate to the directory containing the Python script
cd /home/erik/Downloads/buildding_and_updating_stock_database

# Activate the virtual environment containing the required Python packages
source venv3.10/bin/activate

# Update the PostgreSQL table with the new data
/bin/python3 "/home/erik/Downloads/buildding_and_updating_stock_database/python_update_db.py"
