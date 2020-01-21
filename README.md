# CRISPRDetect-parsing

**This Script summarizes the results of a CRISPR finding tool, CRISPRDetect in a tab-delimited file.**

### USE: 
**python _SummarizeCRISPRDetect.py <CRISPRDetect_result_file> <Parsed_File>_**

### OUTPUT_FORMAT:_(TAB separated)_
*primary_Repeat, alternative_repeat, repeat_no, repeat_len, identity, spacer_length, contig/seq_name, contig/seq_end_position, questionable_array(yes/no), score, LeftFlankSeq, RightFlankSeq*

*Silent line 60 if you do not want to print/see the results on commandline*

### Requirements
'''
=> python 2.7
=> packages: sys, numpy
'''

#### Citing CRISPRDetect: 
>Biswas A et al (2016). https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2627-0
