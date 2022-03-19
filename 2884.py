h, m = map(int, input().split())
end_time = 60 * h + m - 45

if end_time < 0:
    end_time += 1440

ans_t, ans_m = divmod(end_time, 60)
print(ans_t, ans_m)

