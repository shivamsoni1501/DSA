
'''
def binarySearch(arr,a,b,val): 
	print(a,b)
	if(a>b):
		print("element is not present in the array.")
		return None
	c = (a+b)//2
	if(val==arr[c]):
		print('')
		print(val, 'is present at index', c)

		return None

	if(val > arr[c]):
		a=c+1
		binarySearch(arr,a,b,val)

	else:
		b=c-1
		binarySearch(arr,a,b,val)
'''

def find(arr, i, j, x):
	while i<=j:
		m = i + (j-i)//2
		if arr[m] == x: return m
		elif arr[m] < x: i = m+1
		else: j = m-1
	return -1

def find_first(arr, i, j, x):
	ans = -1
	while i<=j:
		m = i + (j-i)//2
		if arr[m] < x: i = m+1
		else:
			if arr[m] == x:
				ans = m
			j = m-1
	return ans
	
def find_last(arr, i, j, x):
	ans = -1
	while i<=j:
		m = i + (j-i)//2
		if arr[m] <= x:
			if arr[m] == x:
				ans = m
			i = m+1
		else:	j = m-1
	return ans
	
def lower_bound(arr, i, j, x):
	ans = -1
	while i<=j:
		m = i + (j-i)//2
		if arr[m] < x:
			i = m+1
		else:
			j = m-1
			ans = m
	return ans

def upper_bound(arr, i, j, x):
	ans = -1
	while i<=j:
		m = i + (j-i)//2
		if arr[m] <= x:
			ans = m
			i = m+1
		else:
			j = m-1
	return ans
	
arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 9, 14, 14, 44, 57, 75, 75]
print(find(arr, 0, len(arr)-1, 3))
print(find_first(arr, 0, len(arr)-1, 3))
print(find_last(arr, 0, len(arr)-1, 3))
print(lower_bound(arr, 0, len(arr)-1, 3))
print(upper_bound(arr, 0, len(arr)-1, 3))
print(lower_bound(arr, 0, len(arr)-1, 8))
print(upper_bound(arr, 0, len(arr)-1, 8))
















