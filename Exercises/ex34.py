animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

for i in range(len(animals)):
	print("The animal at index %r is the %r" % (i, animals[i]))

for i in range(len(animals)):
	print("The %r st animal is the %r" % (i+1, animals[i]))