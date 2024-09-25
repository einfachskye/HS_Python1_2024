num = input()
str = input()
num_2 = int(input())

result = []

l = str.split()

new_map = map(int, l)
new_list =  list(new_map)

for i in new_list:
    i = i + num_2
    result.append(i)

print(*result)