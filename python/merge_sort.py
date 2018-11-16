

def merge_sort(arr):

	if len(arr) <= 1:
		return arr

	left_array = arr[0:int(len(arr) / 2)]
	right_array = arr[int(len(arr) / 2):]

	return merge(merge_sort(left_array), merge_sort(right_array))


def merge(l,r):
	left = l
	right = r 
	temp_array = []

	while len(left) != 0 and len(right) != 0:
		if left[0] < right[0]:
			temp_array.append(left[0])
			del left[0]
		elif right[0] < left[0]:
			temp_array.append(right[0])
			del right[0]
		else:
			temp_array.append(right[0])
			temp_array.append(left[0])
			del right[0]
			del left[0]

	return temp_array + left + right


a = [1,6,2,4,8,9,7,3,5,0]
res = merge_sort(a)
print(res)
