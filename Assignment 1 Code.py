
# coding: utf-8

# In[1]:


i=2000
x=''
while i<=3000:
    #print (i)
    if i%7==0 and i%5!=0:
        x=x+','+str(i)
    i=i+1
        
print (x[1:len(x)])


# In[3]:


print("Enter FirstName:")
x=input()
print("Enter LastName:")
y=input()
print(y+' '+x)


# In[10]:


d=12
r=12/2
pi=3.14
V=4/3*pi*r**3
print(V)

