def linear_search(arr, target):

    limit = len(arr) #list size

    for i in range(limit):

        if i == target: # if target is obtained
            return i
        
    return -1

sample_list = [8,1,2,9,7] # list (arr)
target_element = 2 #target
result = linear_search(sample_list,target_element)

if result != -1: # success
    print(f"Element {target_element} is found at {result} index")
else: # failure
    print(f"Element {target_element} is not found")
