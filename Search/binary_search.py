def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)

        if arr[mid] == target: # if target is in the center of list
            return mid
        
        elif arr[mid] > target: # if if target is less than middle element
            high = mid - 1 # take the first half

        else: # if target is greater than middle element
            low = mid + 1 # take the second half

    return -1

sample_list = [1,2,7,8,9] # sorted list (arr)
target_element = 8 #target

result = binary_search(sample_list,target_element)

if result != -1: # success
    print(f"Element {target_element} is found at {result} index")
else: # failure
    print(f"Element {target_element} is not found")