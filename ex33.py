def testWhile(number, increment):
	i = 0
	numbers = []
	
	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers

number = 6
increment = 1
numbers = testWhile(number, increment)
	
print "The numbers: "

for num in numbers:
	print num