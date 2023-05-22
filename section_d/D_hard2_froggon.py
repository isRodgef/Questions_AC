def froogon_representation(n):
    factorial_list = [1]
    i = 2
    while factorial_list[0] <= n:
        factorial_list.insert(0,factorial_list[0] * i)
        i += 1

    representation = []
    temp_n = n
    for factorial in factorial_list:
        count = temp_n   // factorial
        if n >= factorial:
            representation.insert(0,str(count))
        temp_n %= factorial

    return " ".join(representation)


# Test the program
inputs = [18,719, 2100100100]

for number in inputs:
    print("The Froogon representation of", number, "is", froogon_representation(number), ".")
    