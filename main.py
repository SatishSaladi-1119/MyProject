# def fun():
#     n = int(input("Please give a number: "))
#     print(f"Before reverse your number is :", n )
#     # reverse = 0
#     # while n!=0:
#     #     reverse = reverse * 10 + n%10
#     #     n = (n//10)
#     # print(f"After reverse :", reverse)
#     rev = (str(n)[::-1])
#     print(rev)
# fun()

# x = 13
# y = 5
# print(x%y)

# a = input("Enter the numbers: ")
# b = a[::-1]
# if a == b:
#     print("palindrome")
# else:
#     print("not palindrome")

# import array as arr
# a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
# print(a.pop())
# print(a.pop(3))
# a.remove(1.1)
# print(a)

# import os
# os.remove("reverse.py")

# print(dir(str))
# a = {1,2,3,4}
# b = {1,3,4,5}
# stg='abcd'
# print(stg.capitalize())
# list1 = [4,0,2,1,3]
# for i in range(len(list1)-1):
#     for i in range(len(list1) - 1):
#         if list1[i] > list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
# print(list1)
# new = set(list1)
# print(list(new))
# list1.sort()
# print(list1)
# import keyword
# print(keyword.kwlist)
# x,y =1,2
# print(f"the x,y values are before swapping:",x,y)
# y,x = x,y
# print(f"the x,y values are after swapping:",x,y)
# def fab():
#     a = 0
#     b = 1
#     for i in range(0,5):
#         c = a+b
#         a = b
#         b = c
#         print(c, end=' ')
# fab()
# a = 0
# b = 1
# for i in range(5):
#     c = a+b
#     a += b
#     print(c)
# def tree_pattern():
#     for i in range(5):
#         for k in range(5-i):
#             print('',end = ' ')
#         for j in range(i):
#             print('*',end = ' ')
#         print(end = '\n')
# tree_pattern()
# list1 = ['satish','geetha','karthika','saladi']
# index = list1.index('saladi')
# item = list1.pop(index)
# result = list1.insert(0,item)
# print(list1)
# for i in range(6):
#     for j in range(i):
#         # i = 1
#         j += 1
#         print(j, end = ' ')
#     print()
# def sort():
#     sorting = [3,5,9,8,2,1]
#     for i in range(0,len(sorting)-1):
#         for i in range(0,len(sorting)-1):
#             if sorting[i] > sorting[i+1]:
#                 sorting[i],sorting[i+1] = sorting[i+1],sorting[i]
#     print(sorting)
# sort()
# sorting = [3,5,9,8,2,1]
# sort = set(sorting)
# print(list(sort))
# print(True+1)
# print(True*5)
# print(False+1)
# print(False*1)
# name = 'satish'
# age = 30
# sal = 100500.00
# print(f"the name is {name}, his age is {age} and earning salary {sal}")
# age = int(input("Enter the Voter Age: "))
# if age >= 18:
#     print("The voter is eligible for Vote")
# else:
#     print("Not Eligible, Age should be 18 or 18 above")
#
# day = int(input("enter the day:"))
# if day == 1:
#     print('Sunday')
# elif day == 2:
#     print("Monday")
# elif day == 3:
#     print("Tuesday")
# elif day == 4:
#     print("Wednesday")
# elif day == 5:
#     print("Thursday")
# elif day == 6:
#     print("Friday")
# elif day == 7:
#     print("Saturday")
# else:
#     print("invalid")

# number = int(input("Enter the number:"))
# if number >= 0:
#     print("Positive Number")
# else:
#     print("Negative Number")

# largest of two numbers
# a = 40
# b = 20
# if a > b:
#     print('largest number')
# else:
#     print("not")
# a = 'satish'
# print(list(range(0,len(a))))
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
# print("done!!!")

# for i in range(-10,0):
#     print(i, end=' ')
# for i in range(1,20):
#     if i == 5:
#         continue
#     print(i)
# l1 = [1,2,3,3,3,34,5,6,6,7,7,7,1]
# d = {}
# for i in l1:
#     # print(i)
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)
# a = "DevLopMent"  # ans is "D evL opM ent"
# b = ""
# for i in a:
#     if i.isupper():
#         b = "{} ".format(b+i)
#     else:
#         b = b+i
# print(b)

