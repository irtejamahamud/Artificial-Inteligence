thislist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
evencount=0
oddcount=0
for x in thislist:
    if x%2==0:
        evencount+=1
    else:
        oddcount+=1
print(f"There are {evencount} Even number in the list")
print(f"There are {evencount} Odd number in the list")