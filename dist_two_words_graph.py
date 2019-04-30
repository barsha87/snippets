words = ['cat', 'bat', 'mat', 'tex', 'hex',
        'ser', 'bar', 'dar', 'der', 'mar', 'mer']
# words = ['cat', 'bat', 'mat', 'mar', 'mer',
#         'ser', 'bar', 'dar', 'der', 'hex']

word_next = {}

def dist(w2, w1):
    count = 0
    for i,char in enumerate(w1) :
        if char != w2[i]:
            count += 1
    return count

for w1 in words:
    word_next[w1] = []
    for w2 in words:
        if dist(w1, w2) == 1:
            word_next[w1].append(w2)

from pprint import pprint
pprint(word_next)

def find_steps(w1, w2):
    visited = [w1]
    q = [w1]
    count = {w1:0}
    prev = {w1:None}
    while q:
        w = q.pop(0)
        words = word_next[w]
        for next_w in words:
            if next_w not in visited:
                q.append(next_w)
                visited.append(next_w)
                count[next_w] = count[w]+1
                prev[next_w] = w
                if next_w == w2:
                    return count[next_w], prev
    return None

w1 = 'cat'
w2 = 'ser'
min_steps, prev = find_steps(w1, w2)
_next = w2
i = -1
while _next:
    print(_next, end =" ")
    _next = prev[_next]
    i += 1

print (i)
print(find_steps('cat', 'tex'))
print(find_steps('hex', 'tex'))
print(find_steps('bar', 'ser'))



