def minOperations(self, n: int) -> int:
	num_of_operations = 0 
	while ( n > 0 ) :
		lowvalue = math.floor(math.log(n, 2))
		highvalue = math.ceil(math.log(n,2))
		num_of_operations = num_of_operations + 1
		lvalue = n-math.pow(2, lowvalue) 
		hvalue = math.pow(2, highvalue)  - n 
		n = lvalue if lvalue < hvalue else hvalue
	return num_of_operations