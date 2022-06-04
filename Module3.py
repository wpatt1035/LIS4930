# Module 3 
#-------------------------------------------------------------------------------------------------------
# Author: Will Patterson
# Global Variables
PeopleList = ("Will", "Alex", "Joe")
PeopleDict = [{"First":"Will","Last":"Smith"},{"First":"Alex","Last":"Jones"},{"First":"Joe","Last":"Ryan"}]
NumberList = [(33,44),(44,55),(66,77)]
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = [21, 22, 23, 24, 25]

# Simple function taking an argument and printing various messages
def simple_name_function(inputName):
    print("Hello " + inputName + "welcome ")
    print(inputName + " What do you like to do for fun?")
    print("Nice to meet you, " + inputName + "")

# Full name function
def full_name_function(inputName):
    first = inputName["First"]
    last = inputName["Last"]
    print("Hello " + first + " " + last + "")


#Simple Number Function
def simple_number_function(inputInt):
    sum = inputInt[0] + inputInt[1]
    print("Total for # " + str(inputInt[0]) + " plus " + str(inputInt[1]) + " equals: " + str(sum))


#Modified Number Function
def modified_number_function(inputInt):
  
    sum = inputInt[0] + inputInt[1]
    return sum

import math
def module_3_question_2():
    print("POW: " + str(pow(16,(1/2))))
    print("Math.sqrt: " + str(math.sqrt(16)))


def module_3_question_3(x, y, z):

    # 3 * x
    x3 = 0
    for num in x:
        x3 += (3 * num)

    # 3 * z
    z3 = 0
    for num in z:
        z3 += (3 * num)

    # x + y
    xySum = 0
    xySub = 0
    xSum = 0
    ySum = 0
    for num in x:
        xSum += num 
    for num in y:
        ySum += num
    xySum = (xSum + ySum)
    xySub = (xSum - ySum)

    # z + y
    zySum = 0
    zySub = 0
    zSum = 0
    ySum = 0
    for num in z:
        zSum += num 
    for num in y:
        ySum += num
    zySum = (zSum + ySum)
    zySub = (zSum - ySum)

    print("What is the value of 3*x? Answer: " + str(x3))
    print("What is the value of x+y? Answer: " + str(xySum))
    print("What is the value of x-y? Answer: " + str(xySub))
    print("What is the value of x[1]? Answer: " + str(x[1]))
    print("What is the value of x[0]? Answer: " + str(x[0]))
    print("What is the value of x[-1]? Answer: " + str(x[-1]))
    print("What is the value of x[:]? Answer: " + str(x[:]))
    print("What is the value of x[2:4]? Answer: " + str(x[2:4]))
    print("What is the value of x[1:4:2]? Answer: " + str(x[1:4:2]))
    print("What is the value of x[:2]? Answer: " + str(x[:2]))
    print("What is the value of x[::2]? Answer: " + str(x[::2]))
    print("What is the result of the following two expressions? x[3]=8 Answer: " + str(x[3]))
    print("What is the result of the above pair of expressions if the list x were replaced with the tuple z? Answers: ")
    print("What is the value of 3*z? Answer: " + str(z3))
    print("What is the value of z+y? Answer: " + str(zySum))
    print("What is the value of z-y? Answer: " + str(zySub))
    print("What is the value of z[1]? Answer: " + str(z[1]))
    print("What is the value of z[0]? Answer: " + str(z[0]))
    print("What is the value of z[-1]? Answer: " + str(z[-1]))
    print("What is the value of z[:]? Answer: " + str(z[:]))
    print("What is the value of z[2:4]? Answer: " + str(z[2:4]))
    print("What is the value of z[1:4:2]? Answer: " + str(z[1:4:2]))
    print("What is the value of z[:2]? Answer: " + str(z[:2]))
    print("What is the value of z[::2]? Answer: " + str(z[::2]))
    print("What is the result of the following two expressions? z[3]=8 Answer: " + str(z[3]))

for person in PeopleList:
    simple_name_function(person)

for person in PeopleDict:
    full_name_function(person)

for numbers in NumberList:
    simple_number_function(numbers)

for numbers in NumberList:
    sum = modified_number_function(numbers)
    print("Total for " + str(numbers[0]) + " plus " + str(numbers[1]) + " equals: " + str(sum))

module_3_question_2()
module_3_question_3(x, y, z)