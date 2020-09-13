with open("2.txt", 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        word_count = len(lines[i].split())
        print(f'В {i+1} строке: {word_count} слов(а).')
    print(f'Всего строк: {len(lines)}')