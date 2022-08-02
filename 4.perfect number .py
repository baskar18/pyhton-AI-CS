Min= int(input("Enter any Minimum Value: "))
Max= int(input("Enter any Maximum Value: "))

print("\nPerfect Number Between {0} to {1}".format(Min,Max))

for i in range(Min,Max - 1):
    Sum = 0
    for n in range(1, i - 1):
        if(i % n == 0):
            Sum = Sum + n

    if(Sum == i):
        print("%d " %i)