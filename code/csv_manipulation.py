import csv

"""
	CSV READING
"""
data = []
with open('people.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	# Loop through rows and add to your data list
	#    your code goes here

	csv_file.close()

"""
	DATA MANIPULATION
"""
# SORTING by SIN
# Go through the data and sort by SIN. Don't forget about the header!
#    your code goes here

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

# duplicating the data for manipulation
#    your code goes here

# remove the header, and store it
#    your code goes here

data_copy = sorted(data_copy,key=itemgetter(2,1)) # sort by LastName, FirstName

# put the header back
#    your code goes here

"""
	CSV WRITING
"""
with open('output.csv', mode="w") as out_file:
	csv_writer = csv.writer(out_file, delimiter=",")
	csv_writer.writerow(data_copy[0])	# write header row

	# Let's write, row-by-row, the LastName, FirstName, and DOB of the People in 
	# our list after sorting!
	for row in data_copy:
		entry = []						# temporary list for data to be written
		
		#    your code goes here

		csv_writer.writerow(entry)		# write row to CSV file

	out_file.close()
