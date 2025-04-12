#!/usr/bin/env python3
import math as mt
import numpy as np
import matplotlib.pyplot as plt


Am ,Ac = 5, 2;
mu = Am/Ac
fm ,fc =10, 100;
omeg_m, omeg_c  = 2*(np.pi)*fm,  2*(np.pi)*fc


val_dict = {0:(0,0)}
def mes(t):
	x = omeg_m*(t/360)*0.0174
	sig = Am*mt.cos(x)
	return sig;

def carrier(t):
	x = omeg_c*(t/360)*0.0174
	car = Ac*mt.cos(x)
	return car;


def mod(t):

	mod = carrier(t) +mu*mes(t)*carrier(t)
	return mod

def demod(t):
	demod= mod(t) * carrier(t)
	return demod
	

time=[]
for t in range(15*10**3):
	time.append(t)
	val_dict.update({t:(mes(t),carrier(t),mod(t),demod(t))});
	

val_1 , val_2 = [v1 for t,(v1,v2,v3,v4) in val_dict.items()],[v2 for t,(v1,v2,v3,v4) in val_dict.items()]

val_3 , val_4 = [v3 for t,(v1,v2,v3,v4) in val_dict.items()],[v4 for t,(v1,v2,v3,v4) in val_dict.items()]



fig ,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2 );
fig.subplots_adjust(hspace = 0.5,wspace = 1);
fig.subplots_adjust(hspace = 0.5);
ax1.plot(time,val_1,"b-",label="Message");
ax1.set_xlabel("Time")
ax1.set_title("Message");
ax1.grid(True);

ax2.plot(time,val_2,"b-",label="Carrier");
ax2.set_xlabel("Time")
ax2.set_title("Carrier");
ax2.grid(True);


ax3.plot(time,val_3,"r-",label="Modulated");
ax3.set_xlabel("Time")
ax3.set_title("AM");
ax3.grid(True);


ax4.plot(time,val_4,"r-",label="DeModulated");
ax4.set_xlabel("Time")
ax4.set_title("Demod");
ax4.grid(True);


plt.tight_layout();
plt.show();
















