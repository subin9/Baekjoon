num_list=list(map(int, input().split()))
num_list.sort()

if num_list[0]==num_list[1]==num_list[2]:
    print(str(10000+num_list[0]*1000))
elif num_list[0]==num_list[1]!=num_list[2]:
    print(str(1000+num_list[0]*100))
elif num_list[0]!=num_list[1]==num_list[2]:
    print(str(1000+num_list[1]*100))
else:
    print(str(num_list[2]*100))
