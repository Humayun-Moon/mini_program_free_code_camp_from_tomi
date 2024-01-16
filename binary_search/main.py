# def binary_search (list, element):
#     middle = 0
#     start = 0
#     end = len(list)
#     steps = 0

#     while (start<= end):
#         print("Step", steps, ":", str(list[start:end+1]))
#         steps = steps +1
#         middle = (start + end)//2
        
#         if element ==list[middle]:
#             return middle
#         if element < list[middle]:
#             end = middle -1
#         else:
#             start = middle + 1
#     return -1            
# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]        
# target = 12
# binary_search(my_list,target)   
# print(len(my_list))     


# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         mid_val = arr[mid]

#         if mid_val == target:
#             return mid  # Target found at index mid
#         elif mid_val < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1  # Target not found

# # Example usage:
# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_value = 6

# result = binary_search(sorted_array, target_value)

# if result != -1:
#     print(f"Target {target_value} found at index {result}.")
# else:
#     print(f"Target {target_value} not found in the array.")

def sort_list (number):
    return number.sort()

def binary_search(array, target):
    low,high = 0 , len(array)-1
    # end = len(array) 
    while low <= high:
        mid = (low+high)//2
        mid_val = array[mid] 
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid -1
    return -1
my_number = [10,20,40,30,70,80,50,100,90,60] 
sort_list = sort_list(my_number)
target_value = 80

result = binary_search (my_number, target_value) 
for number in my_number:
    print(number, end="  ")
print()    
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array.")                