"""
This module creates and formats dog-care records.
"""

def create_dog_record(name, age, feeding, notes, date_recorded):
    """Validate and organize dog-care information."""
    if not name:
        raise ValueError("The dog's name cannot be blank.")
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return {
        "name": name,
        "age": age,
        "feeding": feeding or "No feeding instructions provided",
        "notes": notes or "No additional notes",
        "date_recorded": date_recorded
    }


def format_dog_record(record):
    """Format a dog-care record for display."""
    return (
        f"Name: {record['name']}\n"
        f"Age: {record['age']} years\n"
        f"Feeding: {record['feeding']}\n"
        f"Notes: {record['notes']}\n"
        f"Date recorded: {record['date_recorded']}\n"
        "------------------"
    )
