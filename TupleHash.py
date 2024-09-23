# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

num = map(int, input().split())
t = tuple(num)
print(hash(t))

