#!/usr/bin/env python3
import math as mt
import numpy as np
import matplotlib.pyplot as plt

import tkinter
from tkinter import messagebox
from tkinter import ttk


class AMP_MOD():

	def __init__(self,t):

	def mes(self):
		Fs = 1000
		omeg_m  = 2*(np.pi)*self.AM_freq
		x = omeg_m*(self.time/Fs);
		sig = self.AM_amp*mt.cos(x)
		return sig;


	def carrier(self):
		Fs = 1000
		omeg_c=2*(np.pi)*self.AC_freq
		x = omeg_c*(self.time/Fs);	
		car = self.AC_amp*mt.cos(x)
		return car;


	def mod(self):
		mu = self.AM_amp/self.AC_amp
		mod = self.carrier() + mu * self.mes() *self.carrier()
		return mod

	def demod(self):
		demod= self.mod() * self.carrier()
		self.mesag();
		return demod
		
	def mesag(self):
		Char_to_BIN= (lambda lst : [ bin(ord(a)).replace('0b','') for a in lst ])
		x = Char_to_BIN(list(self.message));
			
		return x;



	def Run_mod():
		
		time=[]
		val_dict={0:(0,0)}
		die(TIME_ENTRY.get(),"Runtime given is not a number")
		for t in range((len(AM_MOD().mesag())*8*10)*1000):
			time.append(t)
			
			val_dict.update({t:(AMP_MOD(t).mes(),AMP_MOD(t).carrier(),AMP_MOD(t).mod(),AMP_MOD(t).demod())});
			

		val_1 , val_2 = [v1 for t,(v1,v2,v3,v4) in val_dict.items()],[v2 for t,(v1,v2,v3,v4) in val_dict.items()]

		val_3 , val_4 = [v3 for t,(v1,v2,v3,v4) in val_dict.items()],[v4 for t,(v1,v2,v3,v4) in val_dict.items()]

		

		fig ,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2 );
		fig.subplots_adjust(hspace = 0.5,wspace = 1);
		fig.subplots_adjust(hspace = 0.5);
		ax1.plot(time,val_1,"b-",label="Message");
		ax1.set_xlabel("Time(ms)")
		ax1.set_title("Message(V)");
		ax1.grid(True);

		ax2.plot(time,val_2,"b-",label="Carrier");
		ax2.set_xlabel("Time(ms)")
		ax2.set_title("Carrier(V)");
		ax2.grid(True);


		ax3.plot(time,val_3,"r-",label="Modulated");
		ax3.set_xlabel("Time(ms)")
		ax3.set_title("AM(V)");
		ax3.grid(True);


		ax4.plot(time,val_4,"r-",label="DeModulated");
		ax4.set_xlabel("Time(ms)")
		ax4.set_title("Demod(V)");
		ax4.grid(True);


		plt.tight_layout();
		plt.show();



def die(x,message):
	if not (x.isdigit()):
		tkinter.messagebox.showwarning(title="Error",message = message);
		raise ValueError(message);
	 	
	return 0



if __name__ == "__main__":
	window = tkinter.Tk();
	window.title("AMPLITUDE MODULATION VARIABLES");

	frame = tkinter.Frame(window);
	frame.pack();


	AM_MESSAGE_BOX =tkinter.LabelFrame(frame,text = "AMPLITUDE MODULATION");
	AM_MESSAGE_BOX.grid(row=0,column=0,padx=200,pady=100);

	# LABELS

	#box1=AM_MESSAGE_BOX.winfo_atom(AM_AMP_LABEL)


	AM_AMP_LABEL = tkinter.Label(AM_MESSAGE_BOX,text = "INSERT MESSAGE AMPLITUDE (V)").grid(row=0);
	AM_AMP_ENTRY= tkinter.Entry(AM_MESSAGE_BOX)
	AM_AMP_ENTRY.grid(row=1,column=0)



	AM_FREQ_LABEL =tkinter.Label(AM_MESSAGE_BOX,text = "INSERT MESSAGE FREQUENCY (Hz)").grid(row=2);
	AM_FREQ_ENTRY= tkinter.Entry(AM_MESSAGE_BOX)
	AM_FREQ_ENTRY.grid(row=3,column=0);


	CARRIER_AMP_LABEL = tkinter.Label(AM_MESSAGE_BOX,text = "INSERT CARRIER AMPLITUDE (V)").grid(row=4);
	CARRIER_AMP_ENTRY= tkinter.Entry(AM_MESSAGE_BOX)
	CARRIER_AMP_ENTRY.grid(row=5,column=0);


	CARRIER_FREQ_LABEL = tkinter.Label(AM_MESSAGE_BOX,text= "INSERT CARRIER FREQUENCY (Hz)").grid(row=6);
	CARRIER_FREQ_ENTRY= tkinter.Entry(AM_MESSAGE_BOX)
	CARRIER_FREQ_ENTRY.grid(row=7,column=0);

	TIME_LABEL = tkinter.Label(AM_MESSAGE_BOX,text ="TIME TO RUN (sec)").grid(row=8);
	TIME_ENTRY = tkinter.Entry(AM_MESSAGE_BOX)
	TIME_ENTRY.grid(row=9,column=0)

	MESSAGE_LABEL = tkinter.Label(AM_MESSAGE_BOX,text ="MESSAGE:").grid(row=10);
	MESSAGE_ENTRY = tkinter.Entry(AM_MESSAGE_BOX)
	MESSAGE_ENTRY.grid(row=11,column=0)
	button = tkinter.Button(AM_MESSAGE_BOX,text="MODULATE AWAY",command=AMP_MOD.Run_mod);
	button.grid(row =12,column =0,padx=70,pady=80)
	window.mainloop();

