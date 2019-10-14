import csv

with open('multiplication2.csv', 'w') as csvfile:
	fieldnames = ['in', 'out']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()

	for i in range(1000):
		writer.writerow({'in': i, 'out': i*2})

	#for every position on a 10x10 grid: one datapoint
	#for x in range(10):
	#	for y in range(10):
	#		writer.writerow({'x_current': x, 'y_current': y, 'x_next': 3, 'y_next': 4})