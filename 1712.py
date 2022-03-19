fix, mov, pri=map(int, input().split())
pro=pri-mov
if pro>0:
    print(int(fix/pro)+1)
else:
    print(-1)
