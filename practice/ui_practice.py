import csv 

with open("employees.csv", "r") as file:
    csv_file = csv.DictReader(file)
    
    fieldnames = csv_file.fieldnames

    csv_data = []
    for data in csv_file:
        csv_data.append(data)

    
with open("copy_employees.csv", "w",newline="") as file:
    write_data = csv.DictWriter(file,fieldnames=fieldnames)
    # write_data.writer(csv_data)
    write_data.writeheader()
    write_data.writerows(csv_data)

            

