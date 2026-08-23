#pro-5 OOP Wrapper

class Person():
    def __init__(self):
        self.name = input("Enter a name: ")
        self.age = int(input("Enter a age: "))

    def __str__(self):
        return f"person created with name: {self.name} and age: {self.age}"
    def __del__(self):
        pass

class Employee():

    def __init__(self,salary=0):
        self._id = int(input("Enter Employee ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.__salary = float(input("Enter a salary: ")) 

    def getsalary(self):
        return self.__salary
    
    def getID(self):
        return self.__id
    
    def setvalue(self,salary):
        if(salary < 0):
            return "invalid input"
        else:
            self.__salary = salary

    def __str__(self):
        return f"employee Id {self._id} and name: {self.name} and age:{self.age} and salary: {self.__salary}"
    
    def __get__(self,other):
        return self.getsalary() > other.getSalary()
    
    def __eq__(self, other):
        return self.getSalary() == other.getSalary()
    
    def __lt__(self, other):
        return self.getSalary() < other.getSalary()
        
    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.department = input("Enter a Department: ")

    def __str__(self):
        return f" {super().__str__()} department: {self.depaertment}"
    
class Developer(Employee):

    def __init__(self):
        super().__init__()
        self.programminglang = input("Enter a single Programming Langague: ")

    def __str__(self):
        return f" {super().__str__()} and ProgrammingLangague{self.programminglang}"
    
People = []
while True:
    print("----Project OOP Project: Employee Management System----")
    print('''
          Choose an Operation:
          1.Create a Person
          2.Create an Employee
          3.Create a manager
          4.Create a Developer
          5.Show a Details 
          6.Compare Salaries
          7.Exit
        ''')
    
    inputChoice = int(input("Enter your Choice: "))
    
    match inputChoice:
        case 1:
            p1 = Person()
            People.append(p1)
            print(p1)
        
        case 2:
            emp1 = Employee()
            People.append(emp1)

        case 3:
            manager1 = Manager()
            People.append(manager1)
            print(manager1)
        
        case 4:
            developer1 = Developer()
            People.append(developer1)

        case 5:
            print('''
                 Choose details to show:
                  1.Person
                  2.Employee
                  3.Manager
                ''')
            Enterchoice = int(input("Enter your choice"))
            if Enterchoice==1:
                print(p1)
            elif Enterchoice==2:
                print(emp1)
            elif Enterchoice==3:
                print(manager1)
        case 6:
            print('Choose two employees to compare salaries')
            empID1 = input("Enter the first employee ID: ")
            empID2 = input("Enter the second employee ID: ")

            empA = None
            empB = None

            for i in People:
                if isinstance(i , Employee):
                    if i.getID() == empID1:
                        empA = i
                    elif i.getID() == empID2:
                        empB = i
            if emp1 and empB:
                if empA > empB:
                    print("Employee 1 has higher salary")
                elif empA < empB:
                    print("Employee 2 has higher salary")
                else:
                    print("Both hve equal salary")
            else:
                print("Employee is not found")

        case 7:
            break

        