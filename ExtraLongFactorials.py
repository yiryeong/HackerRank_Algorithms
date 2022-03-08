def extraLongFactorials(n):
    answer = 1
    for value in range(2, n+1):
        answer *= value

    print(answer)


print(extraLongFactorials(25))
print(extraLongFactorials(45))
