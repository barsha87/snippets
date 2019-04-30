#lifo

class Stack:
    data = []
    idx = []
    def push(self, num):
        count = len(self.data)
        for i in range(count):
            if num > self.data[i]:
                self.data = self.data[:i] + [num] + self.data[i:]
                self.idx = self.idx[:i] + [count+1] + self.idx[i:]
                return
        self.data = self.data + [num]
        self.idx = self.idx + [count+1]


    def pop(self):
        idx = max(self.idx)
        pos = self.idx.index(idx)
        self.idx.pop(pos)
        return self.data.pop(pos)

    def get_min(self):
        #O(1) time and O(1) space
        return self.data[-1]

    def display(self):
        print('Stack: ', end = '')
        for i in range(len(self.idx)):
            pos = self.idx.index(i+1)
            print(self.data[pos], end = ' ')
        print()

st1 = Stack()
q = int(input())
inp = list(map(int, input().split()))
i = 0
while q:
    if inp[i] == 1:
        i += 1
        st1.push(inp[i])
    elif inp[i] == 2:
        print(st1.pop())
    else:
        print(st1.get_min())
    i += 1
    q -= 1
    st1.display()


