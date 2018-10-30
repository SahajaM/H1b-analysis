from __future__ import division
import csv
from collections import Counter
import sys


script = sys.argv[0]
# Opening the input file as csv_file
with open(sys.argv[1], mode='r') as csv_file:

	#initializations
	fl =[]
	states = []
	socname = []
	percentage_states = []
	percentage_names = []
	total_certified = 0
	
	# Reading csv_file and performing required operations 
	h1b = csv.DictReader(csv_file,delimiter=';')

	# Appending worksite states and SOC names in which case status is certified and also calculating total number of certified cases
	for row in h1b:
		if(row['CASE_STATUS']=='CERTIFIED'):
			states.append(row['WORKSITE_STATE'])
			socname.append(row['SOC_NAME'])
			total_certified += 1

	# Counting the occurances of each state and getting the top 10 states in required order
	counting_states = sorted(Counter(states).most_common(10), key=lambda (x,y):(-y,x))

	# Calculating percentage of state occurances compared to all certified cases
	for row in counting_states:
		percentage_states.append(float(round(((row[1]/total_certified)*100),1)))

	# Combining states and percentage into a single list
	list_states = [l +('{:.1f}%'.format(i),) for l,i in zip(counting_states,percentage_states)]

	# Counting the occurances of each occupation and getting the top 10 occupations in required order
	counting_names = sorted(Counter(socname).most_common(10), key=lambda (x,y):(-y,x))

	# Calculating percentage of occupation occurances compared to all certified cases
	for row in counting_names:
		percentage_names.append(float(round(((row[1]/total_certified)*100),1)))

	# Combining occupations and percentage into a single list
	list_names = [l +('{:.1f}%'.format(i),) for l,i in zip(counting_names,percentage_names)]

# Opening the output top 10 occupations file
with open(sys.argv[2],'wb') as out:
	
	# writing into file
	csv_out = csv.writer(out,delimiter=';')
	csv_out.writerow(['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
	for row in list_names:
		csv_out.writerow(row)		

# Opening the output top 10 states
with open(sys.argv[3],'wb') as out:

	# writing into file
	csv_out = csv.writer(out,delimiter=';')
	csv_out.writerow(['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
	for row in list_states:
		csv_out.writerow(row)