# l1 = ['satish','ramana','adi','rithvika']
# s = 'karthis' # out put should come this letters order
# l2 = []
# for i in s:
#     for j in l1:
#         if j.startswith(i):
#             l2.append(j)
# print(l2)
# s = 'karthika shree'
# l = []
# for i in s:
#     l.insert(0,i)
# print(l)
#
# l = ''
# for i in range(len(s),0,-1):
#     l += s[i-1]
# print(l)

# a = [1,2,3]
# b = [2,3,4]
# c = [3,4,5]
# s = [x for x in a if x in b and x in c]
# print(s)
# c = [[x for x in a if x not in b],[x for x in b if x not in a],
#      [x for x in c if x not in a and x not in b]]
# print(c)
# Name = input("Enter the Name: ")
# # if Name:
# #     name = Name
# # else:
# #     name = 'N/A'
# name = Name or 'N/A'
# print(name)
# string = 'satish'
# reverse = ''
# for i in string:
#     reverse = i + reverse
# print(reverse)
# list1 = ["a","b","c"]
# list2 = [1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)
# mytuple = ('apple',100,200)
# mylist = list(mytuple)
# mylist[0] = 300
# mytuple = tuple(mylist)
# print(mytuple)
# mytuple = (100,200,300)
# print(mytuple)
# del mytuple
# print(mytuple)
# myset = {'apple','banana'}
# print(myset)
# myset.add('orange')
# print(myset)
# myset.update(["cherry",'kiwi'])
# print(myset)
# set1 = {1,2,3}
# set2 = {4,5,6}
# print(set1.union(set2))
# set1.update(set2)
# print(set1)
# mydic = {
#     "brand" : "TaTa",
#     "Model"  : "Harrier",
#     "year" : 2023
# }
# print(mydic)
# print(mydic.get('brand'))
# for i in mydic.keys():
#     print(i)
# for i in mydic.values():
#     print(i)
# for i in mydic.items():
#     print(i)
# for i,j in mydic.items():
#     print(i,j)
# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)
# fib(100)
# s = 'karthika shree'
# l = ''
# for i in s:
#     l = i+l
# print
# def read():
#     # with open("C:\\Users\\apple\\Downloads\\satish.txt",'r') as f:
#     #     print(f.read())
#     with open("C:\\Users\\apple\\Downloads\\satish.txt",'a') as f:
#         f.write("\nsankar \nsrinu")
#     with open("C:\\Users\\apple\\Downloads\\satish.txt",'r') as f:
#         print(f.read())
# read()
# lst = [2,0,8,0,4,]
# for i in lst:
#     if i == 0:
#        lst.remove(i)
#        lst.append(i)
# print(lst)
# lst1 = [2,4,5,1]
# lst2 = [2,4,5,1,3,4]
# lst3 = lst2[len(lst1):]
# print(lst3)
# def cycle(n):
#         lst = [2,4,5,1]
#         for i in lst:
#             item = lst.index(1)
#             j = lst.pop(item)
#             k = lst.insert(0,j)
#         print(lst)
# cycle(1)
# lst = [1,2,3,4,5,6,7,8,9]
# evens = list(filter(lambda n : n%2 == 0,lst))
# doubles = list(map(lambda n : n*2,evens))
# print(evens)
# print(doubles)
# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# e1 = Emp(101,'Satish','13LPA')
# e1.display()
# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#     def __str__(self):
#         return (self.ename)
# e1 = Emp(101,"Satish Saladi",'13LPA')
# print(e1)
# class A:
#     a,b = 10,20
#     def add(self):
#         print(self.a + self.b)
# class B(A):
#     x,y = 20,10
#     def sub(self):
#         print(self.x - self.y)
# obj = B()
# obj.add()
# obj.sub()

