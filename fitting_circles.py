import math

num_testcases = int(input())

for i in range(num_testcases):
    testcase = input().split()
    length = int(testcase[0])
    width = int(testcase[1])
    if length >= width:
        result = length / width
        if not result.is_integer():
            result = math.floor(result)
    elif width > length:
        result = width / length
        if not result.is_integer():
            result = math.floor(result)
    print(int(result))
