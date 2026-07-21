import csv
with open ("csv/employees.csv", newline = "") as file:
    data = csv.reader (file)
    list_all = [row for row in data]

employee_names = [row[1] + " " + row[2] for row in list_all[1:]]
    
e_names = [name for name in employee_names if "e" in name]


print(employee_names)
print(e_names)
