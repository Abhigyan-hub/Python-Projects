num1=int(input('enter first number'))
num2=int(input('enter second number'))
print("Prime numbers between {} to {}".format(num1,num2))
for i in range(num1,num2):
    prime=True
    for j in range(2,i):
        if(i%j==0):
            prime=False
    if prime==True:
        print(i)