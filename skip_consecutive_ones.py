n = int(input())
a = [1,1]
for i in range(2,n+1):
    a.append(a[i-1] + a[i-2])

print('ans = ' ,a[-1]+a[-2])

#[1,1,2,3,5,8]
#
# f1(1) = 1
# f0(1) = 1
#
# f0(n) = f0(n-1)+ f1(n-1)
# f1(n) = f0(n-1)

a = [1]
b = [1]

for i in range(1,n):
    a.append(a[i-1]+b[i-1])
    b.append(a[i-1])

print(a[-1]+b[-1])


