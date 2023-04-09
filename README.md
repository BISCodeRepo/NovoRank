# NovoRank
NovoRank is a machine learning/deep learning-based algorithm that post-processes the De novo sequencing results.

- NovoRank is implemented and tested with

Python 3.x \
Numpy 1.21.0 \
Numba \
Pandas \
DeepLC ( https://github.com/compomics/DeepLC )

Scikit-learn \
Tensorflow

## How to use NovoRank?

NovoRank performs three steps to obtain result, and you can test it using the sample data and pre-trained model provided on Github and https://drive.google.com/drive/folders/1iLJP7NpX9PXnIXjDbx39OGloWh5XMo3p?usp=share_link.

- Example of running NovoRank 

After downloading all the sample data, collect them in a folder named "sample" obtained from GitHub, and run NovoRank.

<br/>

> < Step 1 > \
To write the location of input/output data and parameters in a config file ( filling in experimental information ) \
and perform clustering using MS-cluster software

**- config.txt**

All options can be found in "config.txt".

<br/>

**- Input data format** 

1. De novo search result (.csv)

Source File|Scan number|Peptide|Score
---|---|---|---|
Hela_1.mgf|10|HKPSVK|85|

2. DB search result (.csv)

Source File|Scan number|GT
---|---|---|
Hela_1.mgf|3|KPVGAAK| 

<br/>
NovoRank handles two types of modifications : 
<br/>
<br/>

1. Fixed modification : Carbamidomethylation on Cys (C)
2. Variable modification : Oxidation on Met (m)

In NovoRank, amino acids are represented as "C" and "m" for fixed and variable modifications, respectively.

<br/>

**- MS-Cluster**

MS-Cluster software is available for download at http://proteomics.ucsd.edu/software-tools/ms-clusterarchives/ . \
Create a list of the full paths to the input files and call it list.txt. 

< Clustering to MS-Cluster using the following command line. >
```c
MSClsuter.exe --list list.txt --output-name CLUSTERS --assign-charges
``` 

<br/>

> < Step 2 > \
Creating new candidates and generating features ( in this step, two .py were used. )

**1. main.py** \
To execute the main.py, it is mandatory to have three inputs ( de novo search result, MGF format files consisting of MS/MS spectra, clustering results by MS-Cluster ). DB search result is an essential input for training deep learning model, but it is not mandatory for testing. \
As output, create the top two candidate peptides and extract the features excluding XCorr and delta XCorr.

```c
python main.py
```

<br/>

**2. main_2.py** \
To extract the features of XCorr and delta XCorr using main_2.py, two inputs are required. The first input is the XCorr calculation result (.tsv) obtained using CometX, and the second input is the output data generated using main.py.

< Calculate XCorr using the following command line of CometX. >

```c
CometX.exe -X -PParameter.params .\*.mgf
``` 

After calculating XCorr,

```c
python main_2.py
```

<br/>

> < Step 3 > \
Deep learning model training or testing

The main_2.py executed in Step 2 performs feature extraction and then proceeds to train and test the deep learning model for re-ranking.\
The deep learning model only handles peptides with a maximum mass of 5000 Da and a length of 40 or less.

**1. Testing** \
Using a pre-trained model ( NovoRank.h5 ), perform testing and output a single assigned peptide for each spectrum as the result.

**2. Training** \
The deep learning model is trained based on the hyper-parameters set in the config.txt. \
The trained model is saved in the .h5 format as the output.
