# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):
    r = ""
    if len(s) == 1:
        return s + "1"
    if len(s) == 0:
        return ""
    
    last = s[0]
    count = 1 
    idx = 1
    
    while idx < len(s):
        if s[idx] == s[idx-1]:
            count +=1
        else:
            r = r + s[idx-1] + str(count)
            count  = 1
        idx +=1
    r = r + s[idx-1] +str(count)
    return r
