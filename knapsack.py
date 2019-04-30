"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum
total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights
 associated with N items respectively. Also given an integer W which represents knapsack capacity,
 find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
 You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of four lines.
The first line consists of N the number of items.
The second line consists of W, the maximum capacity of the knapsack.
In the next line are N space separated positive integers denoting the values of the N items,
and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

Output:
For each testcase, in a new line, print the maximum possible value you can get with the given conditions
that you can obtain for each test case in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000

Example:
Input:
1
3
4
1 2 3
4 5 1
Output:
3
"""

def knapsack_v1(n, w, val, wt):
    sum_wts = 0
    select = []
    sum_vals = 0
    for i in range(n):
        if sum_wts + wt[i] <= w:
            select.append(1)
            sum_wts += wt[i]
            sum_vals += val[i]
        else:
            select.append(0)
    return sum_vals, select

def knapsack_v2(n, w, val, wt):
    if w <= 0:
        return 0
    print ('(n, w) ', n, w)
    sum = 0
    if n == 0:
        if wt[0] <= w:
            sum = val[0]
    else:
        for i in range(n):
            sum += max(knapsack_v2(n-1, w-wt[-i], val, wt), knapsack_v2(n-1, w, val, wt))
    print('sum ', sum)
    return sum

def knapsack_greedy(n, w, val, wt):
    val_per_unit = {val[i]/wt[i]:i for i in range(n)}
    total = 0
    while val_per_unit:
        i = val_per_unit.pop(max(val_per_unit))
        if wt[i] <= w:
            total += val[i]
            w -= wt[i]
        # print (total)
    return total

def knapsack(n,w,val,wt):
    dp = []
    for i in range(n+1):
        dp.append([])
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i].append(0)
            elif wt[i-1] <= j:
                dp[i].append(max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]]))
            else:
                dp[i].append(dp[i-1][j])

    return dp[n][w]

"""
1
5
26
24 13 23 15 16
12 7 11 8 9
"""

if __name__ == '__main__':
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        w = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))
        res = knapsack(n, w, val, wt)
        print(res)




