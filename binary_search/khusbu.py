def binary_search(list, target):
    low,top = 0,len(list) -1
    steps = 0
    
    

    while low <= top:
        print(f"Step : {steps} {str(list[low:top+1])}")
        mid = (low + top)// 2
        mid_value = list[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            top = mid -1

    return -1
my_number = [1,2,3,4,5,6,7,8,10] 
for num in my_number:
    print(num, end= " ")
print()    
target = int(input("Enter your target number: "))   

result = binary_search(my_number, target)

if result != - 1:
    print(f"Your tageted number {target} is index of {result}")
else:
    print(f"Your number we couldn't find in the list so try again with valid number")
