def isPalindrome(self, x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False