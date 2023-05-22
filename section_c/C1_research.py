def sum_digits(iterable):
    total = 0
    for line in iterable:
        total += int(line)
    return total

if __name__ == '__main__':
    filename = 'AvoTest/Test/researchlv1.csv'
    iterable = open(filename, 'r') 
    total = sum_digits(iterable)
    print(total)
    iterable.close()