def remove_vowels(S):
    vowels = "aeiouAEIOU"
    result = "".join([char for char in S if char not in vowels])
    print(result)

S = input()
remove_vowels(S)
