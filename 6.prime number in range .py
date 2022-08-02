min= int(input (" Enter the minmum Value: "))  
max = int(input (" Enter the maximum Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for num in range (min, max + 1):  
    if num > 1:  
        for j in range (2, num):  
            if (num % j) == 0:  
                break  
        else:  
            print (num)  