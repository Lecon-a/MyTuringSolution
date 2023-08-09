def solution(list_n, x):
    res = []
    i = 0
    n = 0
    limit = 0
    count = 0

    while i <= len(list_n):
        if limit == len(list_n):
            i = -1
            res.append(int(list_n[i+1]) + int(list_n[i+2]))
            break
        # case 1
        if x > 0:
            limit = i + 2
            n = i
            if i == len(list_n)-2:
                n = -2
            res.append(int(list_n[i+1]) + int(list_n[n+2]))
        # case 2
        elif x < 0:
            count += 1
            if count > len(list_n):
                break
            n = i
            if i == len(list_n)-1:
                i -= 1
                n += 1
            res.append(int(list_n[i]) + int(list_n[n-1]))
        # case 3
        else:
            if i == len(list_n):
                break
            res.append(0)

        i += 1

    return res
    
print("Enter array of numbers with space in between: ", end="")
numbers = input().split(" ")
print("Enter the value of x: ", end="")
threshold = int(input())
print(solution(numbers, threshold))