# Datasharing plan for Micro NMF project
Goal: 
Share data that is useful for readers of the paper and for the wider research community. I think a good way to achieve both is to have two data releases:

## General data release
The warped maps that are the input to all analyses. This release will contain:

- individual maps warped to group average
- the group average
- the individual transformation matrices (individual to group average)
- some basic documentation on how the data were derived from the HCP release
    - inclusion criteria
    - processing steps (not the code itself, more like method section)
    - meta-data (as required by Zenodo)
- a license (appropriate for HCP derived data, need to check)

This will be the structure of the release:

1. warped maps/
    - subject 1/
        - warped map file
        - transformation to group avg file
    - subject 2/
        - …
2. group average map file
3. striatum labels file
4. README.md
5. LICENSE

## The paper data supplement
The intermediate results / data outputs required to run the code released with the paper

- consistent file naming that also matches what released code outputs (as declarative as possible, so people get what’s going on)
- general documentation on dataset (belongs to paper, look here for the code)
- meta-data (as req by Zenodo)
- a license

This will be the structure of the release:

1. A flat folder containing the intermediate files
    1. D1 multimodal input matrix (voxel by modality matrix). filename: {leftstri or rightstri}_multimodal_input_matrix.mat
    2. D2 T1w/T2w only input matrix (voxel by T1w/T2w). filename: {leftstri or rightstri}_t1t2_input_matrix.mat
    3. D3 FA only input matrix (voxel by FA). filename: {leftstri or rightstri}_fa_input_matrix.mat
    4. D4 MD only input matrix (voxel by MD). filename: {leftstri or rightstri}_md_input_matrix.mat
    5. Stability analysis inputs (opnmf results on the 10 splits for granularities 2 to 10). directory/filename organization: stability_analysis_inputs/{leftstri or rightstri}/{granularity}/group{split number}indices\_{A or B}\_results.mat 
    5. D2 Multimodal stability analysis results (.csv file with granularity-group pair as rows and mean/correlation/accuracy measures as columns). filename: {leftstri or rightstri}\_multimodal\_stability\_measures.csv
    6. D3 T1w/T2w stability analysis results (.csv file with granularity-group pair as rows and mean/correlation/accuracy measures as columns). filename: {leftstri or rightstri}_t1t2_stability_measures.csv
    7. D4 FA stability analysis results (.csv file with granularity-group pair as rows and mean/correlation/accuracy measures as columns). filename: {leftstri or rightstri}_fa_stability_measures.csv
    8. D5 MD stability analysis results (.csv file with granularity-group pair as rows and mean/correlation/accuracy measures as columns). filename: {leftstri or rightstri}_md_stability_measures.csv
    9. D6 a .mat file with the labels. filename: {leftstri or rightstri}_5components_matrix.mat
    10. D7 a .mnc file with the volumetric representation of labels. filename: {leftstri or rightstri}_5clusters.nii.gz
    11. D8 .mat files with latent variables obtained with PLS. directory/filename: latent_variables/{left or right}\_lv\_{one or two}.mat
2. README.md
3. LICENSE file
