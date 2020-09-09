origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [origin_list[i] for i in range(1, len(origin_list)) if origin_list[i - 1] < origin_list[i]]
print(result_list)
