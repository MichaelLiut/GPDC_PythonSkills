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


# Let's say we just want to plot the number of occurances of a certain job. 

# store occupation data
occupations = {}
for row in data:
	# occupation is the 4th CSV entry	
	#    your code goes here

	if occ in occupations.keys():
		# add to occupation count
		#    your code goes here
	else:
		# initializes the first instance
		# of that particular occupation
		#    your code goes here


# perhaps remove those with too little occurances? how would you do this?
#    your code goes here

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