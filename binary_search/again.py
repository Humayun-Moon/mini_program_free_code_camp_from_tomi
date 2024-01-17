name = input("Enter your name: ")
print(f"Hey {name}, Welcome to binary search") 

def binary_search(list, target):
    low,high = 0, len(list) - 1 
    steps = 0

    while low <= high:
        print(f"step: {steps} {str(list[low:high+1])}")
        mid = (low+high)//2
        mid_value = list[mid] 

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid_value -1
    return -1
my_number = [1,2,3,4,5,6,7,8,9,10]
goal = 11
result =  binary_search(my_number,goal)       
print(result)    