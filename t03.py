
aList = [1,2,3,4,5]

def mySum(a,b,c):
    print("In mySum:")
    aa = a + b
    bb = b + c
    cc = c + a

    #StepOut
    aList[3] = 120

    dd = aa + bb + cc
    print("Out mySum!")

    return dd//2


def myDiv( a ,b ):
    print("In myDiv:")

    aa = a % b

    aList[1] = 100

    return aa

    print("Out myDiv!")


def  mySub(a,b,c):
    print("In mySub:")

    aa = a - b
    bb = b - c

    aList[0] = 300

    cc = aa - bb


    print("Out mySub!")

    return cc


A = 3.4
B = 5.8
C = 9.3


AA = A + B
print(AA)

#StepInto, ForceStepInto
BB = mySum(A,B,C)
print(BB)


#For SmartStepInto
EE = mySum(A,B,myDiv(A,B))

DD = mySub(A,B,C)
print(DD)

#RunToCursor
CC = A + B + C
print(CC)