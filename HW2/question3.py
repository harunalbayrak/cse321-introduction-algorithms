from bisect import bisect_left 
  
def BinarySearch(arr, x): 
    i = bisect_left(arr, x) 
    if i != len(arr) and arr[i] == x: 
        return i 
    else: 
        return -1

def question3(array,number):
    array.sort()
    listx = []
    listy = []
    for x in range(0,len(array)):
        m = number / array[x]
        res = BinarySearch(array, m) 
        if res != -1: 
            listx.append(array[x])
            listy.append(array[res])
            
    for x in range(0,len(listx)):
        print("Pair:(",listx[x],",",listy[x],")")
            
       
    
array = [1,2,3,6,5,4]
question3(array,6)