# for i in range(65, 70):
#     for j in range(65, i + 1):
#         print(chr(j), end="")
#     print()
#
# for i in range(65, 70):
#     for j in range(65, i + 1):
#         print(chr(i), end="")
#     print()
#
# for i in range(65, 70):
#     k = i
#     for j in range(65, i + 1):
#         print(chr(k), end="")
#         k = k + 1
#     print()
#
# str = "SATISH"
# for i in range(0, 6):
#     for j in range(0, i + 1):
#         print(str[j], end="")
#     print()
#
# for i in range(65, 70):
#     for j in range(i, 64, -1):
#         print(chr(j), end="")
#     print()
# class A():
#     def tree(self):
#         for i in range(65,70):
#             k = i
#             for j in range(65,i+1):
#                 print(chr(k),end='')
#                 k+=1
#             print()
# class B(A):
#     def tree2(self):
#         for i in range(65,70):
#             # k = i
#             for j in range(65,i+1):
#                 print(chr(j),end='')
#                 # k+=1
#             print()
# class C(B):
#     def tree3(self):
#         for i in range(65,71):
#             # k = i
#             for j in range(65,i+1):
#                 print(chr(i),end='')
#                 # k+=1
#             print()
# obj = C()
# obj.tree()
# obj.tree2()
# obj.tree3()
# class A():
#     def m1(self):
#         print("This is m1 method from A")
# class B(A):
#     def m1(self):
#         print("This is m1 method from B")
#         super().m1()
# obj = B()
# obj.m1()
# class Bank():
#     def rateOfInterest(self):
#         return 0
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
# obj = XBank()
# print(obj.rateOfInterest())
# obj = YBank()
# print(obj.rateOfInterest())
# class A:
#     name = "Saladi"
# class B(A):
#     name = "Satish"
#     def test(self):
#         print(super().name)
# obj = B()
# print(obj.name)
# obj.test()
# print("Hello Satish")
# print("Hello Geetha")
# try:
#     print(Saladi)
# except:
#     print("Syntax Error")
# try:
#     num1 = int(input("Enter the Value: "))
#     num2 = int(input("Enter the Value: "))
#     result = num1/num2
#     print(f"Result is:{result}")
# except ZeroDivisionError:
#     print("Thrown ZeroDevision exception...")
# except SyntaxError:
#     print("Thrown SyntaxError exception...")
# except:
#     print("Exception handled.....")
# else:
#     print("No exception occured...")
# finally:
#     print("always execute...")
# def age(num):
#     if num<0:
#         raise ValueError("Only Integers are allowed")
#     if num%2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# num = 10
# # num = int(input("Enter the age: "))
# try:
#     age(num)
# except ValueError:
#     print("ValueError exception handled")

# digits = [1,2,3,4,5]
# index = digits.index(5)
# remove = digits.pop(index)
# item = digits.insert(0,remove)
# print(digits)
# for i in range(5):
#     digits = digits[-1::] + digits[:-1]
#     print(digits)
# list = []

# def create_list(start, count):
#     mylist = []
#     for i in range(start, start + count):
#         mylist.append(i)
#     return mylist
# the_list = create_list(0, 8)
# print(the_list)
# def fun(n):
#     ls = [1,2,3,4,5]
#     for i in range(n):
#         ls = ls[-1::] + ls[:-1]
#         print(ls)
# fun(6)
# def pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print('*',end =' ')
#         print()
# pattern(5)
# list1 = ['satish','geetha','karthika','saladi']
# list1 = list1[-1::]+list1[:-1]
# print(list1)
# for i in range(5):
#     for k in range(5-i):
#         print('',end = ' ')
#     for j in range(i):
#         print('*',end=' ')
#     print(end='\n')
# def pat(n):
#     for i in range(n):
#         for j in range(i):
#             print('',end=' ')
#         for k in range(n-i):
#             print('*',end = ' ')
#         print(end='\n')
# pat(6)
# l = [3,5,9,8,2,1]
# for i in range(0,len(l)-1):
#     for i in range(0,len(l)-1):
#         if l[i] > l[i+1]:
#             l[i],l[i+1] = l[i+1],l[i]
# print(l)
# s = 'satish'
# a = ''
# for i in s:
#     a = i+a
# print(a)
# l = []
# for i in s:
#     l.insert(0,i)
# print(l)
# list1 = ["a","b","c"]
# list2 = [1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)
set1 = {1,2,3}
set2 = {4,5,6}
# print(set1.union(set2))
# set1.update(set2)
# print(set1)
# a = "DevLopMent"
# b =''
# for i in a:
#     if i.isupper():
#         b = '{} '.format(b+i)
#     else:
#         b = b+i
# print(b)
# l = ['geetha','satish','karthika','saladis']
# s = 'sgk'
# m = []
# for i in s:
#     for j in l:
#         if j.startswith(i):
#             m.append(j)
# print(m)
# lst = [1,2,3,4,5,6,7,8,9]
# even = list(filter(lambda n : n%2 == 0,lst))
# print(even)
# dubles = list(map(lambda n: n*2,even))
# print(dubles)
# def fun(n):
#     for i in range(65,n):
#         for j in range(65,i+1):
#             print(chr(i),end='')
#         print()
# fun(70)
# x = input("Enter the values: ")
# y = input("Enter the values: ")
# z = zip(x,y)
# print(dict(z))
# x = [1,2,3,4,5]
# for i in range(5):
#     x = x[-1::]+x[:-1]
#     print(x)

