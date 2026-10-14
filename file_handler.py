"""
This module saves and loads dog-care records using CSV files.
"""

import csv
import os

FILE_NAME = "dog_records.csv"
FIELDNAMES = ["name", "age", "feeding", "notes", "date_recorded"]


def save_dog_record(record):
    """Save a dog-care record to a CSV file."""
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()

        writer.writerow(record)


def load_dog_records():
    """Load saved dog-care records from the CSV file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))

    for record in records:
        record["age"] = int(record["age"])

    return records
