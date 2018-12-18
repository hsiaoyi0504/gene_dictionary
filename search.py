import json
from Bio import Entrez


Entrez.email = 'hsiaoyi0504@gmail.com'


def search(gene_name, organism='human'):
    handle = Entrez.esearch(db='gene', retmax=1, term='{}[ORGN] AND {}[GENE]'.format(organism, gene_name), idtype='acc')
    record = Entrez.read(handle)
    handle.close()
    handle = Entrez.esummary(db='gene', id=record['IdList'][0])
    record = Entrez.read(handle)
    return str(record['DocumentSummarySet']['DocumentSummary'][0]['Summary'])


def test_search():
    summary_text = search('tp53')
    assert type(summary_text) is str
    assert len(summary_text) != 0


if __name__ == '__main__':
    # insert genes you want to build the dictionary into genes list below
    genes = ['TP53', 'CDH1']
    gene_dictionary = {}
    for gene_name in genes:
        gene_dictionary[gene_name] = search(gene_name)
    with open('data.json', 'w') as outfile:
        json.dump(gene_dictionary, outfile)
