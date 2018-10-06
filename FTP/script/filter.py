from tabulate import tabulate
import sys

f = open(sys.argv[1], 'r')

data = []

print

for line in f:
	ip_user = line.split(' ')[0]
	user = line.split(' ')[1]
	date_time = line.split(' ')[2][1:]
	op = line.split(' ')[4]
	file = line.split(' ')[5]
	code = line.split(' ')[6]
	
	if(user == sys.argv[2]):
		# Create Directories or Files
		if(sys.argv[3] == str(1)):
			if(op == 'MKD' or op == 'STOR'):
				data.append([ip_user, user, date_time, op, file, code])
		# Download files
		elif(sys.argv[3] == str(2)):
			if(op == 'RETR'):
				data.append([ip_user, user, date_time, op, file, code])
		# Delete Directories or Files
		elif(sys.argv[3] == str(3)):
			if(op == 'DELE' or op == 'RMD'):
				data.append([ip_user, user, date_time, op, file, code])
		# Rename Directories or Files
		elif(sys.argv[3] == str(4)):
			if(op == 'RNFR' or op == 'RNTO'):
				data.append([ip_user, user, date_time, op, file, code])

print tabulate(data, headers=['IP', 'User', 'Access', 'Operation', 'File', 'Response Code'])