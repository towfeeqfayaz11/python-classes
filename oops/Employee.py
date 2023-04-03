class Employee:
    def __init__(self, firstName, lastName, email):
        # data members
        self.__fName = firstName
        self.__lName = lastName
        self.__email = email
    
    # these are member functions
    def __printFullName(self):
        print(f'{self.__fName} {self.__lName}')

    def getEmail(self):
        return self.__email



class FullTimeEmployee(Employee):
    def __init__(self, firstName, lastName, email, monthlySalary):
       super().__init__(firstName, lastName, email)
    #    self.fName = firstName
    #    self.lName = lastName
    #    self.email = email
       self.monthlySalary = monthlySalary
    
    def getSalary(self):
        return self.monthlySalary


class PartTimeEmployee(Employee):
    def __init__(self, firstName, lastName, email, hourlySalary):
       super().__init__(firstName, lastName, email)
    #    self.fName = firstName
    #    self.lName = lastName
    #    self.email = email
       self.hourlySalary = hourlySalary
    
    def getSalary(self):
        return self.hourlySalary


e1 = FullTimeEmployee("tom", "jack", "t.jack@gmal.com", 10000)
# e1.printFullName()
print(e1.getSalary())
print(e1.getEmail())

# print(e1.__fName)


# p1 = PartTimeEmployee("mohan", "raj", "m.raj@gmal.com", 15000)
# p1.printFullName()
# print(p1.getSalary())