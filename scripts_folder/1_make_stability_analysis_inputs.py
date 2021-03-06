#Corinne Robert - Make inputs for the stability analysis
#From the original input matrix, this codes create 10 different splits of the data
#For each split, we have to groups one of 165 participants and one of 164 participants (with the same mean age)


import numpy as np
import scipy.io
import scipy.stats
from sklearn.model_selection import StratifiedShuffleSplit

#import the .mat
working_dir="C:\\Users\\coco_\\Documents\\Documents\\Mcgill\\NSCI410\\projects\\Striatal_NMF\\analysis\\"
rawleft_t1t2 = scipy.io.loadmat(working_dir+'nmf_input_matrix/left1t2.mat')
left_fa=scipy.io.loadmat(working_dir+'nmf_input_matrix/leftstri_fa_329.mat')
left_md=scipy.io.loadmat(working_dir+'nmf_input_matrix/leftstri_md_329.mat')

#Transform data from .mat files to numpy array
rawleft_t1t2 = np.array(rawleft_t1t2['left_t1t2'])
left_fa = np.array(left_fa['left_fa'])
left_md = np.array(left_md['left_md'])

#create the matrices for the split
X = np.arange(329)
y1 = np.repeat(0,164)
y2 = np.repeat(1,165)
y=np.concatenate((y1,y2))
#get the subjects indices of the 10 splits
sss = StratifiedShuffleSplit(n_splits=10, test_size=164, random_state=0)

idx=1
#Construct the 20 new split matrices
for train_index, test_index in sss.split(X, y):
	fnameA=working_dir+"stability_inputs\\group"+str(idx)+"indicesA.mat"
	fnameB=working_dir+"stability_inputs\\group"+str(idx)+"indicesB.mat"
	
	t1t2A = rawleft_t1t2[:,train_index]
	t1t2A=scipy.stats.zscore(t1t2A,axis=None)
	t1t2B = rawleft_t1t2[:,test_index]
	t1t2B=scipy.stats.zscore(t1t2A,axis=None)
	
	faA = left_fa[:,train_index]
	faA=scipy.stats.zscore(faA,axis=None)
	faB = left_fa[:,test_index]
	faB=scipy.stats.zscore(faB,axis=None)
	
	mdA = left_md[:,train_index]
	mdA=scipy.stats.zscore(mdA,axis=None)
	mdB = left_md[:, test_index]
	mdB=scipy.stats.zscore(mdB,axis=None)
	
	A = np.concatenate((t1t2A,faA,mdA),axis=1)
	B = np.concatenate((t1t2B,faB,mdB),axis=1)
	A= A-np.min(A)
	B=B-np.min(B)
	
	scipy.io.savemat(fnameA, mdict={'left': A})
	print("Saved: "+fnameA)
	scipy.io.savemat(fnameB, mdict={'left': B})
	print("Saved: "+fnameB)
	idx+=1
		
	
