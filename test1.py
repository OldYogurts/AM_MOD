
import numpy as np;

x = ['1101','0101'];
lst = [];
for i in range(len(x)):
	byte_in_q = x[i];
	for j in range(0,len(byte_in_q)):
		lst.append(byte_in_q[j]);



print('list:',lst);
freq = 100
FS = 1000
t = len(lst) * 10 *100
omeg= 2*np.pi*freq


y= np.sin(omeg*t)
val = {};
idx = -1;
print('time',t);
time_list = []
for i in range(t):
	time_list.append(i);
	if(i%1000 == 0) : idx +=1;
	bin_dig = lst[idx];
	if(bin_dig == '0') : y = 0;
	else : y = np.sin(omeg*i/1000);
	val.update({i:y});

val_1 = [v1 for t , (v1) in val.items()];
import matplotlib.pyplot as plt
plt.plot(time_list,val_1);
plt.title("Plot of sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

