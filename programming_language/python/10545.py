integer_list = list(map(int, input().split()))
word = input()

dial = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
answer = ''

for i in word:
    for j in range(10):
        if i in dial[j]:
            for k in range(len(dial[j])):
                if i == dial[j][k]:
                    answer = answer[] + (j*k) # 샵추가하게끔 고칠것

print(answer)

# integer_list와 일대일대응으로 고쳐서 출력하게끔