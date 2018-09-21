
from collections import defaultdict
from tabulate import tabulate

requests = defaultdict(lambda:0)
data = []
f = open('cu.log', 'r')

for l in f:
	ip = l.split(' ')[0]
	if(ip != "::1"):
		requests[l.split(' ')[0]]+=1

f.seek(0,0)

for line in f:
	user = line.split(' ')[0].split(':')[0]
	traficoIn = line.split(' ')[9] + ' bytes'
	traficoOut = line.split(' ')[10] + ' bytes'
	tiempoRespuesta = line.split(' ')[11] + ' ms'
	if(user != "::1"):
		data.append([user,traficoIn,traficoOut,tiempoRespuesta])


print tabulate(data, headers=['Usuario', 'Trafico In', 'Trafico Out', 'Tiempo Respuesta '])