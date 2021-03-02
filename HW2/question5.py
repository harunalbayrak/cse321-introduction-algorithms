def question5(array1,array2):
    min_arr = []
    max_arr = []
    myset = set()
    if len(array1) > len(array2):
        min_arr = array2
        max_arr = array1
    else:
        min_arr = array1
        max_arr = array2
        
    for x in min_arr:
        myset.add(x)
        
    for y in max_arr:
        if(y in myset):
            print(y, "was found the both array.")
    
array1 = [1,2,3,4,5]
array2 = [2,5,10,15,20,25,30,40]
question5(array1,array2)