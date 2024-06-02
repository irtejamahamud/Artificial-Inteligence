thistuple = ("irteja","mahmud",213902016)
print(thistuple)
print(len(thistuple))
print(thistuple[1])

x=("apple","banana","mango")
y=list(x)
y[1]="kiwi"            #convert tuple into list to change the item
x=tuple(y)
print(x)

i=0
print("Using Loop")
while i<len(x):
    print(x[i])
    i+=1

