class Department:
    def __init__(self,name):
        self.name=name

    def display_info(self):
        return f"Department : {self.name}"

class University:
    def __init__(self,name):
        self.name=name
        self.department=[]  # A list to hold department objects

    def add_department(self, department):
        self.department.append(department)

    def display_department(self):
        print(f"Departments in {self.name} University:")
        for department in self.department:
            print(department.display_info())

# Create Department Objects
department1= Department("Computer Science")
department2= Department("Electrical Engineering")
department3= Department("Mechanical Engineering")

#create university objects
university=University("Tech University")

#Add departments to the university
university.add_department(department1)
university.add_department(department2)
university.add_department(department3)

# Display departments in the university

university.display_department()
