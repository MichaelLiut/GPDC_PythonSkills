import csv

"""
	CSV READING
"""
data = []
with open('people.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		data.append(row)
	csv_file.close()

"""
	DATA MANIPULATION
"""
# SORTING by SIN
sorted_data = data[1:]				# create a new list, without header
sorted_data.sort()					# sort the data based on first column
sorted_data.insert(0,data[0])		# add column header

# SORTING by Last Name, then First Name
# 	this is a bit trickier! 
from operator import itemgetter, attrgetter
"""
	'itemgetter' will allow you to sort by the position in the list the column 
	heading is. For example: 	sorted(data, key=itemgetter(2))
								where 2 is the third column. In computer science 
								our list counting starts at 0 not 1!
	'attrgetter' will allow you to sort by the column name. 
				For example: 	sorted(data, key=attrgetter('LastName'))
"""

data_copy = data.copy()				# duplicating the data for manipulation
header = data_copy.pop(0)			# remove the header, and store it
data_copy = sorted(data_copy,key=itemgetter(2,1)) # sort by LastName, FirstName
data_copy.insert(0,header)			# put the header back!

"""
	CSV WRITING
"""
with open('output.csv', mode="w") as out_file:
	csv_writer = csv.writer(out_file, delimiter=",")
	#csv_writer.writerow(data_copy[0])	# write header row

	for row in data_copy:
		entry = []				# temporary list for data to be written
		entry.append(row[2])			# add LastName
		entry.append(row[1])			# add FirstName
		entry.append(row[9])			# add DateOfBirth
		entry.append(row[4])			# add DateOfBirth 
		csv_writer.writerow(entry)		# write row to CSV file

	out_file.close()
