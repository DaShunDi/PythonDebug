print("Just test errors in running ... ...")

a = input("Plz input a mumber: ")

print("The number is : %d" %int(a))

print("and then we open a file : ")

fName = input("Input the file path:")

fh = open(fName)

print(fh.read())