def longest_increasing_subsequence(a):
    max_subs = [a[0]]
    for i in range(len(a)):
        if len(max_subs) >= len(a)-i-1:
            break
        res = []
        res.append(a[i])
        for j in range(i+1,len(a)):
            if a[j] > res[-1]:
                res.append(a[j])
            if a[j] < res[-1]:
                if len(res)-2 < 0 or a[j]>res[-2]:
                    res[-1] = a[j]
        if len(res) > len(max_subs):
            max_subs = res
    return max_subs


def longest_v2(arr):
    results = [[arr[0]]]
    with open('output.txt', 'w') as f:
        for i in range(1, len(arr)):
            flag = 0
            for res in results:
                if arr[i] > res[-1]:
                    res.append(arr[i])
                    flag  += 1
                elif arr[i] < res[-1]:
                    if len(res) - 2 < 0 or arr[i] > res[-2]:
                        res[-1] = arr[i]
                        flag += 1
            if flag == 0:
                results.append([arr[i]])

            for res in results:
                f.write('%s\n' %(res))
            f.write('\n\n')
    # print("length of result : %s" %len(results))
    max_len = 0
    subs = []
    for res in results:
        if len(res) > max_len:
            max_len = len(res)
            subs = res
    # print(subs)
    return max_len


# binary search in result  for arr[i], if not return end
def binary_search(arr, l, r, key):
    while (r - l > 1):

        m = l + (r - l) // 2
        if (arr[m] >= key):
            r = m
        else:
            l = m
    return r

import pdb
def LongestIncreasingSubsequenceLength(sequence):
    res = []
    prev = []
    idx = []
    res.append(sequence[0])
    idx.append(0)
    prev.append(0)
    for i in range(1, len(sequence)):
        if (sequence[i] > res[-1]):
            # add
            pos = len(res)
            idx.append(i)
            res.append(sequence[i])
        else:
            #replace
            pos = binary_search(res, -1, len(res)-1, sequence[i])
            res[pos] = sequence[i]
            idx[pos] = i
        prev.append(idx[pos-1])

    j = idx[-1]
    for i in range(len(res)-1, -1, -1):
        res[i] = sequence[j]
        j = prev[j]

    return res




import bisect


def longest_increasing_subsequence_v3(sequence):
    P = [0] * len(sequence)
    M = [0] * (len(sequence) + 1)
    L = 0
    for i in range(len(sequence)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if sequence[M[mid]] < sequence[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo

        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL)

    S = [0] * L
    k = M[L]

    for i in range(L - 1, -1, -1):
        S[i] = sequence[k]
        k = P[k]

    return S

def longest_increasing_subsequence_v4(arr):
    # Write your solution here

    dp = []
    par = []
    dp_idx = []

    for i, num in enumerate(arr):
        pos = bisect.bisect_left(dp, num)
        if pos == len(dp):
            #add
            dp_idx.append(i)
            dp.append(num)
        else:
            #replace
            dp[pos] = num
            dp_idx[pos] = i
        # prepare parent index for each num
        par.append(dp_idx[pos - 1])

    idx = dp_idx[-1]
    for i in range(len(dp)-1, -1, -1):
        dp[i] = arr[idx]
        idx = par[idx]
    return dp

inputs = [[16, 3, 5, 19, 10, 14, 12, 0, 15],[16, 3, 5, 19, 10, 14, 12, 0, 15, 1, 2, 3, 4, 5, 6, 7, 8],
          [10, 8, 6, 4, 2, 0], [14]]
with open('input01.txt', 'r') as f:
    inp = f.readlines()
inp = inp[1:]
inputs.append(map(lambda x: int(x.strip()), inp))
# inputs = [[16, 3, 5, 19, 10, 14, 12, 0, 15]]

import time

for j in inputs:
    #print("longest: %s" %longest_increasing_subsequence(j))
    # start = time.time()
    # print("longest my code: %s" % longest_v2(j))
    # end = time.time()
    # print("time:%s" % (end - start))
    # #print("longest: %s" % lis(j))
    start = time.time()
    res = LongestIncreasingSubsequenceLength(j)
    print("longest nlogn: %s: %s" % (len(res), res))
    end = time.time()
    print("time:%s\n\n" %(end - start))
    # start = time.time()
    # res = longest_increasing_subsequence_v3(j)
    # print("longest nlogn: %s: %s" % (len(res), res))
    # end = time.time()
    # print("time:%s\n\n" % (end - start))
    start = time.time()
    res = longest_increasing_subsequence_v4(j)
    print("longest nlogn: %s: %s" % (len(res), res))
    end = time.time()
    print("time:%s\n\n" % (end - start))