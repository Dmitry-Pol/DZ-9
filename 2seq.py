text = input('введите количество элементов будущего списка через запятую (4,5,6,7,8)')
if ',' in text:
    user_list = [int(i) for i in text.split(',')]
elif ';' in text:
    user_list = [int(i) for i in text.split(';')]
elif '/' in text:
    user_list = [int(i) for i in text.split('/')]
print(user_list)
# print(text.split(','))

user_list_set = set(user_list)
print(list(user_list_set))

