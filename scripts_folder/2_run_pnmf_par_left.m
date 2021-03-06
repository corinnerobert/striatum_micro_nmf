addpath('/data/chamal/projects/corinne/projects/Striatal_NMF/analysis/brainlets');
load(micro);

number_of_cores=6; %3 or 4, depending upon SPM or PLS
d=tempname(); %get a temporary location;
mkdir(d);
cluster = parallel.cluster.Local('JobStorageLocation',d,'NumWorkers',number_of_cores);
p=parpool(cluster,number_of_cores);
p.IdleTimeout= Inf;

[W,H,recon] = opnmf_mem_rai(left, k, [], 4,100000,[],[],100,[]);
save(outfile,'W','H','recon');
delete(gcp('nocreate'));
exit

