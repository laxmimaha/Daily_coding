
def binary_search (arr,  index):
    left = 0 
    right = len(arr)-1
    if left > right :
	    return -1
	
    mid = (left + right) // 2
    if arr[mid] == index :
	    return mid

    if arr[left] <= arr[mid] :
	    if index >= arr[left] and index <= arr[mid] :
		    return binary_search(arr, left, mid-1, index)
	    return binary_search(arr, mid + 1, right, index)


    if index >= arr[mid] and index <= arr[right] :
	    return binary_search(arr, mid + 1, right, index)
    return binary_search(arr, left, mid-1, index)


arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 8
i = binary_search(arr, key)
if i == -1:
	print ("key not found")
else:
	print (i)

