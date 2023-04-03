# conditional Statements
# if , if .. else,   elif

#Example 1
# A person is eligible for vote Age >= 18

age = 12
if age>=18:
 print("Eligible for vote")   #indentation
else:
    print("Not eligible for vote")

# Example 2
if False:
    print("True condition")
else:
    print("false condition")

# Example 3
if 1:                         # if statements accept only boolean values
    print("one")
else:
    print("not one")

# Example 4  find the number is even or odd num%2==0 --> even

num= 13
if num%2==0:
    print(num,"is even number")
else:
    print(num, "is odd number")

#  Example 5 if else in single line (ternary operator)

num = 16
print("Even number" ) if num%2==0 else print("Odd Number")

#  Example 6 if else,  multiple statement in single line (ternary operator)
num=19
{print("Even"),print("number"), print("1st")} if num%2==0 else {print("Odd"), print("Number"),print("2nd")}


#*****************************************************************************************

# if we have multiple conditions then we can go with elif condition

# Example 7 Multiple Conditions with elif

weekno = 4

if weekno==1:
    print("Monday")
elif weekno==2:
    print("Tuesday")
elif weekno==3:
    print("Wednesday")
elif weekno==4:
    print("Thursday")
elif weekno==5:
    print("Friday")
elif weekno==6:
    print("Saturday")
elif weekno==7:
    print("Sunday")
else:
    print("wrong Input")











