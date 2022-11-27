N = int(input())

def hansu(N) :
    ans = 0
    for k in range(1, N+1) :
        arr = str(k)
        if len(arr) > 2 :
            dif = int(arr[0]) - int(arr[1])
            for i in range(1, len(arr)-1) :
                if int(arr[i]) - int(arr[i+1]) == dif :
                    ans += 1
        else :
            ans += 1
    return ans

print(hansu(N))
