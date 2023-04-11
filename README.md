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

NovoRank performs three steps to obtain result, and you can test it using the sample data and pre-trained model provided on 'sample' folder in NovoRank github repository and https://drive.google.com/drive/folders/1iLJP7NpX9PXnIXjDbx39OGloWh5XMo3p?usp=share_link.

- Example of running NovoRank 

After downloading all the sample data, collect them in a folder named 'sample' obtained from NovoRank gitHub repository, and run NovoRank.

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

MS-Cluster software and user’s manual are available for download at http://proteomics.ucsd.edu/software-tools/ms-clusterarchives/. Create a list of the full paths to the input files and call it list.txt. 

< Clustering to MS-Cluster using the following command line. >
```c
MSClsuter.exe --list list.txt --output-name CLUSTERS --assign-charges
``` 

<br/>

> < Step 2 > \
Creating new candidates and generating features ( in this step, two .py were used. )

**1. main.py** \
To execute the main.py, it is mandatory to have three inputs ( de novo search result, MGF format files consisting of MS/MS spectra, clustering results by MS-Cluster ). DB search result is an essential input for training deep learning model, but it is not mandatory for testing.

As output, create the top two candidate peptides and extract the features excluding XCorr and delta XCorr.

```c
python main.py
```

<br/>

**2. main_2.py** \
To extract the features of XCorr and delta XCorr using main_2.py, two inputs are required. The first input is the XCorr calculation result (.tsv) obtained using CometX, and the second input is the output data generated using main.py.

<br/>

**- CometX** \
To use CometX, you need to use the CometX.exe located in the 'sample' folder in the NovoRank gitHub repository.

The input for CometX consists of the parameter file (comet.params.new) and the .mgf files. The .mgf files used for CometX can be found in the mgf_XCorr folder inside the save folder where the main.py outputs are stored. The .tsv output files generated by CometX are also created in the mgf_XCorr folder.

The parameter file used in CometX is the same as the parameter file used in comet_version 2019.01 rev. 5. \
fragment ions parameters need to be changed to suit the experimental conditions.

< Calculate XCorr using the following command line of CometX. >

```c
CometX.exe -X -Pcomet.params.new .\save\mgf_XCorr\*.mgf
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

Test result and trained model are saved in the 'sample' folder.

