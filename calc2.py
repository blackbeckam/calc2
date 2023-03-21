firstnumber=float(input("enter firstnumber:"))
secondnumber=float(input("enter secondnumber:"))
myoperator=str(input("enter operator(+,-,*/)"))


if myoperator=="+":
    print(firstnumber+secondnumber)
elif myoperator=="-":
    print(firstnumber-secondnumber)
elif myoperator=="*":
    print(firstnumber*secondnumber)
elif myoperator=="/":
    print(firstnumber/secondnumber)
else:
    print("invalid number")
