# ways to create string variable
# EXAMPLE 1
print('EXAMPLE 1   !!!!!!!!!!!')
s= "Welcome"
s= 'Welcome'
s= str("Welcome")
s= str('Welcome')

# creating empty string variable
name= ""
name=''
name= str()

# EXAMPLE 2
print('EXAMPLE 2   !!!!!!!!!!!')
# mutable= can not change the value of variable &
# Immutable=  can change the value of variable
# STRING is immutable in nature
str1 = 'Welcome'
print(id(str1))
str1 = str1+" to Python"
print(id(str1))

# EXAMPLE 3
print('EXAMPLE 3   !!!!!!!!!!!')
#  + and * in String
str = 'welcome'
print(str+" to pycharm")
print(str*3)

# EXAMPLE 4
# Slicing []    # slice(start, stop, step)
print('EXAMPLE 4   !!!!!!!!!!!')
str= 'welcome'
print(str[1:5])  # elso
print(str[:5])    #welso
print(str[2:])   #lsome
print(str[:2:-1])  # remove last 2 char  #lco

# EXAMPLE 5  : ord()  and  chr()
print('EXAMPLE 5   !!!!!!!!!!!')
print(ord('B'))  # gives ASKII number   66
print(chr(78))   #  D

# EXAMPLE 6   : min(), max(),  len()
print('EXAMPLE 6   !!!!!!!!!!!')
print(min('IDGKSVDKSV'))  # D
print(max('BUSGDFSDK'))   # U
print(len('FDKSFVSK'))    # 8

# EXAMPLE 7   : in ,   not in operators  -- returns TRUE/FALSE
print('EXAMPLE 7   !!!!!!!!!!!')
s= 'WELCOME'
print('COME' in s)  # TRUE   its case sensative
print('LONE' in s)  # FALSE

print('COME' not in s)  # FALSE
print('LONE' not in s)  # TRUE

# EXAMPLE 8   :   String comparison
print('EXAMPLE 8!!!!!!!!!!!!!')
# compares with char value at each char and length as well
print('tim' == 'tie')  # false
print('free' != 'freedom')   # true
print('arrow' > 'aron')  # true
print('arrow' < 'z')  # true
print('right' >= 'left')  # true


# EXAMPLE 9 : Testing String .... TRUE / FALSE
print('EXAMPLE 9   !!!!!!!!!')
t= 'welcome dd'
print(t.isalnum())   # false
#method checks whether all the characters in a given string are either
# alphabet or numeric (alphanumeric) characters.
print(t.isalpha())   # true
# #The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.

print('6437'.isdigit())  #true

print("welcome java".isidentifier())   # false
# valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_)
#  A valid identifier cannot start with a number, or contain any spaces.

print('WELCOME'.isupper())  # TRUE
print('welcome'.islower())  # True
print(' '.isspace())        # True

# EXAMPLE 10 :    Searching for Substrings
print('EXAMPLE 10  !!!!!!!!')
p= 'welcome to python'
print(p.endswith('thon'))  # true
print(p.startswith('tea'))  # false
print(p.find('come'))     # 3
print(p.find('beco'))     # -1    not found
print(p.count('o'))     # 3   returns the number of substrings in String

# EXAMPLE 11 :  converting the string
print('# EXAMPLE 11 : !!!!!!!!!')
b= 'String in PYTHON'
print(b.capitalize()) # String in python

print(b.title())  # String In Python

print(b.upper())  # STRING IN PYTHON

print(b.lower())   # string in python

print(b.swapcase())  # sTRING IN python   it will convert upper case to lower and vice versa

print(b.replace('in', 'on'))  # String on PYTHON


# EXAMPLE 12 :   Reverse a String
print('EXAMPLE 12!!!!!!!')
# Method 1

s= 'welcome'
rev_str= ' '
for i in s:
    rev_str=i+rev_str
print(rev_str)

# Method 2
s= 'Welcome'
print(s[::-1])  # s[0:7:-1]