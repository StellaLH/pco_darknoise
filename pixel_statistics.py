# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:14:45 2017

@author: stella
"""
import numpy as np

statistic=['mean', 'std', 'min','max']
mean='mean'
std='std'
min='min'
max='max'

exposure_time=['0.001', '0.01','0.1', '1']

frames=[100,1000,10000]

pixel_rate=['slow', 'fast']
slow='slow'
fast='fast'

print "Arguments of the background_noise() function:\n"
print "> stat: mean/std/min/max \n"
print "> no_frames: 100/1000/1000 \n" 
print "> exp_time: 0.001/0.01/0.1/1 \n" 
print "> pix_rate: slow/fast \n"


def background_noise(stat,no_frames, exp_time,pix_rate):
	for stat=='mean':
		for pix_rate=='slow':
			data=np.load("mean_%sframes_%ss_slow.npy" %(no_frames, %exp_time))
#    a=statistic.index(str(stat))
#    b=frames.index(str(no_frames))
#    c=exposure_time.index(str(exp_time))
#    d=pixel_rate.index(str(pix_rate))
    data=np.load("%s_%sframes_%s_%s.npy" %(stat, no_frames, exp_time, pix_rate))

    print "%s_%sframes_%s_%s.npy"  %stat, no_frames, exp_time, pix_rate
    