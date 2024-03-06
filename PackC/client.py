import sys
sys.path.append("C:/Users/apple/PycharmProjects/Practice/PackA")
sys.path.append("C:/Users/apple/PycharmProjects/Practice/PackB")

from emp import *
obj = Employee(101,"John",20000)
obj.displayemp()

from stu import *
obj = Student(101,"Scott",'A')
obj.displaystu()