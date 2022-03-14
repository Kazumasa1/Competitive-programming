N, A, B = map(int,input().split())


N_str = str(N)
# Nの桁数を調べる
N_len = len(N_str)

# for i in N_len:

ans_list = []

for i in range(N+1):
    i_str = str(i)
    # iの桁数を調べる
    i_len = len(i_str)

    i_sum = 0
    # 格桁の和を求める
    for j in range(i_len):
        i_sum += int(i_str[j])
    
    i_sum_int = i_sum

    if A <= i_sum_int and i_sum_int <= B:
        ans_list.append(i)

ans = 0
for k in range(len(ans_list)):
    ans += ans_list[k]

print(ans)

