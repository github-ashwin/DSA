def first_last_sum(num):
    first = int(num[0])
    last = int(num[len(num)-1])
    print(first+last)


N = int(input())
for i in range(N):
    num = input()
    first_last_sum(num)
