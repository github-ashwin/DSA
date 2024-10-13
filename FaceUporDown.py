T = int(input())

for i in range(T):
    
    N,X = map(int,input().split())
    result = min(X,N-X)
    print(result)