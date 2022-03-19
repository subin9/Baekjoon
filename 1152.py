sen = input()

count = 1

for i in sen:
    if i == " ":
        count += 1

if sen[0] == " ":
    count -= 1
if sen[-1] == " ":
    count -= 1

print(count)