# def fib():
#     x = 0
#     y = 1
#     # print(x)
#     # print(y)
#     for i in range(5):
#         z = x+y
#         x = y
#         y = z
#         print(z)
# fib()
# string = 'satish saladi'
# new_string = ''
# for i in string:
#     new_string = i + new_string
# print(new_string)
# for i in string.split():
#     new_string = i +' '+ new_string
# # print(new_string)

# def pattern():
#     for i in range(5):
#         for k in range(i):
#             print('',end= ' ')
#         for j in range(5-i):
#             print('*',end = ' ')
#         print()
# pattern()

sorting = [3,5,9,8,2,1]
# for i in range(0,len(sorting)-1):
#     for i in range(0,len(sorting)-1):
#         if sorting[i] > sorting[i+1]:
#             sorting[i],sorting[i+1] = sorting[i+1],sorting[i]
# print(sorting)

# new = []
# for i in ((sorting)):
#     new.insert(0,i)
# print(new)
# a = "DevLopMent"  # ans is "D evL opM ent"
# b = ''
# for i in a:
#     if i.isupper():
#         # b = "{} ".format(b+i)
#         b = f'{b+i} '
#     else:
#         b = b+i
# print(b)
# import math
# print(math.sqrt(7))

# Python program to illustrate the difference between shallow and deep copy
# import copy

# class Car:
# 	def __init__(self, name, colors):
# 		self.name = name
# 		self.colors = colors

# # Create a Honda car object
# honda_colors = ["Red", "Blue"]
# honda = Car("Honda", honda_colors)

# # Deepcopy of Honda
# deepcopy_honda = copy.deepcopy(honda)
# deepcopy_honda.colors.append("Green")
# print("Deepcopy:", deepcopy_honda.colors)
# print("Original:", honda.colors)

# # Shallow Copy of Honda
# copy_honda = copy.copy(honda)
# copy_honda.colors.append("Green")
# print("Shallow Copy:", copy_honda.colors)
# print("Original:", honda.colors)

# class A:
#     def __init__(self,model,year):
#         self.model = model
#         self.year = year
#     @staticmethod
#     def stat_show(self,model,year):
#         return (self,model,year)
#     def dyn_show(self):
#         return(self.model,self.year)
# obj = A('bmw',2021)
# print(obj.dyn_show())
# print(A.stat_show('Tata','Nexon',2024))
# def fib(n):
#     a = 0
#     b = 1
#     # n = int(input("Enter the number:"))
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a+b
#         a = b 
#         b = c
#         print(c)
# fib(6)

# x,y = 1,2
# print(f"the x,y values are before swapping:",x,y)
# y,x = x,y
# print(f"the x,y values are after swapping:",x,y)

# def rev():
#     name =  'Satish Saladi'
#     reverse = ''
#     for i in name.split():
#         reverse = i +' '+ reverse
#     print(reverse)
# rev()

# def sorting():
#     num = [5,2,1,6,4,0,3]
#     for i in range(0,len(num)-1):
#         # print(i)
#         for i in range(0,len(num)-1):
#             # print(i)
#             if num[i] > num[i+1]:
#                 num[i],num[i+1] = num[i+1],num[i]
#     print(num)
#     print(list(set(num)))
#     print(sorted(num))
# sorting()

# import numpy
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # row = 1
# # column = 2
# # x[row][column] = 11
# # print(x)
# print(numpy.matrix(x))

# s = [1,2,3,4,5]
# l = []
# for i in s:
#     l.insert(0,i)
# print(l)

# A, B, C = map(int, input().split())
# print(A, B, C)

# a = 1
# b = 4
# while (a != b):
#    print(b)
#    b = b + 1

# t = int(input())
# for i in range(t):     
#     N = int(input())     
#     print(N)

