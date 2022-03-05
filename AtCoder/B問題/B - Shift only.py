# 問題へのリンク
# https://atcoder.jp/contests/abc081/tasks/abc081_b

n = int(input())
a = list(map(int, input().split()))

check = True
count = 0
while True:

    for i in range(n):
        if a[i]%2!=0:
            check = False
            break
    if check == False:
        break
    for j in range(n):
        a[j] = a[j]/2
    count += 1

print(count)