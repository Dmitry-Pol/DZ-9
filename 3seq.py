N = int(input('введите количество элементов будущего списка'))
user_list1 = []
for i in range(N):
    user_list1.append(int(input('введите число')))

N = int(input('введите количество элементов будущего списка'))
user_list2 = []
for i in range(N):
    user_list2.append(int(input('введите число')))

user_list1 = set(user_list1)
user_list2 = set(user_list2)

print(user_list1 - user_list2)