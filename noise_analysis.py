# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:31:00 2017

@author: stella
"""

# ***Check if still duplicating last slide***

#-----------------------------------------------------------------------
# imports & definitions
#-----------------------------------------------------------------------

import numpy as np
import h5py
frames=[100,1000,10000]
exp_time=[0.001,0.01,0.1,1]
pix_rate=['slow','fast']

#-----------------------------------------------------------------------
# analysis loop
#-----------------------------------------------------------------------

for i in frames:
    for j in exp_time:
        for k in pix_rate:
            #-----------------------------------------------------------
            # dump for analysis of each file
            #-----------------------------------------------------------
            mean=[]
            std=[]
            mnm=[]
            mxm=[]
            chunks=i/100 # number of files for each acquisition
            num=["%06d" % a for a in range(1, chunks+1)]
            for l in num:
                fid=h5py.File('%d_frames_%d_%s_%d' %(i,j,k,l),'r')
                data=fid['/entry/data']
                mean.append(np.mean(data[0:99], axis=0)) # **!!ASSUMES DUPLICATED FINAL SLIDE!!**
                std.append(np.std(data[0:99], axis=0))       
                mnm.append(np.min(data[0:99], axis=0))
                mxm.append(np.max(data[0:99], axis=0))
            #-----------------------------------------------------------
            # dump for analysis over all the frames
            #-----------------------------------------------------------
            grand_mean=[]
            grand_std=[]
            grand_mnm=[]
            grand_mxm=[]
            
            #-----------------------------------------------------------
            # statistics for whole data set
            #-----------------------------------------------------------
            grand_mean.append(np.mean(mean)) 
            grand_mnm.append(np.min(mnm))
            grand_mxm.append(np.max(mxm))
            standy=0            
            for m in std: # calculation of ovoerall standard deviation
                standy+=m*m/chunks
            grand_std.append(np.sqrt(standy))
                
            #-----------------------------------------------------------
            # save final data
            #-----------------------------------------------------------
            np.save('mean_%dframes_%ds_%s.npy' %(i,j,k),grand_mean)
            np.save('std_%dframes_%ds_%s.npy' %(i,j,k),grand_std)
            np.save('min_%dframes_%ds_%s.npy' %(i,j,k),grand_mnm)
            np.save('max_%dframes_%ds_%s.npy' %(i,j,k),grand_mxm)
            
            