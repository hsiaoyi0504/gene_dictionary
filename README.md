# Gene Dictionary

Build simple gene dictionary using data from NCBI gene database.

## How to Use

1. Install the prerequisite and follow the installation steps shown below.
1. Choose one of two methods:
   - Acquire data through NCBI's API
     1. edit the list of genes in **search.py**
     1. `pipenv run search`
   - Use local copy of NCBI gene database
     1. edit the list of genes in **extract.py**
     1. `pipenv run extract`
1. result will be saved in **data.json**

### Prerequisite

- Python 3.7
- [pipenv](https://github.com/pypa/pipenv)
- [gene2xml](ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/README)

### Installation

``` shell
wget ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/ASN_BINARY/Mammalia/Homo_sapiens.ags.gz -O Homo_sapiens.ags.gz
gene2xml -i ./Homo_sapiens.ags.gz -o ./gene_database.xml -c T -l T -b T
pipenv install
```

## Run test

``` shell
pipenv install --dev
pipenv run test
```