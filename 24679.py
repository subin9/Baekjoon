def RB(num_list: list):
    set1 = num_list[0] + num_list[1]
    if set1 > num_list[2]:
        if sum(num_list) % 4 == 0 or sum(num_list) % 4 == 3:
            return "B"
        else:
            return "R"

    elif set1 < num_list[2]:
        if set1 % 2 == 0:
            return "R"
        else:
            return "B"

    elif set1 == num_list[2]:
        if set1 % 2 == 0:
            return "B"
        else:
            return "R"


T = int(input())
count = 0
answer = []

while count != T:
    count += 1
    num_list = list(map(int, input().split()))
    num_list.sort()
    answer.append(RB(num_list))
    num_list.clear()

for i in answer:
    print(str(i))