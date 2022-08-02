min= int(input("Enter the min value"))
max= int(input("Enter the max value "))

for i in range (min,max+1):
    if i >1 :
        for j in range (2,i):
            if(i%j)== 0:
                break
            else:
                print(i,end=" ")
                break
