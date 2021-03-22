# HCP data sharing checklist
Author: (Corinne Roberts)[mailto:corinne.robert@mail.mcgill.ca]

## Summary
### Open-access data use terms

To use and redistribute HCP data or derivatives HCP data you must share it under the same [open-access data use terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms) provided by the HCP. You must not try to contact or identify human subjects and you must comply with your institution guidelines as the HCP data is not de-identified.
### Restricted data use terms 

Additionnally with the open-access data use terms, to share HCP data derivatives that uses restricted data you must comply with the [restricted data use terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-restricted-data-use-terms) provided by the HCP. Briefly, **except for family structure**, you cannot publicly share any subject-specific information that is part of the restricted data (see [section A2](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-restricted-data-use-terms)). **IF** you want to share subject-specific family structure information or derivatives that used restricted data, you must not share HCP subject's specific IDs. Instead, you need to make study-specifc ones of your choosing (like A,B,C...) that you can link to the HCP IDs using the a [Subject key](https://www.humanconnectome.org/study/hcp-young-adult/document/creating-and-using-subject-keys-connectomedb). **Your Subject key will be made available to the HCP restricted data user only, you cannot share this key publicly**.

Here are some example of what is ok and not ok to share: you can publicly share the mean age of your overall sample BUT you cannot share the exact age of subject A; you can share the family structure of subject A BUT you cannot share any other restricted info about subject A; you cannot share the family structure of subject (HCP specific ID)
### Acknowledgement and License

As you must know, any data used in your research that was not acquired by yourself or your coauthors needs to be acknowledge properly in the acknowledgment section, otherwise it constitutes a form of plagiarism. Hence, if you are using HCP data, in your acknowledgment section you need to write the following : "Data were provided [in part] by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University.". 

The HCP does not provided any clear licensing information, however, the shared HCP derivatives must be shared under the same same [Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms) 

## Checklist
There are two cases:
### If your derivatives only used open-access HCP data
- [ ] Share under the same [Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms)

### If your derivatives used restricted HCP data
1. For subject specific data/derivatives (**[open-access data](https://www.humanconnectome.org/study/hcp-young-adult/document/quick-reference-open-access-vs-restricted-data) or family-structure only**): 
    - [ ] Make study specific IDs
    - [ ] Link your study-specific IDs to the HCP IDs with a [Subject key](https://www.humanconnectome.org/study/hcp-young-adult/document/creating-and-using-subject-keys-connectomedb)
    - [ ] Share subject specific data with study-specific IDs 

1. For multiple-subject derivatives:
    1. If data analyzed with [Additional Restricted Data elements](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-restricted-data-use-terms)
        - [ ] Check if derivatives contain at least 3 subjects
        - [ ] Remove study-specific IDs link to individual data points (subjects)
        - [ ] Share derivatives
    2. If data anlyzed only contain open-access data (e.g images ...):
        - [ ] Share derivates, you may link individual datapoints to study-specific IDs ??
   1. ### Other
       - [ ] Check data sharing and licensing guidelines of the journal you want to submit to
       - [ ] Choose a License
            
# elife data sharing checklist
elife guidelines states that the necessary program code, scripts for statistical package must be provided and sufficiently documented so that another informed researcher may replicates all published findings. 

elife recommends to publish only materials that can be reproduce under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/).
## Checklist
- [ ] Share HCP derivatives as planned 
- [ ] Edit and comment code so that anyone can replicate most of the figures
- [ ] Maybe add documentation on how to run Neurosynth on our collection shared on Neurovault
- [ ] Choose a license       
