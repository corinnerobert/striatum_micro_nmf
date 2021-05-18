#sample script for loading in .mat component results (eg a voxels X comonents matrix) and
#writing/mapping values to nifti file for visualization
#main steps:
#1: load some label/image data into python, as you did for building input matrix. used as a coord space/ref for the output label
#2. load in .mat results from pnmf
#3. map W component scores (or a clustering) to output label - ie take the array loaded in from a nifti file, replace values with component scores/cluster labels, write file out 

#load libraries
import os
import glob
import pandas as pd
import numpy as np
import scipy
import scipy.io
import sys

#load TractREC 
sys.path.append('../lib/TractREC/TractREC/')
import TractREC as tr


#this function takes in component scores and writes out a nifti label file, using the coordinates extracted via tract rec
# voxscores - n_voxels X n_components matrix/array.  function will write out one label for each column
# base - a string specifying folder/path base for output file. modify if you like
# lb_ref - the majority voted label, used as a reference image for the output label. the fcn makes an image 'like' lb_ref, but replaces values with component scores/cluster lbels
# hemi - a string included in the output filename of the label. not essential, can remove/reformat if you like
#refimg_res - a res object from Tractrect. will contain voxel coordinate info in the vox_coord variable. required
def voxelscores_to_label(voxscores, base, lb_ref, hemi,refimg_res):
    voxcoords=refimg_res[0].vox_coord
    compnum  = np.shape(voxscores)[1]
    for c in range(0,compnum):
        outpath = base + hemi + 'stri-' + str(c) + '.nii.gz'
        print(outpath)
        b=np.transpose(voxscores[:,c])
        print( np.shape(b))
        d,a,h = tr.imgLoad(lb_ref,RETURN_HEADER=True)
        d_out = np.zeros_like(d).astype(np.float32)
        for idx, coord in list(enumerate(voxcoords[0])):
            d_out[coord[0]][coord[1]][coord[2]] = b[idx]

        tr.niiSave(outpath,d_out,a,header=h,CLOBBER=True)
        
#load in majority voted label and some t1t2 data, just as a reference
#the main point of this is to get the majority voted label and coordinates loaded in
#the chunk of code below (until the ###) will look similar to sample_get_t1t2_pca329_left.py

working_dir="C:/Users/coco_/Documents/Documents/Mcgill/NSCI410/projects/Striatal_NMF/warped/" #MODIFY - DONE

#you'll need a lookup table in .csv format with label number and structure. create one for your labels (left right striatum)
#look at the .csv file below as an example, then modify the line below to point to your .csv lookup
all_label_seg_file="../data/Labels_stri_lookup_table.csv" #MODIFY - DONE
all_label_seg=pd.read_csv(all_label_seg_file)
all_label_seg=all_label_seg.set_index(['Index']) #make the index column the actual index
all_lobule_subset_idx=[1] #MODIFY - this should be the label value of the structure of interest eg if this is extracting left striatum, make this the left striatum label val
all_label_seg.head()
all_lobule_subset_idx
df=pd.read_csv('../data/subjects_IDs_test.csv') #MODIFY to point to your copy of the demographics file
df_sorted=df

#Create two lists, each containing the filenames of the t1t2 filtered files and majority voted labels
t1divt2_files=[]
fused_label_files=[]
for row in df_sorted['Subject']:
    fname = working_dir  + str(row) + '/leftstri_correctedt1t2.nii.gz' #MODIFY - DONE

    t1divt2_files.append(glob.glob(fname)[0])
    fname = working_dir  + str(row) + '/final_majority_voted_Lstri_label.nii.gz' #MODIFY - DONE

    fused_label_files.append(glob.glob(fname)[0])
    
t1divt2_IDs=[os.path.dirname(name.split("/warped/")[1]) for name in t1divt2_files]

#use TractREC to extract the t1t2 data for each subject, only in voxels overlaying with the label



tr=reload(tr)
df_seg,res=tr.extract_quantitative_metric(t1divt2_files,fused_label_files,IDs=t1divt2_IDs,ROI_mask_files=None,label_df=all_label_seg,\
                                      label_subset_idx=all_lobule_subset_idx,thresh_mask_files=None,thresh_val=None,\
                                      max_val=None,thresh_type=None,erode_vox=None,metric='data',DEBUG_DIR=None,\
                                      VERBOSE=True,USE_LABEL_RES=False,volume_idx=0)

#the res variable is now a list of the results for each subject
###

#res also contains the coordinates of each voxel, key for mapping values back. 
#eg in the output W matrix, W[0,0] is voxel 1, component 1 value. where does this go in the original image?
#in res[0].vox_coord[0][0][0]
#code below is for loading in some opnmf results, then mapping component scores or cluster labels back to nifti

#load in some .mat results from opnmf
#the 7 lines below are for pointing to the nmf results .mat file, and making an output directory for the .nii files you will create. modify as necessary to point to your .mat opnmf results
compnum=5
hemi='left'
res_dir = '../output/opnmf_out/'
if not os.path.exists(res_dir):
    os.makedirs(res_dir)
fname='../data/' + \
hemi + 'stri_' + str(compnum) + 'components_matrix.mat'

#load in the results. in particular we want W here, which is voxels X components
w = scipy.io.loadmat(fname)['W']
h=scipy.io.loadmat(fname)['H']

lb_ref = "C:/Users/coco_/Documents/Documents/Mcgill/NSCI410/projects/Striatal_NMF/warped/final_majority_voted_Lstri_label.nii.gz" #modify, point to a majority vote striatum label

#the fcn call on the next line should create/write one nifti file for each component
voxelscores_to_label(w,res_dir,lb_ref,hemi,res) #modify res_dir, hemi variables for appropriate paths if necessary

#instead of one file per component, the code below uses a winner take all strategy to create cluster labels, and writes out the file
#eg for voxel 1, say component 2 score is highest -> voxel 1 is now in cluster 2. repeat for all voxels
#w_label_out ends up having dimensions n_voxels X 1 - as opposed to n_voxels X component
#values in w_label_out corrspond to cluster labels, output clustering is essentially combining each of the previously created component label files into one

w_label = np.zeros((np.shape(w)[0],1))
np.shape(w_label)
for v in range(0,np.shape(w_label)[0]):
    w_label[v,0] = np.argmax(w[v,:])
print( np.shape(w_label))
print( np.max(w_label))
w_label_out = w_label + 1

voxelscores_to_label(w_label_out,res_dir,lb_ref,hemi + '-cluster' + str(compnum),res) #modify res_dir, hemi variables for appropriate paths if necessary


