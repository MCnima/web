def organize():
    with open('data.txt', 'r', encoding="utf8") as data:
        main_list = data.read()
        main_list = main_list.split(',')
        print(main_list[:3])


if __name__ == '__main__':
    organize()
