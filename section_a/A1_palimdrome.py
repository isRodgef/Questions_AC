def palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print (palindrome('racecar'))
    print (palindrome('racecars'))
    print (palindrome('r'))
    print (palindrome('123454321'))