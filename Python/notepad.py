def median(arr):
    arr = sorted(arr)
    n = len(arr)
    return (sum(arr[n//2-1:n//2+1])/2.0, arr[n//2])[n % 2] if n else None


def median(arr):
    arr = sorted(arr)
    n = len(arr)
    return (sum(arr[n//2-1:n//2+1])/2.0, arr[n//2])[n % 2] if n else None



def activityNotifications(expenditure, d):

    freq = {}
    cnt = 0

    def median(idx):
        cur = 0
        for i in range(201):
            if i in freq:
                cur += freq[i]
            if cur >= idx:
                return i

    for i, v in enumerate(expenditure):

        if i >= d:
            if d % 2 == 0:
                med = 0.5*(median(d//2) + median(d//2+1))
            else:
                med = median(d/2)

            if v >= 2*med:
                cnt += 1

            freq[expenditure[i-d]] -= 1

        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1

    return cnt
