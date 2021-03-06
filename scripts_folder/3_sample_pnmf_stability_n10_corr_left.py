import os
import glob
import pandas as pd
import numpy as np
import seaborn as sns
import scipy
import scipy.io
import pickle


import sys
sys.path.append('/data/chamal/projects/corinne/projects/Striatal_NMF/preprocessed/TractREC/') #MODIFY 
import TractREC as tr
import sklearn
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing

from sklearn.decomposition import NMF
import random
from sklearn.model_selection import StratifiedShuffleSplit
import datetime


df_sorted = pd.read_csv('/data/chamal/projects/corinne/projects/Striatal_NMF/raw_data/df_sorted_unrestricted_329.csv') #MODIFY 

#Defining some variables - should be same for you
n_subjects = 329
n_splits = 10
max_gran = 10

#output directory where the stability results go
out_dir = "/data/chamal/projects/corinne/projects/Striatal_NMF/analysis/stability/stability_out/leftn" + str(n_splits) + "/" #MODIFY 
if not os.path.exists(out_dir):
       os.mkdir(out_dir)

#columns of the output spreadsheet, keep as is
cols = ["Granularity","Iteration","Euclidean_mean","Euclidean_median","Euclidean_std","Cosine_mean","Cosine_median","Cosine_std","Corr_mean","Corr_median","Corr_std","Recon_errorA","Recon_errorB"]
df = pd.DataFrame(columns = cols) #initiate dataframe

#location of the opnmf results (.mat files) for each split
stab_dir = "/data/chamal/projects/corinne/projects/Striatal_NMF/analysis/stability/pnmf_out/left" #MODIFY 
#LEFT HC STABILITY
#this loop computes spatial stability for each split, for each granularity
#results are stored in a .csv file that is written to your out_dir variable
for i in range(1,n_splits):
    
    for g in range(2,max_gran+1):
        #load split input, run nmf for each split
        fname = stab_dir + "/" + str(g) + "/group" + str(i) + "indicesA_result.mat" #MODIFY 
        print fname
        resA = scipy.io.loadmat(fname)
        Wa = resA['W'] #voxels X components matrix - componet scores
        ea = resA['recon'][0,0] #reconstruction error 
        
        #repeat for split B
        fname = stab_dir + "/" + str(g) + "/group" + str(i) + "indicesB_result.mat"  #MODIFY
        print fname
        resB = scipy.io.loadmat(fname)
        Wb = resB['W']
        eb = resB['recon'][0,0]
         
        #assess correlation of identified parcel component scores - which parcels vary together?
        c_Wa = cosine_similarity(Wa)
        c_Wb = cosine_similarity(Wb)
        
        #define some arrays to store similarity metrics across all voxels
        #these arrays are dimensions 1 X n_voxels - so the corr stores the correlation of each voxels btwn splits
        #cosine similarity and euclid distance were also tested but not used, can leave them in though 
        cosine_dist = np.zeros((1,np.shape(c_Wa)[0]))
        euclid_dist = np.zeros((1,np.shape(c_Wa)[0]))
        corr = np.zeros((1,np.shape(c_Wa)[0]))

        #cycle through each voxel and compare that voxels data in c_Wa and c_Wb
        #this is asking - what is the {correlation,cosinesim,eucliddistance} between the similarity btwn voxel i and all other voxels
        #in split A and the similarity btwn voxel i and all other voxels in split B
        for parcel in range(0,np.shape(c_Wa)[0]):
            cosine_dist[0,parcel] = scipy.spatial.distance.cosine(c_Wa[parcel,:], c_Wb[parcel,:])
            euclid_dist[0,parcel] = scipy.spatial.distance.euclidean(c_Wa[parcel,:], c_Wb[parcel,:])
            corr[0,parcel] = np.corrcoef(c_Wa[parcel,:],c_Wb[parcel,:])[0,1]

        #for this split/granularity, make a small .csv (1 row) containing mean, median, std of the various metrics, along with the granularity and split
        df_curr = pd.DataFrame(data = [[g, i+1, np.mean(euclid_dist), np.median(euclid_dist),np.std(euclid_dist),
                                        np.mean(cosine_dist), np.median(cosine_dist),np.std(cosine_dist),np.mean(corr),np.median(corr),np.std(corr),ea,eb]], columns = cols)
        df = df.append(df_curr) #append the 1 row df to the full df -> this becomes 1 row longer each loop iteration
        df.to_csv(out_dir + 'temppnmf_cosine-sim_lefthc_corr.csv') #each loop iteration, write out a temp output file. not really necessary, remove if you like
        del Wa,Wb,ea,eb,resA,resB
    

#write out the full df containing the similarity metrics for each granularity, for each split
#should be (n_granularities * n_splits) + 1 rows
df.to_csv(out_dir + 'pnmf_cosine-sim_leftstri_corr.csv') #MODIFY
del df, df_curr
