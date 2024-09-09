if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = max(arr)
    arr = [score for score in arr if score != highest]
    runner_up = max(arr)
    print(runner_up)