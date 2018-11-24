from Bio import Entrez

Entrez.email = 'hsiaoyi0504@gmail.com'

def search(gene_name):
    handle = Entrez.esearch(db='gene', retmax=10, term='human[ORGN] AND {}[GENE]'.format(gene_name), idtype='acc')
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
    genes = ['TP53', 'CDH1']
    gene_dictionary = {}
    for gene_name in genes:
        gene_dictionary[gene_name] = search(gene_name)
    print(gene_dictionary)
    