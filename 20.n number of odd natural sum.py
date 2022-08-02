min = int(input(" Please Enter the Maximum Value : "))
Odd = 0
sum=0

for number in range(min):
    if(number % 2 != 0):
        print(number)
        sum= sum+number
print(f"the sum of odd values ",sum)
