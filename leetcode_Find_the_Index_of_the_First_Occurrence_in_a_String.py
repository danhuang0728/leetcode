needle = "abc"
haystack = "dcgaw"
def strStr( haystack, needle):
    x = len(needle)
    for i in range(len(haystack)):
        print(haystack[i:i+x])
        if needle == haystack[i:i+x]:
            return i 
    return -1
print(strStr(haystack, needle))