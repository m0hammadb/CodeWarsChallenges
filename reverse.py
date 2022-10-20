def reverse(inp):
    if(inp == ""):
        return ""
    return inp[-1] + reverse(inp[:-1])

def isPalindrome(inp):
    if(len(inp) <= 1):
        return True
    if(inp[0] != inp[-1]):
        return False
    return isPalindrome(inp[1:-1])
print(isPalindrome("mamam"))
    