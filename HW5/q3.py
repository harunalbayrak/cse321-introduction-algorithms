def question3(W, wt, val, n): 
    array = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                array[i][w] = 0
            elif wt[i-1] <= w: 
                array[i][w] = max(val[i-1] 
                          + array[i-1][w-wt[i-1]],   
                              array[i-1][w]) 
            else: 
                array[i][w] = array[i-1][w] 
   
    return array[n][W] 
   
values = [10, 4, 3] 
weights = [5, 4, 2] 
W = 9
n = len(values) 
print(question3(W, weights, values, n))