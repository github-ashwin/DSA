T = int(input())
if 1 <= T <= 1000:
    for _ in range(T):
        N = int(input())
        n = N
        r = 0

        
        while n != 0:
            d = n % 10
            r = r * 10 + d
            n = n // 10  

        
        if N == r:
            print("Yes")
        else:
            print("No")
