import csv
import matplotlib.pyplot as plt 
import numpy as np
from operator import itemgetter, attrgetter

"""
	CSV READING
"""
data = []
with open('people.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		data.append(row)
	csv_file.close()


# store occupation data
occupations = {}
for row in data:
	occ = row[4]					# occupation is the 4th CSV entry	
	if occ in occupations.keys():
		occupations[occ] += 1		# add to occupation count
	else:
		occupations[occ] = 1		# initializes the first instance
									# of that particular occupation


# perhaps remove those with too little occurances?
to_be_removed = []					# list of removable occurances
for i in occupations:
	if occupations[i] < 5:			# if the occurances are less than 3,
		to_be_removed.append(i)		# add to removal list

for j in to_be_removed:			
	occupations.pop(j) 			# remove that occurance

# Let's do a bar plot of the number of people of a certain occupation.
occ_names = []
occ_count = []

for i in occupations:
	occ_names.append(i)
	occ_count.append(occupations[i])

occ_names = tuple(occ_names)

y_pos = np.arange(len(occ_names))
fig = plt.bar(y_pos, occ_count, align='center', alpha=0.5)
plt.xticks(y_pos, occ_names)
plt.ylabel('Occupation Count')
plt.title('Occupation Analysis')
plt.show()