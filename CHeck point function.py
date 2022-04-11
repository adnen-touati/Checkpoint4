#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 1

def highernumber(x,y,z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z :
        print(y)
    else :
        print(z)

 


# In[2]:


x = int(input())
y = int(input())
z = int(input())
highernumber(x,y,z)


# In[4]:


#question 2
def sub_add (x,y):
    print(x+y,x-y)
a = int(input())
b = int(input()) 
sub_add(a,b)


# In[35]:


#Question 3
#* Write a function that sums the elements of a list of integers.
#* Write a function that multiplies the elements of an integer list.
#* Use the two functions to sum the elements whose position is an even number (0,2,4…) and multiply the rest.
#Hint: Consider extracting two lists from a first list 
#Part 1
L =[1,2,3,4] 
def add (my_list) :
    x=0
    for i in my_list:
        x= x + i
    print(x)

add(L)
def add1 (my_list1) :
    x=0
    for i in range (len(my_list1)):
        x= x + int(my_list1[i])
    print(x)
add1(L)

#part 2
def mult (my_list) :
    x=1
    for i in range (len(my_list)):
        x= x * int(my_list[i])
    print(x)
mult(L)

#part 3
L1=[]
L2=[]
def evenodd (my_list):
    for i in range (len(my_list)) :
        if i % 2==0 :
             L1.append(my_list[i])
        else:
             L2.append(my_list[i])
evenodd(L)

print(L1)
print(L2)
add(L1)
mult(L2)

            

    
    


# In[33]:


def mult (my_list) :
    x=1
    for i in range (len(my_list)):
        x= x * int(my_list[i])
    print(x)
l=[2,4]
mult(l)


# In[12]:


#Question 4
#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow

#Hint : There's a split function to separate your input string into words and a sort function to sort.

chaine= input()
L2=[]
L1=chaine.split("-")
print(L1)
L1.sort()
print (L1)
for i in range(len(L1)):
    L2.append(L1[i]+"-")
print(L2)
s=""
for i in L2:
    s += i
s


# In[ ]:




