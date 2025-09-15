
# Python Generators – Database Seeder

This script sets up a MySQL database **ALX_prodev** with a `user_data` table and populates it with sample data from `user_data.csv`.

### Files:
- `seed.py` – Contains database setup and seeding functions.
- `0-main.py` – Test script that uses `seed.py` to:
  - Create database
  - Create table
  - Insert data
  - Print sample rows

### Setup Instructions:
1. Install dependencies:
   ```bash
   pip install mysql-connector-python
