def pomme(number):
    """
        sum of digits
    """
    if str(number) > 20:
        return "Error: number too big"
    total = 0
    for digit in str(number):
        total += int(digit)
    if total > 9:
        return pomme(total)
    return total

if __name__ == '__main__':
    print(pomme(123456789123456789))
    print(pomme(12))
    print(pomme(99))
    print(pomme(0))
