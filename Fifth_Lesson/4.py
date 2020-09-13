my_digits = {'One': 'Один',
             'Two': 'Два',
             'Three': 'Три',
             'Four': 'Четыре'
             }
with open("4.txt", "r") as f, open("4_new.txt", "w") as ff:
    for line in f:
        sub_lines = line.split(' - ')
        if sub_lines[0] in my_digits:
            sub_lines[0] = my_digits[sub_lines[0]]
            ff.write(' - '.join(sub_lines))
