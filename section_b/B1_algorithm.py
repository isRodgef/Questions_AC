def selection_sort(number_list):
    resultant_list = []
    for row in number_list:
        if not resultant_list:
            resultant_list.append(int(row))
        else:
            for index, number in enumerate(resultant_list):
                if int(row) <= resultant_list[index]:
                    resultant_list.insert(index, int(row))
                    break
                elif index == len(resultant_list) - 1:
                    resultant_list.append(int(row))
                    break
    return resultant_list


if __name__ == '__main__':
    filename = 'algorithms1.csv'

    number_list = open(filename, 'r')
    resultant_list = selection_sort(number_list)
    print(resultant_list)
    number_list.close()