# t = int(input())       
# for i in range(t):     
#     # accept 2 integers on the 1st line using map
#     A,B = map(int, input().split()) 
#     # accept 3 integers on the 2nd line using map
#     C,D,E = map(int, input().split())
#     # output the 5 integers on a single line for each test case
#     print(A, B, C, D, E)

# import os
# from datetime import datetime
# print(dir(os))
# print(os.getcwd())    # for current directory
# os.chdir("C:\\Users\\apple\\")    # for change the directory
# print(os.getcwd())
# print(os.listdir())     # for list of directories/folders
# os.mkdir("Satish")        # for create folder
# os.makedirs("Satish\Sub_Satish")        # for create folder and subfolder at a time
# os.rmdir("Satish")                    # for remove dir/folder
# os.removedirs("Satish/Sub_Satish")    # for remove folder and subfolders
# os.rename('Satish','Geetha')          # for rename folder name
# print(os.stat("Flipkart"))            # for file properties
# print(os.stat("Flipkart").st_mtime)
# mod_time = os.stat("Flipkart").st_mtime
# print(datetime.fromtimestamp(mod_time))
# for dirpath,dirnames,filenames in os.walk('C:\\Users\\apple\\PycharmProjects'): # for all the folders and files information in that path
#     print("currentpath:", dirpath)
#     print('directories:', dirnames)
#     print('files:', filenames)
# print(os.environ.get("HOME"))
# file_path = os.path.join(os.environ.get("HOME"), 'main.py')  # for finding the file path of main.py file
# print(file_path)
# print(dir(os.path))
# print(os.path == "C:\\Users\\apple\\PycharmProjects\\Practice\\sample.txt")
# import subprocess
# subprocess.run()

# dic = {(1,2) : 'a,b'}
# print(dic)

# a = [1,2,3,4,5,6]
# print(a[-1::])
# print(a[:-1])
# for i in range(6):
#     a = a[-1::] + a[:-1]
#     print(a)

# x = input('enter the value:')
# y = input('enter the value:')
# # print(list(zip(x,y)))
# z = dict(zip(x,y))
# print(z.keys())

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# if __name__ == '__main__':
#     n = int(input().strip())
#     1<n<100
# if n%2 == 0:
#     if range(n,6):
#         print("Not Weird")
#     elif range(n,20):
#         print("Weird")
#     else:
#         print('Not Weird')
# else:
#     print("Weird")

# print(10**5)

# def count_substring(string, sub_string):
#     count = 0
#     start_index = 0
#     while start_index < len(string):
#         index = string.find(sub_string,start_index)
#         if index == -1:
#             break
#         count += 1
#         start_index = index + 1
#     return count 
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(f"count of string:{count}")

# globalvar = 10
# def fun():
#     ans = 0
#     localvar = globalvar   # Optimization
#     for i in range(1000):
#         # ans += globalvar * i
#         ans += localvar * i
#     return ans
# print(fun())

# user_name = input("Name:")
# # if user_name:
# #     name = user_name
# # else:
# #     name = 'N/A'
# # print(name)

# name = user_name or 'N/A'
# print(name)

# old = ['a','b','c','b','a']
# new = list(set(old))
# print(new)
# new =[]
# for item in old:
#     if item not in new:
#         new.append(item)
# print(new)
# new = list(dict.fromkeys(old))
# print(new)

# inv = {'sword' : 1,'postion' : 3}
# loot = {'sword' : 1,'postion' : 2,'shield' : 1}
# # inv.update(loot)
# # print(inv)
# new_inv = {
#     k : inv.get(k, 0) + loot.get(k, 0) \
#     for k in set(inv | loot)
# }
# print(new_inv)

# inv = ['gem','swoad','ele','xyz']
# new_inv = inv[1::] + inv[:1]
# print(new_inv)

# x = [1,1,2,3,2,1,4]
# most = max(x,key = x.count)
# print(most)

# my_tup = ([1,2],[3])
# print(id(my_tup))
# my_tup[1].append(4)
# print(my_tup)
# print(id(my_tup))

# def do_this():
#     print('doing this')
# def do_that():
#     print('doing that')
# match input("doing this or that?:"):
#     case 'this':
#         do_this()
#     case 'that':
#         do_that()
#     case _:
#         print("invalid input")

# web = ['www.youtube.com','www.wikipedia.com','www.google.com']
# for link in web:
#     # print(link.lstrip('www.')) #out put removing w in wikipedia
#     print(link.removeprefix("www."))

