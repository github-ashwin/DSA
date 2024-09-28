def display_result(array):
    size = len(arr)
    
    for i in range(size):
        for j in range(i,size):
            print(' '.join(map(str,arr[i:j+1])))

T = int(input())

for i in range(T):
    N = int(input())
    if N>1 and N<20:
        arr = list(map(int,input().split()))
        display_result(arr)


def display_result(array):
    size = len(arr)
    
    for i in range(size):
        for j in range(size):
            print(''.join(map(str,arr[i:j+1])))