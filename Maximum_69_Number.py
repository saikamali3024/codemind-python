number = input()
number_str=str(number)
for i in range(len(number_str)):
    if number_str[i]=='6':
        number_str=number_str[:i]+'9'+number_str[i+1:]
        break
maximum_69_number=int(number_str)
print(maximum_69_number)