# def my_decorator(fun):
#     def wrapper():
#         print(f"runing {fun.__name__}")
#         fun()
#         print('completed')
#     return wrapper
# @my_decorator
# def do_this():
#     print('doing this')
# @my_decorator
# def do_that():
#     print('doing that')
# do_this()
# do_that()

# import os
# files = ['test.txt','image.jpg','test.3.txt']
# for item in files:
#     name = os.path.splitext(item)[0]
#     print(name)

# with open('C:\\Users\\apple\\Downloads\\test.txt','r') as input, \
#     open('C:\\Users\\apple\\Downloads\\test.txt','w')  as output:
#     text = input.readlines()
#     uppercase = [t.upper() for t in text]
#     output.writelines(uppercase)

# balance = 945.70
# while True:
#     try:
#         num = float(input("Deposit balance:"))
#         break
#     except ValueError:
#         print("Enter the numbers only")
# balance += num
# print(f"balance is {balance}")

# while True:
#     password = input("Enter the Password:")
#     if password == 'Satish@9':
#         print("Access Granted!")
#         break
#     else:
#         print('Aceess Denaied!')

# s1 = 'abcdefghi'
# s2 = 'abcdefgsi'
# s = zip(s1,s2)
# s3 = enumerate(s)
# # print(list(s))
# # print(list(s3))
# for i,(a,b) in s3:
#     if a!=b:
#         print(f'index: {i}')

# inv = ['Iron Sword','Wooden Shield','Stick']
# print(f"You have: {', '.join(inv)}")

# names = ['satish saladi','manikanta kavala','ramana narla','veerendra nandikolla']
# last = [i.split()[-1] for i in names]
# print(last)

# names = ['satish','manikanta','ramana','veerendra']
# # x = [len(name) for name in names]
# x = {name:len(name) for name in names}
# print(x)

# x = 'satishSaladi'
# print(x.title())
# print(x.rfind('a'))

# x = 'abc'
# x.replace('a','1')
# x + 'def'
# print(y)

# nums = range(1,100)
# def is_prime(num):
#     for x in range(2,num):
#         if num%x == 0:
#             return False
#     return True
# primes = list(filter(is_prime,nums))
# print(primes)

# string = input("Enter the Name:")
# new = ''
# for name in string:
#     if name.isupper():
#         new = f'{new} {name}'
#     else:
#         new = new + name
# print(new)

# def fun(arr):
#     for i in arr:
#         if i == 0:
#             arr.remove(i)
#             arr.append(0)
#     return arr
# arr = [1,0,3,4,0,5]
# print(fun(arr))
#     t = []
#     z = 0
#     for i in arr:
#             if i != 0:
#                   t.append(i)  
#             else:
#                   z += 1
#     t.extend(z * [0])
#     return t
# arr = [1,0,3,4,0,5]
# print(fun(arr))
# import random
# import time
# n = 200000
# arr = [random.randint(0,9) for _ in range(n)]
# start = time.time()
# x = fun(arr)
# stop = time.time()
# print(stop -  start)

# names = {}
# # names[1] = 'Manikanta'
# # # print(names)
# names[2] = 'Shankar'
# names[3] = 'Pradeep'
# names[4] = 'Sridhar'
# names[5] = 'Satish'
# names[6] = 'Seshagiri'
# names[7] = 'Raja'
# # print(names)
# names.update({8 : 'Srinu'})
# # print(names)
# # names.pop(1)
# # print(names)
# names.update({1:'Manikanta'})
# names.update({9:'Manikanta'})
# # # print(names)
# # # print(help(names))
# # # print(names)
# # # print(names.items())
# for i,j in names.items():
#     # print(i,j)
#     if j == 'Manikanta':
#         print(i,j)
            
# print(names.get(9))
# print(names.get(1))

# import logging

# arr = [1,0,3,4,0,5]
# logging.debug(arr)

# import subprocess

# s = subprocess.run('hostname',shell = True)
# print(s)
# import os
# from datetime import datetime
# os.chdir('C:/WINDOWS/TEMP/')
# print(os.environ.get('TEMP'))
# file_path = os.path.join(os.environ.get('TEMP') , 'test.txt')
# print(file_path)

# import random
# list1 = ['satish','geetha','karthika','saladi']
# random.shuffle(list1)
# print(list1)

