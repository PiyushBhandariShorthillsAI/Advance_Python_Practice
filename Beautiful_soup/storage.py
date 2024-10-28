# storage.py
import csv

def save_to_csv(data, filename="output.csv"):
    """Saves data to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(data)
