s = "abcdd"

print(s[3:4])

def is_special(s):
        if len(set(s))==1:
            return True
        elif len(s)%2==1 and len(set(s))==2 and len(set(s[:len(s)//2]+s[len(s)//2+1:]))==1:
            return True
        else:
            return False

    cnt = n

    for i in range(n-1):
        for j in range(2, n-i+1):
            if len(set(s[i:i+j]))>2:
                continue
            if is_special(s[i:i+j]):
                cnt += 1
    return cnt
