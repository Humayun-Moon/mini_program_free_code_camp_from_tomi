
def binary_search(num, target):
    low,top = 0, len(num) -1
    while low <= top:
        mid = (low+top)//2
        mid_num = num[mid]

        if mid_num == target:
            return mid
        elif mid_num < target:
            low = mid + 1
        else:
            top = mid -1
    return -1
list = [100,120,130,110,150,140,1000, 500]
def sort(number,n):
    number.sort()
    return number[:-n]
print("Below the sorted: List")
for i in list:
    print(i, end= " ") 
print()    
highest = sort(list, 2)
print(f"Your highest number of list: {highest}")  

target = int(input("Enter your targeted number from list : "))
result = binary_search(list,target) 
while True:
    if result != -1:
        print(f"Your target {target} is index of {result}")
        break
    else:
        print(f"We couldn't find your target {target} if you want try again")  
        continue  


