def to_bin(a):
    aint = int(a)
    stringa = str(bin(aint))
    count = stringa.count("1")
    return count


N, K = map(int, input().split())
cur_bot = N
wat_per = 1
buy_bot = 0

while K < to_bin(cur_bot):
    if cur_bot % 2 == 0:
        cur_bot /= 2
        wat_per *= 2  # 병당 물 증가

    else:  # 병이 홀수
        cur_bot += 1  # 병을 구입
        buy_bot += wat_per  # 카운트

print(buy_bot)