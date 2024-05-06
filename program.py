def find_consec(target, arr):
    n = len(arr)
    consec = {}
    count = 1
    pos = 0

    for i in range(n-1):
        if(arr[i]==arr[i+1]):
            count += 1
        else:
            consec[pos] = (arr[i], count)
            count = 1
            pos = i+1
    new_consec = {}
    for key,val in consec.items():
        if val[1]>=3 and val[0]!=target:
            new_consec[key] = val
    return new_consec
