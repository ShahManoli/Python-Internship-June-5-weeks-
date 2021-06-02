#functions
#no argument no return ype

# def myfunction():
#     print("manoli")
# myfunction()
# myfunction()

#with argument no return type

# def myfunction(name):
#     print("Name is",name)
# myfunction("manoli")

#with argument with return type

# def myfunction(name):
#     return name
# name=myfunction("manoli")
# print("valus is",name)

#returning multiple values

# def myfunction():
#     name='manoli'
#     a=50
#     return name,a
# name,a=myfunction()
# print("name is",name)
# print("a is",a)

#default arguments

# def sum(a=50,b=50):
#     print(a+b)
# sum(20,20)
# sum()

#keyword argument

# def sum(a,b):
#     print(a+b)
# sum(b=50,a=10)

#variable length arguments
#(* - non keyword arguments)
#(** - keyword arguments)

#non keyword argument:
# def sum(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     print("sum is",sum)
# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40,50)

#keyword argument:
# def myfunction(**arg):
#     for i,j in arg.items():
#         print(i,j)
#
# myfunction(name='manoli',name2='shah')

#local and global variables
# def fun():
#     x=5
#     print("value inside function :",x)
# y=20
# fun()
# print("value outside function:",y)

#indentation error - it occurs when in loops,class ,conditional statements space is not kept.

#operators

#arithmetic operators
# a=20
# b=10
# print('a+b=',a+b)
# print('a-b=',a-b)
# print('a*b=',a*b)
# print('a/b=',a/b)
# print('a//b=',a//b)
# print('a**b=',a**b)

#comparision operators
# a=10
# b=6
# print('a>b is',a>b)
# print('a<b is',a<b)
# print('a==b is',a==b)
# print('a!=b is',a!=b)
# print('a>=b is',a>=b)
# print('a<=b is',a<=b)

#logical operators

# a,b,c=10,20,30
# if a>b and a>c:
#     print("a is largest")
# if b>a and b>c:
#     print("b is largest")
# if c>a and c>b:
#     print("c is largsest")

#or operator
# ch=input("enter a character")
# if(ch=='A' or ch=='a' or ch=="E" or ch=='e' or ch=='I' or ch=='i' or ch=='O'or ch=='o' or ch=='U'or ch=='u'):
#     print(ch,'is a vowel')
# else:
#     print(ch,"is a consonant")

#membership operator - they are used to test whether a variable is found in a sequence.
#(string,listtuple,set and dictionary)

# x=10

# y=20
# l=[10,30,40,50]

# print(x in l)
# print(y in l)
# print(y not in l)

#identity operator

x=10
y=10
print(x is y)
print(x is not y)

