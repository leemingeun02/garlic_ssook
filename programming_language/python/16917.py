A, B, C, X, Y = map(int, input().split(" "))

반반이 제일싸면 반반만 후라이드 양념 중에 더 많은거 만큼 산다
반반 2개가 a랑 b 합친거보다 싸면 반반 + 후라이드만 사거나 반반 + 양념만 산다
반반이 제일 비싸면 후라이드 양념만 개수만큼 산다

if C < A and C < B:
    print((X > Y ? X : Y) * 2 * C)
elif 2 * C < A + B:
    print()
elif C > A and C > B:
    print(A * X + B * Y)