print('Handling data please wait!')


def split():
    print('splitting data please wait!')
    with open('data.txt', 'rb') as data:
        input_data = data.read()
        splited_data = input_data.split()
        with open('data.txt', 'wb') as data_2:
            for i in range(len(splited_data)):
                data_2.write(splited_data[i])
            data_2.close()
        data.close()
    print('Done!')


def lister():
    with open('data.txt', 'r', encoding="utf8") as data_3:
        listed_data = data_3.read()
        listed_data = listed_data[8:-38]
        print(listed_data)
        with open('data.txt', 'w', encoding="utf8") as data_4:
            data_4.write(listed_data)
            data_4.close()
        data_3.close()
