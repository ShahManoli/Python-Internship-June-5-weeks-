# OOPS concept

# class demo:
#     def sum(self):
#         print("this is my function")
#
#     def show(self,name):
#          print("name is",name)
# d1=demo()
# d1.sum()
# d1.show("manoli")

#add
# class sum:
#     def fun(self,a,b):
#         c=a+b
#         print("ans is :",c)
# abc=sum()
# abc.fun(30,20)

# constructor
# class demo:
#     def sum(self):
#         print("this is my function")
#
#     def show(self,name):
#          print("name is",name)
#
#     def __init__(self):
#         print("this is demo class..")
#
#     def __init__(self,name):
#         print("this is demo class..")
#         print("name is",name)
#
#
# d1=demo("xyz")
# d1.sum()
# d1.show("manoli")

# assign string value to class variable using method
# class demo:
#     name=""
#
#     def fun(self):
#         print("this is normal method")
#     def fun2(self,name):
#         self.name=name
#     def show(self):
#         print("Name is",self.name)
#
# d1=demo()
# d1.fun()
# d1.fun2("manoli")
# d1.show()

# assign string value to class variable using constructor
# class demo:
#     name=""
#     def __init__(self,name):
#             self.name=name
#     def fun1(self):
#         print("Name is:",self.name)
# abc=demo("Manoli")
# abc.fun1()

# example 2:
# class demo:
#     a=0
#     b=0
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def fun1(self):
#         c=self.a+self.b
#         print("ans is :",c)
# abc=demo(50,50)
# abc.fun1()

#inheritance
#single inheritance
# class parent:
#     def __init__(self):
#         print("this is demo class")
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def __init__(self):
#         print("this is demo1 class")
#     def fun2(self):
#         print("this is child class")
# c=child()
# c.fun1()
# c.fun2()

#multi level inheritance
# class parent:
#     def __init__(self):
#         print("this is demo class")
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def __init__(self):
#         print("this is demo1 class")
#     def fun2(self):
#         print("this is child class")
# class grandchild(child):
#     def fun3(self):
#         print("this is child method of child class")
#
# c=grandchild()
# c.fun1()
# c.fun2()
# c.fun3()

#multiple inheritance
# class parent:
#     def __init__(self):
#         print("this is demo class")
#     def fun1(self):
#         print("this is parent class")
# class child:
#     def __init__(self):
#         print("this is demo1 class")
#     def fun2(self):
#         print("this is child class")
# class grandchild(parent,child):
#     def fun3(self):
#         print("this is child method of child class")
#
# c=grandchild()
# c.fun1()
# c.fun2()
# c.fun3()

#hierarchical inheritance
# class parent:
#     def __init__(self):
#         print("this is demo class")
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def __init__(self):
#         print("this is demo1 class")
#     def fun2(self):
#         print("this is child class")
# class grandchild(parent):
#     def fun3(self):
#         print("this is child method of child class")
#
# d1=child()
# d1.fun1()
# d1.fun2()
#
# d2=grandchild()
# d2.fun1()
# d2.fun3()

#hybrid inheritance
# class Myparentclass1():
#     def method_parent1(self):
#         print("parent1 method called")
# class Myparentclass2():
#     def method_parent2(self):
#         print("parent2 method called")
# class childclass(Myparentclass1, Myparentclass2):
#     def child_method(self):
#             print("child method")
# class childclass2(Myparentclass1):
#     def child_method2(self):
#         print("child method2")
# c=childclass()
# c.method_parent1()
# c.method_parent2()
# c.child_method()
#
# c2=childclass2()
# c2.child_method2()
# c2.method_parent1()

#polymorphism

#method overriding
# class demo:
#     def fun1(self):
#         print("this is demo class")
# class demo1(demo):
#     def fun1(self):
#         print("this is demo1 class")
#
# d1=demo1()
# d1.fun1()

#method overloading

# class demo:
#     def sum(self,a,b):
#         ans=a+b
#         print("ans is",ans)
#     def sum(self,a,b,c):
#         ans=a+b+c
#         print("ans is",ans)
#
# x=demo()
# x.sum(10,20,30)
#last method will be implemented    