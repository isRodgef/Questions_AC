filename = 'AvoTest/Test/algorithms1.csv'
resultant_list = []
with open(filename, 'r') as nummber_list:
    for row in nummber_list:
        if not resultant_list:
            resultant_list.append(int(row))
        else:
            for i in range(len(resultant_list)):
                if int(row) <= resultant_list[i]:
                    resultant_list.insert(i, int(row))
                    break
                elif i == len(resultant_list) - 1:
                    resultant_list.append(int(row))
                    break



print(resultant_list)