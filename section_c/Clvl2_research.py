def levenshtein_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    distance_matrix = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        distance_matrix[i][0] = i
    for j in range(len_s2 + 1):
        distance_matrix[0][j] = j

    for row in range(1, len_s1 + 1):
        for column in range(1, len_s2 + 1):
            cost = 0 if s1[row - 1] == s2[column - 1] else 1

            deletion = distance_matrix[row - 1][column] + 1
            insertion = distance_matrix[row][column - 1] + 1
            substitution = distance_matrix[row - 1][column - 1] + cost

            distance_matrix[row][column] = min(deletion, insertion, substitution)

    return distance_matrix[len_s1][len_s2]




def fuzzy_search(s, lst, threshold):
    # Create a list of tuples containing the string and its distance
    distances = [(word, levenshtein_distance(s, word)) for word in lst]
    
    # Filter the list to contain only words within the threshold
    return [word for word, distance in distances if distance <= threshold]

if __name__ == '__main__':
    filename = "researchlv2num1.csv"
    word_list = []
    with open(filename, 'r') as f:
        for line in f:
            word_list.append(line.strip())
    print(fuzzy_search(s="hello", lst=word_list, threshold=2))
