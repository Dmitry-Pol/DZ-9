N = int(input('введите количество элементов будущего списка'))
user_list = []
for i in range(N):
    user_list.append(int(input('введите число')))

print(user_list)
user_list.sort()
print(user_list)