# max contiguous sum of arrays

def maxsum(a):
    max_arr = [a[0]]
    for i in range(1, len(a)):
        max_arr.append(max(a[i], max_arr[i-1]+a[i]))
    return max(max_arr)

if __name__ == '__main__':
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxsum(arr))


"""
3
5
1 2 3 -2 5
4
-1 -2 -3 -4
8
-25 36 19 25 17 -1 -2 15


output
109
9
1

"""