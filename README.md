# NovoRank
NovoRank is a machine learning/deep learning-based algorithm that post-processes the De novo sequencing results.

- NovoRank is implemented and tested with

Python 3.x \
Numpy 1.21.0 \
Pandas \
DeepLC

## How to use NovoRank?

NovoRank performs three steps to obtain results, and you can test it using the sample data provided on Github.

> < step 1 > \
To write the location of input/output files and parameters in a config file (filling in experimental information) \
and perform clustering using MS-cluster software

**- config.txt**

<br/>

**- Input file format** 
1. De novo search result

Source File|Scan number|Peptide|Score
---|---|---|---|
Hela_1.mgf|10|HKPSVK|85|

2. DB search result

Source File|Scan number|GT
---|---|---|
Hela_1.mgf|3|KPVGAAK| 

<br/>

**- MS-Cluster**

MS-Cluster software is available for download at http://proteomics.ucsd.edu/software-tools/ms-clusterarchives/ \
Create a list of the full paths to the input files and call it list.txt. 

< Commend line >
```c
MSClsuter.exe --list list.txt --output-name CLUSTERS --assign-charges
``` 
<br/>

> < step 2 > \
Creating new candidates and generating features (In this step, two .py files were used.)

**1. main.py** \
To execute the main.py file, it is mandatory to have three inputs (De novo search result, MGF format files consisting of MS/MS spectra, Clustering results by MS-Cluster). DB search result is an essential input for training deep learning model, but it is not mandatory for testing.


```c
python main.py
```

**2. main_2.py**

```c
python main_2.py
```

> step 3

lll
