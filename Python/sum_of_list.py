my_list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    a = int(input("Enter the number: "))
    my_list.append(a)

print("List:", my_list)
print("Sum of the elements in the list:", sum(my_list))


def max_num_list(lst):  
    max_num = lst[0] 
    for a in lst:  
        if a > max_num:  
            max_num = a
    return max_num

print("Maximum number in the list:", max_num_list(my_list))  
