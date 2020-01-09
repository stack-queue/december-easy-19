num_testcases = int(input())

for i in range(num_testcases):
    testcase = input().split()
    n = int(testcase[0])
    k = int(testcase[1])
    string = input()

    arr = [1]
    for i in range(len(string)):
        total = 0
        j = i
        while(j >= 0):
            if(int(string[j:i + 1]) < k):
                total = (total + arr[j]) % (10 ** 9 + 7)
            else:
                break
            j -= 1
        arr.append(total)
        
    print(arr[-1] % (10 ** 9 + 7))
