
print("\n\n----------MY FIRST CRUD SYSTEM----------\n\n")

class Employee:
    id_count=0
    total_empl=0
    def __init__(self,name,dept,salary):
        self.id = Employee.id_count
        self.name = name
        self.dept = dept
        self.salary = salary

        Employee.id_count +=1
        Employee.total_empl +=1

    def show_info(self):
        print(f"ID: {self.id}| Name: {self.name}| Department: {self.dept}| Salary: {self.salary}")

employees = []
 
#taking input for employee

def creat_empl ():
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    emp = Employee(name,dept,salary)
    employees.append(emp)

    print("\nEmployee Created")

#read the data of employee

def read_empl ():
    if not employees:
        print("\n\nNo Employee created yet\n\n")
        return 
    print("\n\nAll Employees:\n\n")
    for emp in employees:
        emp.show_info()

#updatading employee

def update_empl ():
    emp_id = int(input("Enter the Employee ID you have to update "))  
    for emp in employees:
        if emp.id == emp_id:
            print("Leave blank and press Enter if no change.")
            name = input("Enter New Name: ") or emp.name
            dept = input("Enter New Department: ") or emp.dept
            salary_input = input("Enter New Salary; ")
            salary = int(salary_input) if salary_input else emp.salary

            emp.name = name
            emp.dept = dept
            emp.salary = salary


            print("Employee Updated.")
            return
    print("\n\nEmployee not found.\n\n")

# deleting employee

def delete_empl():
    emp_id = int(input("Enter employee's ID to delete "))
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            print("Employee Deleted")
            return
    print("\n\nEmployee not found\n\n")

# CLI response function

def show_menu():
    # print("\n\n----------My First Crud System----------\n\n")
    print("1.Create Employee")
    print("2.Read All Employees")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.Total Employee")
    print("6.Exit")
while True:
    show_menu()
    choise = int(input("\nSelect Option:  \n"))

    if choise == 1:
        creat_empl()
    elif choise == 2:
        read_empl()
    elif choise == 3:
        update_empl()
    elif choise == 4:
        delete_empl()           
    elif choise == 5:
        if not employees:
            print("\n\nNo Employee created yet\n\n")
        else:
            print(f"Total Employees in Crud: {Employee.total_empl}")

    elif choise == 6:
        print("\n\nGOOD BYE.\n\n")
        break
    else:
        print("\n\nWrong Input.\n\n")    
