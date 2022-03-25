from mimetypes import init


"""

The program will depict two options and determine which of the two options offer a greater pay rate. Option 1 offers $100 per day while option 2 offers incremental amounts (x2) over a certain time period (10 days)

Option 1 will output 1000 because $100 * 10 days
option 2 is a double multiplier over a 10 day period. 
(1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512)
A for loop can iterate from 1 to 10 and the total sum can be saved in a variable called temp

If options 1 and 2 are similar then the output will be "Both options are similar"
Otherwise options 1 or 2 will output depending on which option offers a greater pay rate





"""


"""
#option 1
option1 = 100 * 10

#option 2
option2 = 0
temp = 1  #this will act as a placeholder

for loop 10 times
    temp will be x2 for each increment of i
    add total amount to option2

if options 1 and 2 are equal, print "Option 1 and 2 are equal"
else if option1 > option2, print "Option 1 is the better option"
else "Option 2 is the better option"

"""

#option1
option1 = 100 * 10

#option2
option2 = 0
temp = 1  #placeholder
for i in range(1, 10):
    temp *= 2
    option2 += temp

print(f"Option 1 : {option1}")
print(f"Option 2: {option2}")

if option1 == option2:
    print("Option 1 and Option 2 pays the same")
elif option1 > option2:
    print("Option 1 is better")
else:
    print("Option 2 is better")