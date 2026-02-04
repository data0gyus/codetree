for _ in range(3):
    numbers = list(map(int, input().split()))
    result = [num * 3 for num in numbers]
    print(*result)