Scan Planner
============

Scan Planner for Common Data Lakehouse Table Formats


Setup
-----

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


Usage
-----

    source venv/bin/activate
    ./hive DATABASE_NAME TABLE_NAME
    ./hudi DATABASE_NAME TABLE_NAME
    ./iceberg DATABASE_NAME TABLE_NAME
    ./delta DATABASE_NAME TABLE_NAME
