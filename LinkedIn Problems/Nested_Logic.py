# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input().strip()
e = raw_input().strip()
act = a.split(" ")
exp = e.split(" ")

if int(act[2]) <= int(exp[2]) and int(act[1]) <= int(exp[1]) and int(act[0]) <= int(exp[0]):
    print 0
elif int(act[2]) > int(exp[2]):
    print 10000
elif int(act[1]) > int(exp[1]):
    print 500 * (int(act[1]) - int(exp[1]))
else:
    print 15 * (int(act[0]) - int(exp[0]))
