def BinarySearch(num_list, key):
    lo = 0
    hi = len(num_list) - 1
    while (lo <= hi):
	mid = lo + (hi - lo)/2
	if (key < num_list[mid]):
	    hi = mid -1
	elif (key > num_list[mid]):
	    hi = mid + 1
	else:
	    return mid
    return -1

#test
print BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 8)
	
