word = input()
word_list = list(word.upper())
word_list.sort()

counter = 1
max_count = 1
answer = []

for i in range(len(word_list) - 1):
    if word_list[i] == word_list[i + 1]:
        if counter >= max_count:
            counter += 1
            max_count = counter
            answer.clear()
            answer.append(word_list[i])

        elif counter == max_count - 1:
            counter += 1
            max_count = counter
            answer.append(word_list[i])

        elif counter < max_count:
            counter += 1

    elif word_list[i] != word_list[i + 1]:
        counter = 1

answer_list = list(set(answer))

if len(answer_list) == 1:
    print(answer_list[0])
elif len(answer_list) > 1:
    print("?")
elif len(word_list) == 1:
    print(word_list[0])