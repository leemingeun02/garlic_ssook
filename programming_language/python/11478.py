S = input()

asdf = set()

for i in range(len(S)):
    for j in range(len(S)-i+1):
        asdf.add(S[i:i+j])
print(len(asdf)-1)