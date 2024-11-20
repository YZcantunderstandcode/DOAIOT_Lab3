# Define a list of 6 dictionaries to store 6 employees' information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]


# This is extra function to demo how to sort the list of dictionaries with chosen key
def sort_employee_data(sortkey):
    templist = employee_data.copy()
    templist.sort(key=lambda x: x[sortkey])
    return templist


def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result


def calculate_average_salary():
    total = 0
    average = 0

    #add your implementation to calculate here
    for everyDictionary in employee_data:
        employeeSalary = everyDictionary["salary"]
        total += employeeSalary

    average = total / len(employee_data)
    average = round(average, 2)  # Rounded to 2 decimal points
    return average


def get_employees_by_dept(targetDept):
    result = []   # A empty list, to be filled in with selected dictionaries

    # Add your implementation from here
    for everyDictionary in employee_data:
        if everyDictionary["department"] == targetDept:
            result.append(everyDictionary)

    return result

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))


def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("5 - Display all records according to sort key")     # This is extra function added.
    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Uper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)


    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)


    elif option == '5':             # Extra function added to the menu.
        # Ask for the key to be used for sorting
        sortkey = input("Enter key for sorting = ")
        newlist = sort_employee_data(sortkey)
        display_records(newlist)


    elif option == 'Q':
        quit()

def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()