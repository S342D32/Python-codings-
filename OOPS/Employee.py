class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role is:", self.role)
        print("Department is:", self.department)
        print("Salary is:", self.salary)
        print("Name is:", self.name)  # This will throw an error if not properly initialized
        print("Age is:", self.age)    # This will throw an error if not properly initialized

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)

# Creating an instance of Engineer and displaying details
e1 = Engineer("Swati", 23, "Developer", "Software", 40000)
e1.showDetails()
