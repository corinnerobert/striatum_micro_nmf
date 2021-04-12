#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os
import scipy.io
import scipy.stats
get_ipython().run_line_magic('pylab', 'inline')


#make output directory
if not os.path.exists('../output/input_matrices/'):
    os.makedirs('../output/input_matrices/')
#load unimodal matrices
leftt1t2 = scipy.io.loadmat('../data/leftstri_t1t2_input_matrix.mat')
leftfa = scipy.io.loadmat('../data/leftstri_fa_input_matrix.mat')
leftmd = scipy.io.loadmat('../data/leftstri_md_input_matrix.mat')
rightt1t2 = scipy.io.loadmat('../data/rightstri_t1t2_input_matrix.mat')
rightfa = scipy.io.loadmat('../data/rightstri_fa_input_matrix.mat')
rightmd = scipy.io.loadmat('../data/rightstri_md_input_matrix.mat')

#normalize residualize data
neg_leftt1t2 = scipy.stats.zscore(leftt1t2['left_t1t2'],axis=None)
neg_leftfa = scipy.stats.zscore(leftfa['left_fa'],axis=None)
neg_leftmd = scipy.stats.zscore(leftmd['left_md'],axis=None)

neg_rightt1t2 = scipy.stats.zscore(rightt1t2['right_t1t2'],axis=None)
neg_rightfa = scipy.stats.zscore(rightfa['right_fa'],axis=None)
neg_rightmd = scipy.stats.zscore(rightmd['right_md'],axis=None)

#concatenate matrices
left_all = np.concatenate((neg_leftt1t2,neg_leftfa,neg_leftmd),axis=1)
right_all = np.concatenate((neg_rightt1t2,neg_rightfa,neg_rightmd),axis=1)

#substract minimum to make all positive matrices
left_all = left_all - np.min(left_all)
right_all = right_all - np.min(right_all)

#save as .mat files 
scipy.io.savemat('../output/input_matrices/leftstri_multimodal_input_matrix.mat', mdict={'left':left_all})
scipy.io.savemat('../output/input_matrices/righttstri_multimodal_input_matrix.mat', mdict={'right':right_all})

#plot left multimodal input matrix
fig = plt.figure(figsize =(15,8), dpi=150 )

ax = fig.add_subplot(111)
ax.set_title('Left Input Matrix')
plt.imshow(left_all)
ax.set_aspect('auto')
ax.set_yticks([])
ax.set_xticks([164.5,493.5,822.5])
ax.set_xticklabels(('T1w/T2w', 'FA', 'MD'))
ax.set_ylabel('Voxels')
ax.set
plt.colorbar(orientation='vertical')
plt.clim(0,2*np.mean(left_all))
plt.savefig( '../output/input_matrices/leftstri_multimodal_input_matrix.png', bbox_inches='tight')
plt.show()


# plot right multimodal input matrix
fig = plt.figure(figsize =(15,8), dpi=150 )

ax = fig.add_subplot(111)
ax.set_title('Right Input Matrix')
plt.imshow(right_all)
ax.set_aspect('auto')
ax.set_yticks([])
ax.set_xticks([164.5,493.5,822.5])
ax.set_xticklabels(('T1w/T2w', 'FA', 'MD'))
ax.set_ylabel('Voxels')
ax.set
plt.colorbar(orientation='vertical')
plt.clim(0,2*np.mean(right_all))
plt.savefig( '../output/input_matrices/right_multimodal_input_matrix.png', bbox_inches='tight')
plt.show()

