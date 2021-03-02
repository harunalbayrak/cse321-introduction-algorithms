swap_quick_sort = 0
swap_insertion_sort = 0

def insertion_sort(arr, low, n): 
    global swap_insertion_sort
    for i in range(low + 1, n + 1): 
        val = arr[i] 
        j = i 
        while j>low and arr[j-1]>val:
            swap_insertion_sort += 1
            arr[j]= arr[j-1] 
            j-= 1
        arr[j]= val
        
def partition(arr, low, high):
    global swap_quick_sort
    i = (low-1)       
    pivot = arr[high] 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            swap_quick_sort += 1
            arr[i], arr[j] = arr[j], arr[i]
    swap_quick_sort += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

        
array = [-5,-3,4,2,25,67,0,-2,6,42,10,3,-7,3,6,7,1]
array2 = [-5,-3,4,2,25,67,0,-2,6,42,10,3,-7,3,6,7,1]
insertion_sort(array, 0, len(array)-1)
quick_sort(array2, 0, len(array2)-1)
print(f"Insertion sort swap: {swap_insertion_sort}")
print(f"Quick sort swap: {swap_quick_sort}")
print(array)
print(array2)
