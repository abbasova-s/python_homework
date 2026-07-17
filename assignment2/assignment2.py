import csv
import traceback

#Task 2: Read a CSV File
def read_employees():
    dict1 = {}
    list1 = []
    try:
        with open ('../csv/employees.csv', newline = "") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    dict1["fields"] = row
                else:
                    list1.append(row)
            dict1["rows"] = list1
            return(dict1)
        
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)


#Task 3: Find the Column Index
def column_index(string):
    return(employees["fields"].index(string))

employee_id_column = column_index("employee_id")
print(employee_id_column)


#Task 4: Find the Employee First Name
def first_name (num):
    index = column_index('first_name')
    row = employees.get("rows")[num]
    return (row[index])

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index('last_name')])
    return employees["rows"]

print(sort_by_last_name())

#Task 8: Create a dict for an Employee
def employee_dict(row):
    dict2 = {}
    for i in range(len(row)):
        key = employees["fields"][i]
        value = row[i]
        if key == "employee_id":
            continue
        else:
            dict2[key] = value
    
    return dict2

print(employee_dict(['1', 'Cindy', 'Wade', '+222 656-486-3727']))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    dict = {}

    for row in employees["rows"]:
        value = employee_dict(row)
        key = row[employee_id_column]
    
        dict[key] = value
    return dict

print(all_employees_dict())

#Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())


#Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Bubbles")
print(custom_module.secret)


#Task 12: Read minutes1.csv and minutes2.csv
def read_file(file):
    minutes_dict = {}
    rows = []
    try:
        with open (file, newline = "") as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader):
                if i == 0:
                    minutes_dict["fields"] = row
                else:
                    tuple_minutes = tuple(row)
                    rows.append(tuple_minutes)
            minutes_dict["rows"] = rows
            return minutes_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

def read_minutes():
    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(read_minutes())


#Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    result = set1.union(set2)
    return result

minutes_set = create_minutes_set()
print(minutes_set)


#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    list1 = list(minutes_set)
    result = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list1))
    return result

minutes_list = create_minutes_list()
print(minutes_list) 


#Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    result = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_list))

    with open ("./minutes.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(minutes1["fields"])

        for row in result:
            writer.writerow(row)

    return result

write_sorted_list()