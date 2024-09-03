def check_long(s):
    length = len(s)
    if length > 10:
        abr = length - 2
        result = s[0] + str(abr) + s[-1]
        return result
    else:
        return s

t = int(input())
for i in range(t):
    s = input()
    print(check_long(s))