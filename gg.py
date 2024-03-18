start=int(input("Enter starting number"))
end=int(input("Enter Ending number"))
if start>end:
    print("Starting number cannot be greater than end")
else:
    for i in range(start,end+1):
        if i%2==0:
         print(i," : Even number")
        else:
            print(i," : Odd number")