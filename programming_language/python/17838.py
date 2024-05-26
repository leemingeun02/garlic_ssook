import sys

T = int(sys.stdin.readline())
for i in range(T):
    command = sys.stdin.readline().rstrip()
    if len(set(command)) != 2:
        print(0)
        continue
    A, B =  set(command)
    if command == "%s%s%s%s%s%s%s" % (A,A,B,B,A,B,B) or command == "%s%s%s%s%s%s%s" % (B,B,A,A,B,A,A) :
        print(1)
    else:
        print(0)