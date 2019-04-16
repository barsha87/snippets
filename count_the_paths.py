from pprint import pprint

# global result
def paths_v2(grid, i, j):
    if result[i][j] != -1:
        return result[i][j]
    else:
        if grid[i][j]== 1:
            result[i][j] = 0
            return result[i][j]

        n = len(grid)
        if j == 0 and i == n-1:
            result[i][j] = 1
        elif j == 0:
            result[i][j] = paths_v2(grid, i+1, j)
        elif i == n-1:
            result[i][j] = paths_v2(grid, i, j-1)
        else:
            result[i][j] = paths_v2(grid, i, j-1) + paths_v2(grid, i+1, j)
        return result[i][j]

def paths_v1(grid, i, j):
    if grid[i][j]== 1:
        return 0
    n = len(grid)
    if j == 0 and i == n-1:
        return 1
    elif j == 0:
        return paths_v1 (grid, i+1, j)
    elif i == n-1:
        return paths_v1(grid, i, j-1)
    else:
        return paths_v1(grid, i, j-1) + paths_v1(grid, i+1, j)


def count_the_paths(grid):
    # global result
    n = len(grid)
    m = len(grid[0])
    result = [[-1 for j in range(m)] for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j] == 1:
                result[i][j] = 0
            else:
                if j == 0 and i == n - 1:
                    result[i][j] = 1
                elif j == 0:
                    result[i][j] = result[i + 1][j]
                elif i == n - 1:
                    result[i][j] = result[i][j - 1]
                else:
                    result[i][j] = result[i][j - 1] + result[i + 1][j]
    return result[0][m - 1] % 1000003


grid = [[1,0,0,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [0,0,1,0,0],
        [0,1,0,0,0]]
print(count_the_paths(grid))
# pprint(result)