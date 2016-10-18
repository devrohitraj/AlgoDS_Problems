# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

lst = []
for i in range(k, n):
    lst.append(a[i])
for i in range(k):
    lst.append(a[i])
for i in lst:
    print i,
