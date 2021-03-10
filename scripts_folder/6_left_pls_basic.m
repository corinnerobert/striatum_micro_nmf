%copy the hc-nmf-micro/analysis/Pls folder to your projects folder, modify the addpath cmd as necessary
addpath /data/chamal/projects/corinne/projects/Striatal_NMF/analysis/PLS/Pls/plscmd

%load in spreadsheets containing your brain data - nmf weights, and behaviour data
%the 1,2 in the csvread cmd is saying read in the csv but start at row 2, column 3 (0based indexing so 1,2 -> 2nd row 3rd col)
%this is because the first row contains headers (eg Subject ID, COMP1_T1T2, Age) and first 2 columns are an index col and subject ids in my spreadsheets
%so the data loaded in should be just the component weights or behav measures, not headers or subject ids
%modify lines below
left_mri_raw = csvread('/data/chamal/projects/corinne/projects/Striatal_NMF/analysis/PLS/pls_inputs/left_brain_spreadsheet.csv',1,2);
behavs_raw = csvread('/data/chamal/projects/corinne/projects/Striatal_NMF/analysis/PLS/pls_inputs/behaviour_spreadsheet_basic.csv',1,2);

%a list of all behaviours used - should match the order of columns in your behav .csv file, modify - DONE
  behavs = {'Age_in_Yrs','SSAGA_Educ','Gender_F','Flanker_Unadj','DDisc_AUC_200','DDisc_AUC_40K','Endurance_Unadj','GaitSpeed_Comp','Dexterity_Unadj','Strength_Unadj'};

%list of component weights, should match order ofcolumns used in your brain .csv file, modify -DONE
components = {'Comp1_T1T2', 'Comp1_FA', 'Comp1_MD', 'Comp2_T1T2',...
    'Comp2_FA', 'Comp2_MD', 'Comp3_T1T2', 'Comp3_FA', 'Comp3_MD',...
	      'Comp4_T1T2', 'Comp4_FA', 'Comp4_MD','Comp5_T1T2', 'Comp5_FA', 'Comp5_MD'};

%zscore manually
mu = mean(left_mri_raw);
sigma = std(left_mri_raw);

z = bsxfun(@minus,left_mri_raw,mu);
datamat{1} = bsxfun(@rdivide,z,sigma);

mu = mean(behavs_raw);
sigma = std(behavs_raw);

z = bsxfun(@minus,behavs_raw,mu);
option.stacked_behavdata = bsxfun(@rdivide,z,sigma);

%set option 3 for brain-behav pls, other variants exist (Eg pls for task fmri) but we want brain-behav. leave as is
option.method = 3;  % 1 = mean-centering (i.e. group/condition comaprison)
                    % 3 = behaviour (comparing 2 sets of variables)

%set permuation and bootstrap numbers - ie how many permuations will you do
%leave as is. 1000 is probably good enough here, but i did 10k because it didnt take too long to run
option.num_perm = 10000;
option.num_boot = 10000;

%run pls
left_result = pls_analysis(datamat,329,1,option);

% check pvalues - prints the pvals of each lv to screen
left_result.perm_result.sprob

% percent covariance - extract the percent cov explained by each lv
left_pct_cov = (left_result.s .^2) / sum(left_result.s .^2);

%save the output to a .mat file. modify the filename to whatevery you want
save('pls_basic/left_5comps_behavs_edu-noWM_pls_basic.mat');

