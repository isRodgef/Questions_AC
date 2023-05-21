def average(lst):
    total = 0
    for i in lst:
        if not isinstance(i, (int, float)):
            return "Invalid Input"
        total += i      
    return total / len(lst)

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    print(average(test_list))

    test_list2 = [8, 9, 10, 11, 12]
    print(average(test_list2))