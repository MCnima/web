# import time


def condition():
    print('Handling data please wait!')
    # time.sleep(1)
    print('Done!')


def proses_data():
    with open('data.txt', 'rb') as data_1:
        proses_1 = data_1.read()
        proses_2 = proses_1[10:-40]
        proses_3 = [proses_2]
        with open('data.txt', 'wb') as data_2:
            for i in range(len(proses_3)):
                data_2.write(proses_3[i])
            data_2.close()
        data_1.close()

    with open('data.txt', 'r', encoding="utf8") as data_3:
        main_list = data_3.read()
        main_list_2 = main_list.replace(':', ',').split(',')
        with open('data.txt', 'w', encoding="utf8") as data_4:
            for arg in range(len(main_list_2)):
                data_4.write(main_list_2[arg]+',')
            # print(main_list_2[0:3])
            # print(main_list_2)
            data_4.close()
        data_3.close()


if __name__ == '__main__':
    condition()
    proses_data()
