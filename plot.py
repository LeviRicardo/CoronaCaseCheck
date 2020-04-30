import matplotlib.pyplot as plt

def formatdata(data):
	data = ''.join(data)
	data = data.split('\t')
	return data

def filtrar(x,y,z):
	xf = []
	yf = []
	zf = []
	for i in range(len(x)-1):
		if x[i] != x[i+1]:
			xf.append(x[i])
			yf.append(y[i])
			zf.append(z[i])
	xf.append(x[-1])
	yf.append(y[-1])
	zf.append(z[-1])
	return xf, yf, zf

file = open('data.txt','r')

x = []
y = []
z = []

for i in file.readlines():
	values = formatdata(list(i)[:-1])
	x.append(values[0])
	try:
		values[1] = str(values[1]).replace(',','')
		y.append(int(values[1]))
	except:
		y.append(0)
	try:
		z.append(int(str(values[-1]).replace(',','')))
	except:
		z.append(0)




x, y, z= filtrar(x,y,z)
length = len(x)

base = int(5*10**(len(str(y[-1]))-2))

file.close()

plt.figure(figsize = (3*length/5,length/5))
plt.xlabel('Data')
plt.ylabel('Casos Confirmados No Brasil')
plt.grid()
plt.ylim(-1,y[-1]*1.05)
plt.plot(x[1:],y[1:],x[1:],z[1:])
plt.legend(('Casos Confirmados','Óbitos'),loc = 'upper left')
plt.yticks(range(0,round(y[-1]*1.05),base),range(0,round(y[-1]*1.05),base))
plt.annotate(f'    {y[-1]}',(x[-1],y[-1]))
plt.annotate(f'    {z[-1]}',(x[-1],z[-1]))
plt.scatter(x[-1], y[-1])
plt.scatter(x[-1],z[-1])
plt.savefig('casos.jpg', dpi = 200)
#plt.show()