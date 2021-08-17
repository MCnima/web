def organize():
    with open('data.txt', 'r', encoding="utf8") as data:
        data_1 = data.read().split(',')
        # print(data_1)
        # print(len(data_1))
        # print(data_1.index('"workingPercent"'))
        # print(data_1[42])
        for i in range((len(data_1) // 48) + 1):
            if data_1[(i+1)*42] != "upTime":
                pass
            else:
                for n in range(8):
                    data_1.insert(((i+1)*42) + n, 'no args here!')
        print(data_1)
        print(len(data_1))


if __name__ == '__main__':
    organize()
