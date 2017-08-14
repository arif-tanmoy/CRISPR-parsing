#This Script summarizes the results of a CRISPR finding tool, CRISPRDetect in a tab-delimited file.
#It is pretty basic script. Sorry for my lack of knowledge. Improve/modify it as you need. 
#Citing CRISPRDetect: Biswas A et al (2016). https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2627-0

#Author: Arif Tanmoy
#Email: arif.m.tanmoy@gmail.com
#USE: Python SummarizeCRISPRDetect.py <CRISPRDetect_result_file> <Parsed_File>
#OUTPUT_FORMAT: primary_Repeat, alternative_repeat, repeat_no, repeat_len, identity, spacer_length, contig/seq_name, contig/seq_end_position, questionable_array(yes/no), score, LeftFlankSeq, RightFlankSeq
#**Silent line 60 if you do not want to print/see the results on commandline**

import sys
from numpy import *
infile=open (sys.argv[1], 'r')
outfile=open (sys.argv[2], 'w')
spc="     "
dot="......"
pos="Position"
arrow=">"
array="Questionable array"
prim="Primary repeat :"
alter="Alternate repeat"
left="Left flank"
right="Right flank"
for cur in infile:
	if arrow in cur:
		line=cur.rstrip()
		contig0=line.split('\t')[0].strip()
		contig=contig0.replace(">", "")
	elif dot in cur:
		line=cur.rstrip()
		end=line.split('\t')[0].strip()
	elif (spc in cur and \
	 dot not in cur and \
	 pos not in cur and \
	 prim not in cur): 
	 	line=cur.rstrip()
	 	a,b,c,d,e = str(line).split()
		repeat_no=a.strip()
		repeat_len=b.strip()
		ident=c.strip()
		spacer_len=d.strip()
	elif left in cur:
		line=cur.rstrip()
		leftfl=line.split(":")[1].strip()
	elif right in cur:
		line=cur.rstrip()
		rightfl=line.split(":")[1].strip()
	elif array in cur:
		line=cur.rstrip()
		qarray=line.split(': ')[1].split('Score')[0].strip()
		score=line.split('Score: ')[1].strip()
	elif prim in cur:
		line=cur.rstrip()
		prepeat=line.split(':')[1].strip()
	elif alter in cur:
		line=cur.rstrip()
		arepeat=line.split(':')[1].strip()
		info='%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (prepeat, arepeat, repeat_no, repeat_len, ident, spacer_len, contig, end, qarray, score, leftfl, rightfl)
		outfile.write(info)
		print info
infile.close()
outfile.close()
