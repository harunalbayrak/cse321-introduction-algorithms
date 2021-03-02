def question1(set, n, sum):
    _s =[[False for i in range(sum + 1)]
        for i in range(n + 1)]
    for i in range(n + 1):
        _s[i][0] = True
    for i in range(1, sum + 1):
        _s[0][i]= False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                _s[i][j] = _s[i-1][j]
            if j>= set[i-1]:
                _s[i][j] = (_s[i-1][j] or _s[i - 1][j-set[i-1]])
    
    return _s[n][sum]
    
set = [2, 3, -5, -8, 6, -1]
sum = 0
n = len(set)
if (question1(set, n, sum) == True):
    print("Yes. There is a subset that sum of the elements is " + str(sum))
else:
    print("No")