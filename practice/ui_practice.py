import csv

# Step 1: Prepare Data
data = [
    {"Number": "1234567890"},
    {"Number": "9876543210"},
]

print(type(data))

# Step 2: Open CSV File
with open("contacts.csv", mode="w", newline="", encoding="utf-8") as file:
    # Step 3: Create DictWriter with Fieldnames
    writer = csv.DictWriter(file, fieldnames=["Number"])

    # Step 4: Write Header (Fieldnames) to File
    writer.writeheader()

    # Step 5: Write Rows of Data
    writer.writerows(data)

print("CSV file created successfully!")
