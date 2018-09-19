from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

def addsplit(inlist):
	outlist =[]
	for n in inlist.split():
		# print(n)
		try: 
			outlist.append(float(n))
			print
		except ValueError:
			pass
	return outlist

ts = '0	0.1	0.2	0.3	0.4	0.5	0.6	0.7	0.8	0.9	1	1.1	1.2	1.3	1.4	1.5	1.6	1.7	1.8	1.9	2'
x0s = '1	1.1	1.2	1.3	1.4	1.5	1.6	1.7	1.8	1.9	2	2.1	2.2	2.3	2.4	2.5	2.6	2.7	2.8	2.9	3'
y0s = '3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3'
xss = '0	0.145677583	0.291355167	0.43703275	0.582710333	0.728387917	0.8740655	1.019743083	1.165420667	1.31109825	1.456775833	1.602453416	1.748131	1.893808583	2.039486166	2.18516375	2.330841333	2.476518916	2.6221965	2.767874083	2.913551666'
yss= '0	0.137032995	0.27406599	0.411098985	0.54813198	0.685164975	0.82219797	0.959230965	1.09626396	1.233296955	1.37032995	1.507362945	1.64439594	1.781428935	1.91846193	2.055494925	2.19252792	2.329560915	2.46659391	2.603626905	2.7406599'

xi = addsplit(x0s)
yi = addsplit(y0s)
t = addsplit(ts)
xs = addsplit(xss)
ys = addsplit(yss)


ax.plot3D(t,xi,yi)
ax.plot3D(t,xs,ys)
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y')
plt.show()