a=int(input())
b=0
for i in range(1,a-1):
   if a%i==0:
       b=b+i
if b==a:
       print("True")
else:
       print("False")