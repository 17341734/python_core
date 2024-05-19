#!/usr/bin/env python
# coding: utf-8

# # Python Data Structures

# ## Numeric Types 

# Every number, string, data structure, function, class, module, and so on exists as a Python object.
# <br> Most used numeric types : Integer and floating point numbers

# numeric types are automatically understood by python

# In[1]:


x=7


# In[2]:


type(x)


# In[3]:


x=7.0


# In[4]:


type(x)


# In[5]:


x=3+1j


# In[6]:


type(x)


# ## Strings 

# A string is a sequence of characters.
# <br> You can write strings using either single quotes ' or double quotes "

# In[7]:


a="this is a string";a


# In[8]:


b='this is also a string';b


# In[9]:


c="ahmet's idea";c


# For multiline string use triple of single-quote or double-quote

# In[10]:


d=""" 
this is a multi line
string
"""


# In[11]:


d


# \n character is a special character which tells the computer to go to next line

# In[12]:


print(d)


# ### len() function gives the number of element in a data object in python 

# In[13]:


b="this is a string"


# In[14]:


len(b)


# In[15]:


b="this is a          string"


# In[16]:


len(b)


# ## String Indexing 

# Sequences maintain a left-to-right order among the items they contain: their items are stored and fetched by their relative positions.
# <br>You can access the characters with the bracket operator [ ]

# In[17]:


t="python"


# In[18]:


t[0]


# in python indexing starts with 0

# In[19]:


t[1]


# In[20]:


t[-1]


# In[21]:


t[-2]


# ## String Slicing

# string name[starting location : ending location+1]

# In[22]:


t="python"


# In[23]:


t[0:2]


# In[24]:


t[0:3]


# In[25]:


t[:]


# In[26]:


t[:3]


# In[27]:


t[3:]


# In[28]:


t[-3:-1]


# In[29]:


t[-3:]


# ## Tuples

# A tuple is a fixed-length, immutable sequence of Python objects.
# <br> The easiest way to create one is with a comma-separated sequence of values or using paranthesis ()

# In[30]:


a=3,4,5;a


# In[31]:


type(a)


# In[32]:


b=(2,4,5)


# In[33]:


type(b)


# ### Any sequence or iterator can be converted to a tuple by invoking tuple:

# In[34]:


a="test string";a


# In[35]:


type(a)


# In[36]:


b=tuple(a);b


# In[37]:


type(b)


# Tuple elements can be accessed with square brackets.

# In[38]:


b[0]


# In[39]:


b[-1]


# In[40]:


b[:3]


# ### tuple object methods 

# In[41]:


b=(1,2,2,3,3,3,4,4,4,4,5,5,5,5,5)


# In[42]:


b.count(2)


# In[43]:


b.count(5)


# In[44]:


b.index(4)


# In[45]:


b.index(3)


# ## List

# In contrast with tuples, lists are variable-length and their contents can be modified.
# <br> They can be defined using square brackets [] or using the list type function:

# In[46]:


mylist=[2,3,4,"text",None,True,"book"];mylist


# In[47]:


mylist[0]


# In[48]:


mylist[3]


# In[49]:


mylist[4]


# In[50]:


mylist[5]


# ### You can convert any sequence data structure into a list by typing list() 

# In[51]:


a="book"


# In[52]:


b=list(a);b


# ## List methods 

# List.append() appends a new element into a list

# In[53]:


t=[1,"1",2,"book","text","class"];t


# In[54]:


t.append("new")


# In[55]:


t


# Del list[i] deletes a list element

# In[56]:


del t[0]


# In[57]:


t


# List.pop(i) removes ith element in a list and returns the value of the element

# In[58]:


t.pop(0)


# T.remove(value) removes first element that has value as “value”

# In[59]:


t


# In[60]:


t.remove("text")


# In[61]:


t


# ##  + concatenates list,string or tuple 

# In[62]:


[1,2,3]+["a","b","c"]


# In[63]:


"test"+"string"


# In[64]:


c=(1,2,3)+("a","b","c");c


# ##  Extend vs Append

# In[65]:


t=[10,20,30]


# In[66]:


t.extend([40,50,60])


# In[67]:


t


# In[68]:


t[3]


# In[69]:


t=[10,20,30]


# In[70]:


t.append([40,50,60])


# In[71]:


t


# In[72]:


t[3]


# ### List slicing 

# In[73]:


