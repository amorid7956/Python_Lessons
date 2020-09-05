def int_func(little_str: str):
    temp_list = little_str.split()
    result_list = []
    for word in temp_list:
        big_char = word[0].upper()
        big_char+=word[1:]
        result_list.append(big_char)
    result = ' '.join(result_list)
    return result

user_str = input('Введите вашу строку из слов: ')
print(int_func(user_str))
