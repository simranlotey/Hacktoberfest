import math

def isArmstrong(num):
	n = num
	numDigits = 0
	sum = 0
	
	# Find number of digits in num
	while n > 0:
		n //= 10
		numDigits += 1
	
	n = num
	
	# Calculate sum of digits raised to the power of numDigits
	while n > 0:
		digit = n % 10
		sum += math.pow(digit, numDigits)
		n //= 10
	
	# Check if num is Armstrong number or not
	if sum == num:
		return True
	return False

# Example 1
num1 = 1634
if isArmstrong(num1):
	print(num1, "is an Armstrong number.")
else:
	print(num1, "is not an Armstrong number.")

# Example 2
num2 = 120
if isArmstrong(num2):
	print(num2, "is an Armstrong number.")
else:
	print(num2, "is not an Armstrong number.")
