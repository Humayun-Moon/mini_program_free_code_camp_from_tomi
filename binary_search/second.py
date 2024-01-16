def binary_search (list, target):
    start = 0
    middle = 0
    steps =0
    end = len(list)

    while (start<=end):
        print("Step", steps, ":", str(list[start:end+1]))
        steps  = steps + 1
        middle = (start+end) // 2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle -1
        else:
            start = middle + 1
    return -1   
try:
    while True:
        my_list = [1,2,3,4,5,6,7,8,9,10] 
        for i in my_list:
            print(i, end= " ")
        print()    
        targets = int(input("Enter you target number : "))
        # binary_search(my_list, targets)   
        result = binary_search(my_list, targets)
        print(f"Your targeted {targets} in index of {result}") 
        

except IndexError as e:
        print(e) 
        print("Try with another number")     
    

# if result in my_list:
#     print("Your tageted number is not in List")
# else:
#     print(f"Your targeted {targets} is index of {result}")    
   
                