origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [origin_list[i] for i in range(len(origin_list)) if origin_list.count(origin_list[i]) == 1]
print(result_list)