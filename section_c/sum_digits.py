filename = 'AvoTest/Test/researchlv1.csv'
total = 0

with open(filename, 'r') as largenumber:
    for line in largenumber:
        for number in line:
            total += int(number)
print(total)