import csv
import random
import string

def generate_random_string(length=10):
    """Generates a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_csv(filename, rows, columns):
    """Generates a CSV file with random content."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow([f'Column_{i+1}' for i in range(columns)])
        # Write rows with random data
        for _ in range(rows):
            row = [generate_random_string() for _ in range(columns)]
            writer.writerow(row)

# Define parameters
rows = 1000000  # Adjust this number based on your needs
columns = 10    # Number of columns

# Generate the CSV file
generate_csv('100mb_file.csv', rows, columns)
