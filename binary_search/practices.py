def get_binary_search(num, target):
    low , high = 0, len(num) -1
    while low <= high:
        mid = (low + high)//2
        mid_val = num[mid] 
        if mid_val == target:
            return mid
        elif mid_val < high:
            high = mid_val -1
        else:
            low = mid_val +1 
    return -1        
my_number = [1,2,3,4,5,6,7,8,9,10]
target = 9
result = get_binary_search(my_number,target)   

if target != -1:
    print(f"Your target {target} is index of {result}") 
else:
    print(f"We could not find you {target} ")    