# class Maths():
#     #static method
#     @staticmethod
#     def add(x,y):
#         return x + y
#     #dynamic method
#     def multifly(self,x,y):
#         self.x = x
#         self.y = y
#         return self.x * self.y
# result = Maths.add(3,3)
# print(f'StaticMethod: {result}')
# res = Maths()
# print(f'DynamicMethod: {res.multifly(2,2)}')
    
# class Emp():
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
#         # return(self.name,self.sal)
#     def __str__(self):
#         return(self.name)
# # Emp('Satish','100k')
# pbj = Emp('Satish','100k')
# print(pbj)
# name = input("enter the name:")
# b = name[::-1]
# if name == b:
#     print('palandrom')
# else:
#     print('not')

# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(A0)

# def d(x):
#     return x*2
# def t(x):
#     return x*3
# x = 2
# print(d(t(d(x))))

# t = {}
# t[{1,2,3}] = 10
# t[{3,2,1}] = 12
# t[{1,2}] = 8
# print(t)
# sum = 0
# for k in t:
#     print(k)
# sum +=1
# print(len(t))
# print(sum(t))

# list = [10,20,13,14,50]
# x = sorted(list,reverse= True)
# print(x)
# if len(x)<2:
#     print('nothing')
# else:
#     print(x[1])

# name = 'hi hello  anybody   there!'
# x = name.replace('  ',' ').replace('  ',' ')
# print(x)

# z = lambda q: q**2
# print(z(24))
# y = list(map(lambda n : n,range(0,5)))
# x = list(map(lambda n :n**2,y))
# print(y)
# print(x)

# list = [10,20,13,14,50]
# x = sorted(list,reverse=True)
# print(max(x))
# print(x[1])
# if len(x) < 2:
#     print('nothing')
# else: 
#     print(x[1])

# text = 'Name\tAge\tLocation\nSatish Saladi\t30\tBangalore'
# print(text.expandtabs(15))

# A,B = map(int, input().split()) 
# print(A*B)

# a,b = map(int,input().split())
# if a+b+(a*b) == 111:
#     print('Yes')
# else:
#     print('No')

# import copy as c
# original_list = [[1, 2, 3],[4, 5, 6]]
# #if in list have any collections in twice than only work shallow copy.
# shallow_list = c.copy(original_list)
# original_list[1][0] = 100
# print(original_list)
# print(shallow_list)

# original_list = [[1, 2, 3],[4, 5, 6]]
# deep_list = c.deepcopy(original_list)
# original_list[1][0] = 400
# print(original_list)
# print(deep_list)

# lista = [3,1,4,2,5]
# # x = sorted(lista,reverse = True)
# # print(x[::-1])
# x = set(lista)
# print(list(x))

# from icecream import ic

# def add(x, y):
#     return x + y
# ic(add(20, 30))

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()  # Call the original function
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()

# with open("F:/Python/Geetha/geetha.jpg", 'rb') as f:
#     content = f.read()

# for i in range(10):
#     with open(f"F:/Python/Geetha/new_geetha{i}.jpg", 'wb') as f:
#         f.write(content)

# lista = [10,8,20,40,15]
# # x = sorted(lista, reverse = True)
# # print(x[1])
# for i in range(len(lista)-1):
#     for i in range(len(lista)-1):
#         if lista[i] > lista[i+1]:
#             lista[i], lista[i+1]  = lista[i+1], lista[i]
# print(lista)
# print(lista[-2])
    
# print(list(map(lambda x, y : x*y, [1,2,3], [5,6,7])))
# print(list(zip([1,2,4,8], [4,5,6], [9,10,11])))
# print(list(filter(lambda x: x>5, [10,2,3,200])))
# from functools import reduce
# print(reduce(lambda x,y : x*y, [1,2,4,5,6])) 

# c = lambda x,y: x+y
# print(c(2,3))

# str_ = "PRadpDeep"
# print(''.join(chr(ord(c) + 32) if "A"<=c<="Z" else c for c in str_))
# x = format('hello','^30')
# print(x)
# x = 5
# x <<= 3
# print(x)

# x = [1,2]
# y = [1,2]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)

# count = 10
# while count > 0:
#     count -= 1
#     if count == 3:
#         continue
#     print(count)
    
lista = [10,4,2,29,49,20]
# print(lista)
for i in range(0,len(lista)-1):
    for i in range(0,len(lista)-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)
print(lista[-2])