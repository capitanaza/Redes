
from collections import defaultdict
from tabulate import tabulate

requests = defaultdict(lambda:0)
data = []
f = open('access.log', 'r')

for l in f:
	ip = l.split(' ')[0]
	if(ip != "::1"):
		requests[l.split(' ')[0]]+=1

f.seek(0,0)

for line in f:
	user = line.split(' ')[0]
	recurso = line.split('"')[1].split('HTTP')[0]
	code = line.split('"')[2].split(' ')[1]
	if(user != "::1"):
		data.append([user,recurso,code,str(requests[user])])


print tabulate(data, headers=['Usuario', 'Recurso', 'Codigo', '# Accesos'])