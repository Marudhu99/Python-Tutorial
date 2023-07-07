class User:
    def __init__(self, uname, pwd):
        self.username = uname
        self.password = pwd

    def login(self):
        if self.username == "Marudhu" and self.password == 221707384:
            return "login successfully"
        else:
            return "login failed"

class Student(User): # Student class inherits User class
    fees = 15000
    def __init__(self,uname,pwd,year):
        super().__init__(uname,pwd)
        self.year = year 

    def feesDetails(self):
        if self.login() == "login successfully" and self.year == 2020:
            print("Login successfully")
            print("Fees:",Student.fees)
        else:
            print("access denied")

uname = input("Enter your username:")     
pwd = int(input("Enter your pwd:"))
year = int(input("Enter your year:"))
student = Student(uname,pwd,year)
student.feesDetails()
        