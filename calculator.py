print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")
print("5.modulas")
print("6.exit")

n=int(input(" enter which thing you want to do:"))

if(n==1):
    add=eval(input(" enter the numbers:"))
    print(" the reasult is=",add,".")

elif(n==2):
    sub = eval(input(" enter the numbers:"))
    print(" the reasult is=", sub, ".")

elif(n==3):
    mul = eval(input(" enter the numbers:"))
    print(" the reasult is=", mul, ".")

elif(n==4):
    div = eval(input(" enter the numbers:"))
    print(" the reasult is=", div, ".")

elif(n==5) :
    mod = eval(input(" enter the numbers:"))
    print(" the reasult is=", mod, ".")

else:
    print(" thank you ! you choose the wrong one.")

print("thanks for using our code")
