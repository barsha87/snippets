
class Queens:

    def __init__(self, n):
        self.n = n
        self.arr = [[0]*n for _ in range(n)]
        self.placed = []
        self.solved = 1

    def place_queens(self):
        i = 0
        while i < self.n:
            j = self._place_queen_row(i)
            while j == None:
                i -= 1
                if i < 0:
                    self.solved = 0
                    return
                j = self._place_queen_row(i, self.placed.pop())
            self.placed.append(j)
            i += 1

    def _place_queen_row(self, i, start=-1):
        if not start == -1:
            self.arr[i][start] = 0
        for j in range(start+1, self.n):
            if self._is_safe(i, j):
                self.arr[i][j] = 1
                return j
        return None

    def _is_safe(self, x, y):

        i, j = x-1, y
        while i >= 0:
            if self.arr[i][j]:
                return False
            i -= 1

        i, j = x-1, y-1
        while i >= 0 and j >= 0:
            if self.arr[i][j]:
                return False
            i -= 1
            j -= 1

        i, j = x-1, y+1
        while i >= 0 and j < self.n:
            if self.arr[i][j]:
                return False
            i -= 1
            j += 1

        return True

    def display(self):
        if self.solved:
            for i in range(self.n):
                print(' '.join(map(str, self.arr[i])))
        else:
            print('No solution')


q1 = Queens(2)
q1.place_queens()
q1.display()
print()

q1 = Queens(3)
q1.place_queens()
q1.display()
print()

q1 = Queens(4)
q1.place_queens()
q1.display()
print()

q1 = Queens(8)
q1.place_queens()
q1.display()
print()

q1 = Queens(10)
q1.place_queens()
q1.display()





