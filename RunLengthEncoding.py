def run_length(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
            
    result = ""
    for char in count:
        result += char + str(count[char])
    
    print(result)
    
s = input()
run_length(s)