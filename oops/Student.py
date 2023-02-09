class Student:

    def __init__(self, name, roll, reg):
        self.name = name
        self.rollno = roll
        self.regno = reg

    def getRollno(self):
        return self.rollno

    def getName(self):
        return self.name

    def getRegno(self):
        return self.regno


studentList  = []

s1 = Student("saravanan", 101, 440101)    

print(s1.name)
s1.name ="ascasa"

print(s1.getName())

# s1.name="xyz"
# # print(s1.getRegno())
# studentList.append(s1)

# m1 = Student("muthu", 102, 440102)
# # print(m1.getRegno())
# studentList.append(m1)


# for stud in studentList:
#     print(stud.getName())

