from tabulate import tabulate
import sys

if(len(sys.argv) != 3):
	print("Usage: python filter.py <FILE> <CODE_SERIES>")
	sys.exit(1)

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
	
	if(sys.argv[2] == str(1)):
		if(code >= str(100) and code < str(200)):
			data.append([date_time, ip_user, user, file, op, code])
	elif(sys.argv[2] == str(2)):
		if(code >= str(200) and code < str(300)):
			data.append([date_time, ip_user, user, file, op, code])
	elif(sys.argv[2] == str(3)):
		if(code >= str(300) and code < str(400)):
			data.append([date_time, ip_user, user, file, op, code])
	elif(sys.argv[2] == str(4)):
		if(code >= str(400) and code < str(500)):
			data.append([date_time, ip_user, user, file, op, code])
	elif(sys.argv[2] == str(5)):
		if(code >= str(500) and code < str(600)):
			data.append([date_time, ip_user, user, file, op, code])
	elif(sys.argv[2] == str(10000)):
		if(code > str(999)):
			data.append([date_time, ip_user, user, file, op, code])

print tabulate(data, headers=['Date - Time', 'IP User', 'User Name', 'File', 'Operation', 'Response Code'])