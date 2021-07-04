
def while_loop(i, inc):

	numbers = []

	while i < 100:
		print("At the top i is %d" % i)
		numbers.append(i)

		i = i + inc
		print("Numbers now: ", numbers)

		print("At the bottom i is %d" % i)

	print("The numbers: ")

	for num in numbers:
		print(num)


while_loop(69, 0.5)



def for_loop(start, inc):

	i = start

	for num in range(int(start), 100, int(inc)):
		print(num)

for_loop(20, 5)
