import xml.etree.ElementTree as ET
import json


def get_text_attr(val):
    val = getattr(val, 'text', 'N/A')
    if val is None:
        val = 'N/A'
    return val


if __name__ == '__main__':
    # insert genes you want to build the dictionary into genes list below
    genes = ['TP53', 'CDH1']
    gene_dictionary = {}
    for event, elem in ET.iterparse('./gene_database.xml', events=('start',)):
        if elem.tag == 'Entrezgene':
            gene_name_tag = elem.find('Entrezgene_gene/Gene-ref/Gene-ref_locus')
            if gene_name_tag is None:
                pass
            elif gene_name_tag.text is None:
                pass
            else:
                gene_name = gene_name_tag.text
                if gene_name in genes:
                    summary_tag = elem.find('Entrezgene_summary')
                    summary_text = get_text_attr(summary_tag)
                    gene_dictionary[gene_name] = summary_text
        elem.clear()

    with open('data.json', 'w') as outfile:
        json.dump(gene_dictionary, outfile)
