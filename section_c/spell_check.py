#def levenshtein_distance(s1, s2):
#    # Base cases
#    if len(s1) == 0:
#        return len(s2)
#    if len(s2) == 0:
#        return len(s1)
#    
#    # Calculate the cost of the last character
#    cost = 0 if s1[-1] == s2[-1] else 1
#    
#    # Recursive calls
#    deletion = levenshtein_distance(s1[:-1], s2) + 1
#    insertion = levenshtein_distance(s1, s2[:-1]) + 1
#    substitution = levenshtein_distance(s1[:-1], s2[:-1]) + cost
#    
#    #return substitution
#    # Return the minimum of the three operations
#    return min(deletion, insertion, substitution)

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)


    distance_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        distance_matrix[i][0] = i
    for j in range(n + 1):
        distance_matrix[0][j] = j

    # Calculate the edit distances for each position in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1] + cost

            distance_matrix[i][j] = min(deletion, insertion, substitution)

    # Return the distance at the bottom-right corner of the matrix
    return distance_matrix[m][n]



def fuzzy_search(s, lst, threshold):
    # Create a list of tuples containing the string and its distance
    distances = [(word, levenshtein_distance(s, word)) for word in lst]
    
    # Filter the list to contain only words within the threshold
    return [word for word, distance in distances if distance <= threshold]

if __name__ == '__main__':
    filename = "AvoTest/Test/researchlv2num1.csv"
    word_list = []
    with open(filename, 'r') as f:
        for line in f:
            word_list.append(line.strip())
    #import code; code.interact(local=dict(globals(), **locals()))
    print(fuzzy_search(s="hello", lst=word_list, threshold=2))
    #print(levenshtein_distance('kitten','sitting'))
    #print(levenshtein_distance('rosettacode','raisethysword'))
    #print(levenshtein_distance('kitten','kitten'))
    #print(levenshtein_distance('kitten',''))
    #print(levenshtein_distance('','kitten'))
    #print(levenshtein_distance('kitten','kittens'))
    #print(levenshtein_distance('kittens','kitten'))
    #print(levenshtein_distance('kittens','kittens'))
    #print(levenshtein_distance('kitten','smitten'))
    #print(levenshtein_distance('kitten','mittens'))
