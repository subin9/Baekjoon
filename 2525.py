h, m = map(int, input().split())
req_t = int(input())

end_time = 60 * h + m + req_t

if end_time >= 1440:
    end_time -= 1440

ans_t, ans_m = divmod(end_time, 60)
print(ans_t, ans_m)
