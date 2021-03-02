def question2(A): 
    memo = [None] * len(A) 
    n = len(A) - 1
    for i in range(len(A[n])):  
        memo[i] = A[n][i]  
    for i in range(len(A) - 2, -1,-1):  
        for j in range( len(A[i])):  
            memo[j] = A[i][j] + min(memo[j], 
                                    memo[j + 1]); 
  
    return memo[0] 

array = [[ 2 ], 
        [5, 4 ], 
        [1, 4, 7 ],
        [8, 6, 9 ,6]] 
print(question2(array)) 