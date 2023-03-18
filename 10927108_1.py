import time

# 程式開始


# 最大子陣列問題
# do
"""
給定一個陣列
可有正有負
找出一個子陣列
其包含有最大的總和
"""
# input
"""
array_size 正整數開頭
array_value 
重複直到遇到array_size = 0 
"""
# output
"""
最大子陣列的起始即結束index
以及總和
直到input結束

ex. 
Low = 4, High = 7, Sum = 6
...

"""

def Find_Maximum_Subarray( A ):
	n = len( A )
	low, high, sum = _Find_Maximum_Subarray( A, 0, n - 1 )
	
	print( "Maximum-Subarray Problem:" )
	print( "Low =", int(low)+1, "High =", int(high)+1, "Sum =", sum )


def _Find_Maximum_Subarray( A, low, high ):
	if high == low:
		return low, high, A[low]
	else:
		mid = ( low + high ) // 2 
		
		left_low, left_high, left_sum    = _Find_Maximum_Subarray( A, low, mid )
		right_low, right_high, right_sum = _Find_Maximum_Subarray( A, mid + 1, high )		
		cross_low, cross_high, cross_sum = _Find_Max_Crossing_Subarray( A, low, mid, high )
		
		if ( left_sum > right_sum and left_sum >= cross_sum ):
			return left_low, left_high, left_sum
		elif ( right_sum >= left_sum and right_sum >= cross_sum ):
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum


def _Find_Max_Crossing_Subarray( A, low, mid, high ):
	left_sum = -3000000
	sum = 0
	for i in range( mid, low - 1, -1 ):
		sum += int(A[i])
		if sum > left_sum:
			left_sum = sum		
			max_left = i
		
	right_sum = -3000000
	sum = 0
	for j in range( mid + 1, high + 1 ):
		sum += int(A[j])
		if sum > right_sum:
			right_sum = sum	
			max_right = j
	
	cross_low  = max_left
	cross_high = max_right
	cross_sum  = left_sum + right_sum
	
	return cross_low, cross_high, cross_sum




start_time = time.time()

print("Maximum Subarray Problem")
# 陣列大小
array_size = input() 
# 陣列內容
array_value = []

while int(array_size) != 0  :
    single_value = input()
    array_value = single_value.split(" ")

    for x in range(len(array_value) ):
        array_value[x] = int(array_value[x])

    Find_Maximum_Subarray(array_value)
    array_size = input()



total_time = time.time() - start_time
print("Cost times= " + str(total_time))
