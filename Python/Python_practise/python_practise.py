"solution 1"'''a=int(input())
if a>0:
    print("positive")
else:
    print("false")'''
"""solution 2""""""a=int(input())
if a>18:
    print("above 18")
if a<18:
    print("less 18")
if a==18:
    print("exact 18")"""
"""solution 3"""'''a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")'''
"""solution 4""" 
"""a=int(input())
if a>18:print("eligible to vote")
else:(print("inelgible to vote"))"""
"""solution 5"""
'''a=int(input("marks="))
if a<=20:print("pass")
elif a<=40:print("average")
elif a<=80:print("good")
else:print("fail")'''
'''solution 6'''
"""a=int(input())
if a<10:print("very cold")
elif a>=10 and a<=19:print("cold")
elif a>=20 and a<=29:print("normal")
elif a>=30: print("hot")"""
"""solution 7"""
'''a=int(input())
if a>=18:print("adult")
if a>21:print("Above 21")
if a>60:print("Senior Citizen")'''
"""Solution 8"""
"""a=int(input())
if a>0:print("positive")
if a>10:print("Greater than 10")
if a%2==0:print("even")"""
"""a=int(input())
if a>0:print("positive")
if a==0:print("equal")
if a<0:print("less")"""
'''a=int(input())
if a%2==0:print("even")
else:print("odd")'''
"""a=int(input())
b=int(input())
c=int(input())
if a>b:print("a big")
if b>a:print("b big")
if c>b:print("c big")"""
'''a=int(input())
if a>=18:
    if a>=60:print("old") 
    else: print("adult") 
else:print("minor")'''
'''x,y,=input("Values:").split()
print(x)
print(y)'''
'''z="car,truck,bus,palne"
print(z.split(",",2))
text="My name is kushagra"
x=text.split()
print(x)
number=[1,2,3,4,5]
square=[num*num for num in number]
print(square)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even= [num for num in numbers if num%2==0 ]
print(even)
numberss = [5, 12, 8, 20, 3, 15]
num=[num for num in numberss if num>10]
print(num)
words = ["apple", "banana", "cat", "elephant"]
length=[len(word)for word in words]
print(length)
a=10
b=2
c=a%b
print(c)
print("hello world")
a=10
b=20
a,b=b,a
print(a,b)
a="kush"
print(len(a))
a="kush"
b="kushagra"
c=len(a)
d=len(b)
a="python1"
b="python1"
print(a and b)
a="kushagra"
b=a[::-1]
print(b)'''
'''x=10
x=20
print(x)
name='kushagra'
age=20
city="kanpur"
print(name)
print(age)
print(city)'''
'''print(10/3)
print(10//3)
a=10
b=3
print("addition",a+b)
print("substraction",a-b)
print("multiply",a*b)
print("exponential",a%b)

a=10
b=a
if a%2==0:
    print("even")
print(b)

a=10
if a>10:
    print("greater than 10")
else:
    print("AND less than 50")'''
'''a=int(input("Enter a Number:"))
if a>10:
    print("number is greater than 10")
a=int(input("Enter temperature:"))
if a>30:
    print("HOT")'''
'''a=int(input("Enter a number:"))
if a%2==0:
    print("The number is even")
else:
    print("the number is odd")'''
'''a=int(input("Enter user age"))
if a>=18:
    print("User is adult")
else:
    print("user is minor")
a=int(input("Enter a number"))
if a>0:
    print("number is positve")
else:
    print("number is negative")'''
'''a=int(input("Entera number"))
if a>0:
    print("positive")
elif a<0:
    print("Negative")
else:
    print("zero")'''
'''a=int(input("Enter a number"))
if a==1:
    print("Monday")
elif a==2:
    print("tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("thursday")
elif a==5:
    print("friday")
elif a==6:
    print("saturday")
elif a==7:
    print("sunday")
else:
    print("invalid")'''
'''a=int(input("enter a number"))
if a>50:
    print("number is greater than 50")'''
'''a=int(input("Enter a number"))
if a%2==0:
    print("a is even")
else:
    print("odd")'''
'''a=int(input("Enter a number: "))
if a>=90:
    print(" b grade")
elif a>=75 and a<=89:
    print(" c grade")
elif a>=60 and a<=74:
    print(" c grade")
elif a>=40 and a<=59:
    print(" d grade")
else:
    print(" fail ")'''
'''a=int(input("Enter age: "))
if a>=18:
    print("eligible to vote")
else:
    print("Not eligible to vote")'''
'''a=int(input("Enter a number: "))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")'''
a=["kush","for","kush"]
'''for i in a:
    print(i)
for i in range(0,20,4):
    print(i,end=" ")'''
'''for i in range(0,10):
    print(i,end=" ")
    if i==7:
        break'''
'''count=0
while count<5:
    count=count+1
    print(count,end="\n")'''
'''for i in range(0,10):
    print(i)
a=int(input("enter a number:"))
for i in range(0,a):
    print(i)
for i in range(0,20):
    print(i%2==0,)'''
'''for i in 'Kushagra':
    if i == 'g' or i == 's':
        continue
    print(i)'''
'''i=1
while i<=5:
    if i==4:
        break
    print(i)
    i+=1'''
'''b=["eat","sleep","repeat"]
for i,j in enumerate(b):
    print(i,j)'''
count=0
while count <4:
    count= count+1
    print("hello")