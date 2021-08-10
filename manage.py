print('Handling data please wait!')


def split():
    print('splitting data please wait!')
    with open('data.txt', 'rb') as data:
        input_data = data.read()
        data_m1 = input_data.split()
        with open('data.txt', 'wb') as data2:
            for i in range(len(data_m1)):
                data2.write(data_m1[i])
            data2.close()
        data.close()
    print('Done!')
