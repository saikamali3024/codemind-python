number=input()
digit_sum=0
digit_product=1
for digit in number:
    digit_sum +=int(digit)
    digit_product *=int(digit)
if digit_sum == digit_product:
        print("Spy Number")
else:
        print("Not Spy Number")