l=[10,20,30,40,50]


# In[74]:


l[1:3]


# In[75]:


l[3:]


# ## Changing list elements

# In[76]:


l=list("abcde");l


# In[77]:


l[1]


# In[78]:


l[1]=100


# In[79]:


l


# ##  sorting the list 

# In[80]:


mylist=list("deabc");mylist


# In[81]:


mylist.sort()


# In[82]:


mylist


# In[83]:


mylist=[4,0,5,9]


# In[84]:


mylist.sort();mylist


# In[85]:


mylist=[4,0,5,9,"a","d","c"]


# In[86]:


mylist.sort();mylist


# ### Insert function adds element at the desired index 

# In[ ]:


mylist=["Zebra","Lion","Cat","Camel","Eagle","Shark"]


# In[ ]:


mylist.insert(1,"Whale")


# In[ ]:


mylist


# In[ ]:


mylist.reverse()


# In[87]:


mylist


# In[88]:


mylist.clear()


# In[89]:


mylist


# In[90]:


del mylist


# In[91]:


mylist


# ## In operator 
# This operator returns if searched element in the data object or not

# In[92]:


mylist=["Zebra","Lion","Cat","Camel","Eagle","Shark"]


# In[93]:


"Eagle" in mylist


# In[94]:


"Horse" in mylist


# In[95]:


t="There are 30 students registered to this class"


# In[96]:


"class" in t


# In[97]:


"Class" in t


# ## Dictionaries

# A dictionary is like a list, but more general. In a list, the positions (indices) have to be integers; in a dictionary the indices can be (almost) any type.
# <br> Dictionary maps between a set of indices (which are called keys) and a set of values.
# <br> Dictionaries can be created by using curly braces {} and using colons to separate keys and values:

# In[98]:


salary={}


# In[99]:


salary["ahmet"]=1000


# In[100]:


salary


# In[101]:


salary["ayşe"]=2000


# In[102]:


salary


# In[103]:


salary["zeynep"]=3000


# In[104]:


salary


# now get the salary of zeynep

# In[105]:


salary["zeynep"]


# now get the salary of ahmet

# In[ ]:





# try getting the first element of dictionary

# In[106]:


salary[0]


# in dictionary you cannot access the data using indeces!!

# with in operator you can check if key is there or not

# In[107]:


"ahmet" in salary


# In[108]:


"mehmet" in salary


# to remove elements use dictionary.pop() function

# In[109]:


salary.pop("ahmet")


# In[110]:


salary


# • The keys and values method give you lists of the keys and values, respectively

# In[111]:


salary.keys()


# In[112]:


salary.values()


# items function retursn both key and value

# In[113]:


salary.items()


# • One dictionary can be merged into another using the update method.

# In[114]:


salary.update({"lale":1500,"Tarık":3000})


# In[115]:


salary


# ##  Nested Dictionary 

# In[116]:


rec = {'name': 'Bob',
'jobs': ['developer', 'manager'],
'web': 'www.bobs.org/ ̃Bob',
'home': {'state': 'Overworked', 'zip': 12345}}


# In[117]:


rec


# In[118]:


rec["name"]


# In[119]:


rec["jobs"]


# In[120]:


rec["jobs"][0]


# In[121]:


rec["home"]


# get the zip code 

# In[ ]:





# ## Sets

# A set is an unordered collection of unique elements.
# <br>• A set can be created in two ways: via the set function or using curly braces:
# <br>• Sets support mathematical set operations like union, intersection, difference
# <br>• Empty set should be created as s=set() command. This creates a new set which is called as s.

# In[122]:


a={2,3,5,7,7,7,4,4,4,3,3}


# In[123]:


type(a)


# In[124]:


a


# In[125]:


b=set([1,2,2,2,3,3,9,9,6,6,6])


# In[126]:


b


# In[127]:


a | b #union 


# In[128]:


a & b #intersection


# In[129]:


a-b # difference


# In[130]:


b-a


# press tab key after a. to see what functions available for set objects

# In[131]:


a.isdisjoint(b)


# In[132]:


c=set([10,20,30])


# In[133]:


a.isdisjoint(c)


# sets take strings as well

# In[134]:


engineers={"bob","sue","ann","vic"}


# In[135]:


managers={"tom","sue"}


# In[136]:


"bob" in engineers


# In[137]:


engineers&managers


# In[138]:


engineers | managers


# In[139]:


engineers - managers

